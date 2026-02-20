"""
Generate 6 expressions per mascot using Replicate (Nano Banana).
Reads 4 source mascot images, creates neutral/happy/smug/angry/sad/wink for each.
Uses REPLICATE_API_TOKEN from .env
"""
import os
import sys
from pathlib import Path

import replicate
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()

if not os.environ.get("REPLICATE_API_TOKEN"):
    print("REPLICATE_API_TOKEN not set. Add it to .env")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL = "google/nano-banana"

# Source file -> assets folder
MASCOTS = {
    "aloe vera mascot.png": "aloe_vera",
    "clean9 mascot.png": "box_boss_nine",
    "omega 3 mascot.png": "captain_arctic",
    "probiotics mascot.png": "professor_bifido",
}

EXPRESSIONS = {
    "neutral": "Keep the mascot exactly as shown. Same expression and pose. Clean simple studio background, centered, 1024x1024.",
    "happy": "Change the mascot to have a happy, smiling expression. Same character, style, proportions. Clean simple studio background, centered, 1024x1024.",
    "smug": "Change the mascot to have a smug, confident, slightly amused expression. Same character, style, proportions. Clean simple studio background, centered, 1024x1024.",
    "angry": "Change the mascot to have an angry, intense, determined expression. Same character, style, proportions. Clean simple studio background, centered, 1024x1024.",
    "sad": "Change the mascot to have a sad, downcast, thoughtful expression. Same character, style, proportions. Clean simple studio background, centered, 1024x1024.",
    "wink": "Change the mascot to have a winking, playful, cheeky expression. Same character, style, proportions. Clean simple studio background, centered, 1024x1024.",
}


def main():
    console = Console()

    for source_file, mascot in MASCOTS.items():
        source_path = PROJECT_ROOT / source_file
        if not source_path.exists():
            console.print(f"[yellow]Skip {mascot}: {source_file} not found[/yellow]")
            continue

        out_dir = PROJECT_ROOT / "assets" / mascot
        out_dir.mkdir(parents=True, exist_ok=True)

        console.print(f"\n[cyan]{mascot}[/cyan] from {source_file}")

        for expr_name, prompt in EXPRESSIONS.items():
            out_path = out_dir / f"{expr_name}.png"
            if out_path.exists():
                console.print(f"  [dim]{expr_name}: exists[/dim]")
                continue

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task(f"  {expr_name}...", total=None)
                try:
                    with open(source_path, "rb") as f:
                        output = replicate.run(
                            MODEL,
                            input={
                                "prompt": prompt,
                                "image_input": [f],
                                "output_format": "png",
                            },
                        )

                    if hasattr(output, "read"):
                        with open(out_path, "wb") as fp:
                            fp.write(output.read())
                    elif hasattr(output, "url"):
                        import urllib.request
                        urllib.request.urlretrieve(output.url(), out_path)
                    elif isinstance(output, str) and output.startswith("http"):
                        import urllib.request
                        urllib.request.urlretrieve(output, out_path)
                    else:
                        console.print(f"  [red]{expr_name}: unexpected output[/red]")
                        progress.remove_task(task)
                        continue

                    console.print(f"  [green]{expr_name}: ok[/green]")
                except Exception as e:
                    console.print(f"  [red]{expr_name}: {e}[/red]")
                progress.remove_task(task)

    console.print("\n[green]Done.[/green]")


if __name__ == "__main__":
    main()
