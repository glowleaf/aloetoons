You’re right — I gave you concepts, but not an **exportable pack** you can actually run. Here’s a full “drop-in” export: **characters + voice rules + dialogue + scripts + asset naming + Replicate prompts + Cursor workflow files**.

---

## 0) What you are building

A tiny mascot content factory:

**Mascot stills (PNG/WebP) → Replicate image-to-video (5–8s idle motion) → optional VO mux → final MP4**

No CapCut animation. No rigging.

---

# 1) The 3 mascots (exportable character bibles)

## A) Omega-3 Mascot — **Captain Arctic**

**Role:** calm ship captain, competent, slightly smug
**Catchphrase:** “captain’s log…”
**Energy:** reassuring + dry humor
**Never says:** medical claims, “cure/treat/heal,” diagnoses
**Visual add-ons (optional):** tiny sailor cap + anchor pin

### Captain Arctic: 20 one-liners (first-person)

1. “captain’s log: you ate zero fish today. again.”
2. “i’m not exciting. i’m reliable. like a good ship.”
3. “focus isn’t a vibe. it’s a routine.”
4. “you want smooth sailing? stop feeding your brain chaos.”
5. “i was born for boring consistency.”
6. “no, i’m not dramatic. i’m preventative.”
7. “captain’s log: we are not panic-checking today.”
8. “if you live on caffeine and hope, i have questions.”
9. “i’m the tiny habit you forget… until you remember.”
10. “i don’t chase trends. i do steady.”
11. “captain’s log: someone is ‘starting monday’ again.”
12. “your attention span is in a storm. i brought a compass.”
13. “i’m ocean energy in a civilized container.”
14. “your diet is a pirate raid. i’m the navy.”
15. “i like schedules. and water. mostly water.”
16. “captain’s log: today we choose calm.”
17. “i’m the quiet upgrade you don’t notice… until you stop.”
18. “i’m not a miracle. i’m maintenance.”
19. “i keep the ship tight. you keep the drama low.”
20. “captain’s log: take it easy. stay consistent.”

---

## B) Clean 9 Mascot — **Box Boss Nine**

**Role:** drill-sergeant coach / boss fight
**Catchphrase:** “day [x]. no excuses.”
**Energy:** intense but funny
**Never says:** extreme promises (“lose X kg”), medical claims
**Visual add-ons:** gloves, timer/stopwatch badge, pointing hand

### Box Boss Nine: 20 one-liners

1. “day 1. welcome. i’m structure.”
2. “i’m not a vibe. i’m a schedule.”
3. “people love ‘change’ until i show up.”
4. “day 2: confidence. day 3: bargaining.”
5. “you said you wanted discipline. surprise.”
6. “i don’t do motivation. i do checklists.”
7. “day 4: you stop negotiating with yourself.”
8. “i’m the boss fight you keep delaying.”
9. “if you want easy, scroll. if you want progress, follow me.”
10. “day 5. you’re not dying. you’re adapting.”
11. “i am nine days of ‘do it anyway.’”
12. “you can’t manifest your way out of habits.”
13. “day 6: stop romanticizing chaos.”
14. “i’m not mean. i’m consistent.”
15. “day 7: you start trusting yourself again.”
16. “you wanted a reset. i brought paperwork.”
17. “day 8: you realize you’re tougher than your cravings.”
18. “day 9: you win. and i judge your next excuse.”
19. “i don’t care how you feel. i care what you do.”
20. “day x: show up. again.”

---

## C) Probiotics Mascot — **Professor Bifido**

**Role:** nerdy gut professor, wholesome gross humor
**Catchphrase:** “today in gut news…”
**Energy:** comedic “logistics manager”
**Never says:** “treats IBS/constipation” etc; keep it vibe + routine
**Visual add-ons:** glasses, bowtie, clipboard

### Professor Bifido: 20 one-liners

1. “today in gut news: your stomach is filing complaints.”
2. “i handle… internal logistics.”
3. “your gut is a city. i run the night shift.”
4. “i don’t do drama. i do regular.”
5. “if your belly is making whale sounds, i’d like a word.”
6. “i’m the peace treaty between you and your stomach.”
7. “you can’t build a calm gut on chaos snacks.”
8. “i bring order. you bring water. deal?”
9. “i’m small. my job is not.”
10. “today in gut news: we are not gambling with dairy.”
11. “i’m not glamorous. i’m necessary.”
12. “some heroes wear capes. i do spreadsheets.”
13. “your gut wants consistency. not surprises.”
14. “i live for routine. and so do you.”
15. “today in gut news: less panic. more water.”
16. “i’m the quiet friend you forget to invite.”
17. “your stomach isn’t angry. it’s confused.”
18. “i don’t judge. i document.”
19. “i’m here to make things… predictable.”
20. “today in gut news: we’re restoring order.”

---

# 2) Asset extraction + naming (so your pipeline is deterministic)

Create one folder per mascot, and export **6 expressions** each (same size, transparent if possible).

### Folder structure

```
assets/
  captain_arctic/
    neutral.png
    happy.png
    smug.png
    angry.png
    sad.png
    wink.png
  box_boss_nine/
    neutral.png
    happy.png
    smug.png
    angry.png
    sad.png
    wink.png
  professor_bifido/
    neutral.png
    happy.png
    smug.png
    angry.png
    sad.png
    wink.png
```

