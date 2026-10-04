# Hyperframes Composition Brief: ElevenLabs (Eleven v3)

## Objective
Create a short, cinematic, narrated brag video for ElevenLabs' Eleven v3.

## Output
- Composition directory: `composition/`
- Rendered video: `brag.mp4`
- Format: vertical — 1080x1920, 30fps
- Duration: 22.5s

## Source Material
- Source: public ElevenLabs messaging about Eleven v3 (elevenlabs.io was blocked by network policy; claims come from ElevenLabs' Eleven v3 announcement as indexed by search).
- Product name: ElevenLabs, Eleven v3
- Copy that must appear verbatim (grounded):
  - "The most expressive Text to Speech model"
  - "70+ languages"
  - Audio tags: "[whispers]", "[excited]", "[laughs]" (also "[sighs]")
  - "Multi-speaker dialogue"
- Invented/craft copy (no product claims): "Words were silent.", "Direct the delivery.", the sample script lines.

## Creative Direction
- Tone preset: cinematic, a trailer for a voice
- Angle: words were silent, and Eleven v3 gives them a voice and a director.
- Hook: caret plus typed "Words were silent." over a flatline, on black.
- Outro: ElevenLabs wordmark, Eleven v3, the "most expressive" claim.
- Avoid: generic SaaS language, equalizer/visualizer graphics, stock "AI" imagery.

## Visual Identity
- Background #0B0A09, text #F3F0EA, orb gradient #FFB59A / #C9B6FF / #8EC5FF
- Display: Instrument Serif. UI: Manrope. Tags: JetBrains Mono. Japanese: Noto Sans JP. All embedded via @font-face from local files.

## Storyboard
See brag-plan.md (6 scenes: Silence 4.0, Reveal 3.4, Direct 5.0, Dialogue 3.4, Languages 2.8, Logo 3.9).

## Audio
- Music: original cinematic score `assets/music/score.wav` at 0.32, ducked to ~0.14 under narration via a volume lane.
- Voiceover: Kokoro af_heart clips `assets/vo/vo1-6.wav` on their own track.
- SFX from /brag's Kenney library: keyboard keypresses (hook), impactBell_heavy (reveal + logo), interface drop (tag pills), impactSoft_medium (language landing).
- Audio-reactive: subtle orb/waveform presence driven by pre-extracted narration + music energy.
