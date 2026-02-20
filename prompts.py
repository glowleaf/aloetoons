"""Prompt presets for Replicate image-to-video."""

IDLE_PROMPT = (
    "cute cartoon product mascot, static camera, subtle idle motion, "
    "gentle bounce, blinking eyes, tiny friendly wave, clean simple studio background, "
    "no camera movement, no cuts, keep logo stable, keep label stable"
)

TALK_PROMPT = (
    "cute cartoon product mascot, static camera, subtle head bob, blinking, "
    "small hand gesture, no cuts, keep logo stable, keep label stable"
)

NEGATIVE_PROMPT = (
    "warping, melting, extra arms, extra fingers, changing logo, changing text, "
    "camera shake, zoom, cuts, flicker"
)

PROMPTS = {"idle": IDLE_PROMPT, "talk": TALK_PROMPT}
