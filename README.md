# Aloe Toons

Mascot video workflow using Replicate (Kling 2.6 + Nano Banana).

## Setup

1. **Generate expressions** from source mascots (run once):
   ```bash
   python generate_expressions.py
   ```
   Uses Nano Banana to create neutral/happy/smug/angry/sad/wink for each mascot from: `aloe vera mascot.png`, `clean9 mascot.png`, `omega 3 mascot.png`, `probiotics mascot.png`

2. Or put mascot images manually in `assets/{mascot}/{expression}.png` (e.g. `assets/captain_arctic/neutral.png`)
3. Add `REPLICATE_API_TOKEN` to `.env`
4. `pip install -r requirements.txt`

## Run

```bash
python run.py
```

Options:
- `--limit 5` — process only first 5 rows
- `--duration 5` or `10` — clip length
- `--aspect 1:1` or `16:9` or `9:16`
- `--force` — regenerate even if output exists
- `--no-audio` — skip Kling audio (add voice-over later with ffmpeg)

## Add voice-over later

```bash
ffmpeg -y -i output/FILE.mp4 -i vo/FILE.mp3 -c:v copy -c:a aac -shortest final/FILE.mp4
```

Save TTS as `vo/{same_basename}.mp3` to match the output file.
