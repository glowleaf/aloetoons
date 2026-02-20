"""
Generate mascot videos via Replicate (Kling 2.6).
Reads scripts.csv, loads images from assets/, writes MP4s to output/.
Uses REPLICATE_API_TOKEN from .env
"""
import json
import sys
from pathlib import Path

import pandas as pd
import replicate
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from prompts import NEGATIVE_PROMPT, PROMPTS

load_dotenv()

if not __import__("os").environ.get("REPLICATE_API_TOKEN"):
    print("REPLICATE_API_TOKEN not set. Add it to .env in this folder.")
    sys.exit(1)

app = typer.Typer()
console = Console()

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL = "kwaivgi/kling-v2.6"


def get_prompt(style: str, text: str, with_audio: bool) -> str:
    base = PROMPTS.get(style, PROMPTS["idle"])
    if with_audio and text:
        return f'{base}. Character says "{text}"'
    return base


@app.command()
def main(
    limit: int = typer.Option(None, "--limit", "-l", help="Process only first N rows"),
    duration: int = typer.Option(5, "--duration", "-d", help="Video duration in seconds (5 or 10)"),
    aspect: str = typer.Option("1:1", "--aspect", "-a", help="Aspect ratio: 1:1, 16:9, 9:16"),
    force: bool = typer.Option(False, "--force", "-f", help="Regenerate even if output exists"),
    no_audio: bool = typer.Option(False, "--no-audio", help="Disable Kling audio (add VO later)"),
):
    scripts_path = PROJECT_ROOT / "scripts.csv"
    if not scripts_path.exists():
        console.print("[red]scripts.csv not found[/red]")
        raise typer.Exit(1)

    df = pd.read_csv(scripts_path)
    if limit:
        df = df.head(limit)

    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    table = Table(title="Batch run")
    table.add_column("Row", style="dim")
    table.add_column("Mascot", style="cyan")
    table.add_column("Expression", style="green")
    table.add_column("Status", style="yellow")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for i, row in df.iterrows():
            mascot = row["mascot"]
            expression = row["expression"]
            style = row.get("style", "idle")
            text = str(row.get("text", ""))

            image_path = PROJECT_ROOT / "assets" / mascot / f"{expression}.png"
            if not image_path.exists():
                table.add_row(str(i + 1), mascot, expression, "[red]SKIP: image missing[/red]")
                continue

            out_name = f"{mascot}__{expression}__kling26__{duration}s"
            out_mp4 = output_dir / f"{out_name}.mp4"
            out_json = output_dir / f"{out_name}.json"

            if out_mp4.exists() and not force:
                table.add_row(str(i + 1), mascot, expression, "[dim]SKIP: exists[/dim]")
                continue

            task = progress.add_task(f"{mascot} {expression}...", total=None)
            prompt = get_prompt(style, text, with_audio=not no_audio)

            try:
                with open(image_path, "rb") as f:
                    output = replicate.run(
                        MODEL,
                        input={
                            "prompt": prompt,
                            "start_image": f,
                            "duration": duration,
                            "aspect_ratio": aspect,
                            "generate_audio": not no_audio,
                            "negative_prompt": NEGATIVE_PROMPT,
                        },
                    )

                video_url = str(output) if hasattr(output, "__str__") else output
                if hasattr(output, "url"):
                    video_url = output.url()
                if isinstance(video_url, str) and video_url.startswith("http"):
                    import urllib.request
                    urllib.request.urlretrieve(video_url, out_mp4)
                elif hasattr(output, "read"):
                    with open(out_mp4, "wb") as fp:
                        fp.write(output.read())
                else:
                    console.print("[red]Unexpected output format[/red]")
                    table.add_row(str(i + 1), mascot, expression, "[red]FAIL[/red]")
                    progress.remove_task(task)
                    continue

                with open(out_json, "w") as fp:
                    json.dump(
                        {"prompt": prompt, "negative_prompt": NEGATIVE_PROMPT, "model": MODEL, "text": text},
                        fp,
                        indent=2,
                    )

                table.add_row(str(i + 1), mascot, expression, "[green]OK[/green]")
            except Exception as e:
                table.add_row(str(i + 1), mascot, expression, f"[red]FAIL: {e}[/red]")

            progress.remove_task(task)

    console.print(table)


if __name__ == "__main__":
    app()