### “Good enough” cropping rules

* Export all at **1024×1024** (or 768×768), centered
* Keep background simple/solid (or transparent)
* Avoid tiny label text if possible (reduces “melt” in I2V)

---

# 3) Replicate “golden prompts” (copy/paste)

## A) Idle motion (most reliable)

**Prompt:**

> cute cartoon product mascot, static camera, subtle idle motion, gentle bounce, blinking eyes, tiny friendly wave, clean simple studio background, no camera movement, no cuts, keep logo stable, keep label stable, 5 seconds

**Negative (if supported by model):**

> warping, melting, extra arms, extra fingers, changing logo, changing text, camera shake, zoom, cuts, flicker

## B) Talk-ish motion (still simple)

> cute cartoon product mascot, static camera, subtle head bob, blinking, small hand gesture, no cuts, keep logo stable, keep label stable, 6 seconds

---

# 4) 30 ready micro-scripts (10 per mascot)

These are designed for **5–8s clips**, and can be VO’ed later, or just subtitles.

### Captain Arctic (10 scripts)

1. “captain’s log. you ate zero fish today. again.”
2. “i’m omega-3. i’m not exciting. i’m reliable.”
3. “captain’s log: we are not panic-checking today.”
4. “focus isn’t a vibe. it’s routine.”
5. “i’m the quiet upgrade you forget… until you stop.”
6. “captain’s log: today we choose calm.”
7. “your attention span is in a storm. i brought a compass.”
8. “i’m not a miracle. i’m maintenance.”
9. “captain’s log: start small. stay consistent.”
10. “steady habits beat dramatic plans. every time.”

### Box Boss Nine (10 scripts)

1. “day 1. welcome. i’m structure.”
2. “i’m not a vibe. i’m a schedule.”
3. “day 2: confidence. day 3: bargaining.”
4. “you wanted change. i brought paperwork.”
5. “day 4: stop negotiating with yourself.”
6. “i am nine days of ‘do it anyway.’”
7. “day 6: stop romanticizing chaos.”
8. “day 7: you start trusting yourself again.”
9. “day 8: you realize you’re tougher than excuses.”
10. “day 9: you win. don’t get cocky.”

### Professor Bifido (10 scripts)

1. “today in gut news: your stomach is filing complaints.”
2. “i handle internal logistics. you’re welcome.”
3. “your gut is a city. i run the night shift.”
4. “i don’t do drama. i do regular.”
5. “if your belly is making whale sounds, i’d like a word.”
6. “today in gut news: less panic. more water.”
7. “your stomach isn’t angry. it’s confused.”
8. “i don’t judge. i document.”
9. “today in gut news: we’re restoring order.”
10. “i’m not glamorous. i’m necessary.”

---

# 5) “Export instructions” for Cursor (actual runnable workflow)

This is a better version of the Cursor task that includes **characters + scripts + file formats** and a simple **CSV-driven runner**.

### Create a CSV: `scripts.csv`

```
mascot,expression,style,text
captain_arctic,smug,idle,captain’s log. you ate zero fish today. again.
captain_arctic,neutral,idle,i’m omega-3. i’m not exciting. i’m reliable.
box_boss_nine,angry,idle,day 1. welcome. i’m structure.
box_boss_nine,smug,idle,i’m not a vibe. i’m a schedule.
professor_bifido,happy,idle,today in gut news: your stomach is filing complaints.
professor_bifido,smug,idle,i handle internal logistics. you’re welcome.
```

### Cursor build prompt (copy/paste)

Build a Python project that:

* loads `scripts.csv`
* for each row, finds the image at `assets/{mascot}/{expression}.png`
* calls Replicate image-to-video using model adapters
* writes `output/{mascot}__{expression}__{model}__{duration}s.mp4`
* writes `output/{...}.json` with prompt, negative prompt, model id, and the script text
* supports `--model kling|svd`, `--duration`, `--aspect`, `--limit`, `--force`
* does NOT do any editing or audio muxing (save video only)
* prints a clean progress table

Dependencies: replicate, python-dotenv, pandas, typer, rich

Also include a `prompts.py` preset dictionary:

* idle: (golden prompt above)
* talk: (talk-ish prompt above)

Adapters must have an `INPUT_MAP` that can be edited if Replicate model keys differ.

---

# 6) Optional: add voice with *near-zero fuss* (no CapCut)

If you want the mascot to “talk” (audio), the least-fuss way is **ffmpeg mux** (one command). This is optional and doesn’t involve animation editing.

1. Generate VO MP3 (ElevenLabs / any TTS) and save as:
   `vo/{same_basename}.mp3`

2. Mux audio:

```bash
ffmpeg -y -i output/FILE.mp4 -i vo/FILE.mp3 -c:v copy -c:a aac -shortest final/FILE.mp4
```

That’s literally it.

---

## Quick sanity checklist (why your I2V sometimes fails)

If videos look melty:

* use the **cartoon mascot** image (not the photo product)
* reduce duration to **5s**
* enforce **static camera**
* simplify/blur micro label text

---

If you want, I can also output a **ready `scripts.csv` with all 30 lines** already mapped to expressions (so you can run it immediately).
