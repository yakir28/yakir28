# Brag Plan: ElevenLabs (Eleven v3)

## What is this app?
ElevenLabs turns text into lifelike speech. Eleven v3 is its most expressive Text to Speech model: 70+ languages, multi-speaker dialogue, and inline audio tags like [whispers], [excited] and [sighs] that direct the delivery.

## The angle
Words have always been silent. Eleven v3 is the moment they get a voice, and a director. The film treats a line of text like a lead actor waking up: it starts as a dead, flat line on black, then it breathes, takes direction ([whispers] / [excited] / [laughs]), gets a scene partner, and goes global.

## Hook (first 2-3 seconds)
Pure black. A caret blinks, and a sentence types out in big serif: "Words were silent." A flat hairline (a waveform with no signal) runs under it. The narration lands over it: "For a long time, words on a page stayed silent."

## Key moments (the middle)
- The flatline ignites into a living waveform as the ElevenLabs wordmark lands on a cinematic hit.
- An editor line gets directed: audio tags type in as pills ([whispers] → [excited] → [laughs]) and the waveform under each line changes character (small and breathy → spiky → bouncing).
- A two-speaker dialogue trades turns. Each speaker's waveform lights up in sequence.
- "Hello" rolls through languages (Hola, Bonjour, Hallo, Ciao, こんにちは, Olá, Привет...) up to "70+ languages".

## Outro / punchline
The waveform folds into the ElevenLabs wordmark. "Eleven v3" and "The most expressive Text to Speech model". Narration: "ElevenLabs. Give your words a voice." Final hit, then hold.

## User flow worth showing
Type a line → add an audio tag to direct it → hear (see) it delivered. Then: two speakers in one conversation → any language.

## Tone
- Preset: cinematic
- Creative direction: trailer for a voice: dark, intimate, big serif type, slow camera push-ins, light sweeps
- Interpretation: fewer, larger moments. Full-bleed type, slow drift and scale on every scene, dramatic crossfades with scale and blur, restraint in SFX (2-3 big hits), with the narration carrying the story.

## Format: vertical — 1080x1920
## Duration: 22.5s

## Visual identity
ElevenLabs.io was blocked by this environment's network policy, so the identity follows ElevenLabs' public look: monochrome black/white, minimal, plus a soft gradient "voice orb".
- Background: #0B0A09 (warm black)
- Text: #F3F0EA (warm off-white)
- Accent: gradient orb #FFB59A → #C9B6FF → #8EC5FF; waveform in #F3F0EA
- Display font: Instrument Serif (cinematic headlines)
- Body/UI font: Manrope; JetBrains Mono for audio tags; Noto Sans JP for Japanese
- Strongest visual element: the waveform/voice orb reacting to speech

## Share copy (draft)
Words were silent. Eleven v3 gave them a voice, a director, and 70+ languages.

## Voiceover script
Kokoro `af_heart` via `npx hyperframes tts`, one clip per line, placed per scene:
1. (0.6s) "For a long time, words on a page stayed silent."
2. (4.4s) "Then, they learned to speak."
3. (7.8s) "Now, you can tell them how. Whisper it. Shout it. Laugh."
4. (12.7s) "Cast a whole conversation, speaker by speaker."
5. (16.1s) "In more than seventy languages."
6. (19.1s) "ElevenLabs. Give your words a voice."
Music ducks to ~0.14 under each line and returns between lines.

## Audio direction
- Role: cinematic support
- Music: original cinematic score composed for this cut (dark drone + sub pulse in the hook, braam hit on the reveal, a soft 8th-note piano/pluck ostinato under the highlights, riser into a final hit on the logo). Composed to the scene grid, so the hits land on the cuts.
- Music treatment: fade in from silence, duck under narration, swell into the logo, ring out.
- Music cue guidance: custom track; cues detected at composition time with `npx hyperframes beats`. Planned strong cues: 4.0s (reveal), 18.6s (logo).
- Audio-reactive treatment: subtle. The voice orb and waveforms breathe with the narration/music energy. No equalizer bars or generic visualizers.
- SFX posture: sparse. Keypresses on the typed hook (thinned), impactBell_heavy on the reveal and logo, impactSoft_medium on the language roll, soft drops for tag pills.
- Restraint rule: nothing harsh under the narration. SFX sit below the voice.

## Storyboard

### Scene 1 — Silence — 4.0s
Black. Caret blinks, "Words were silent." types out in big serif. A flat hairline under it, slow camera push-in.
Sequential/interaction: yes, typed hook with keypress ticks.
Audio intent: low drone, heartbeat sub pulses, tension.
Transition mood: dramatic → the flatline ignites (light sweep) into Scene 2.

### Scene 2 — Reveal — 3.4s
The flatline becomes a living waveform. The gradient voice orb blooms behind it, then the ElevenLabs wordmark lands on the hit, with "Eleven v3" under it.
Audio intent: braam hit, warm swell.
Transition mood: crossfade with scale → Scene 3.

### Scene 3 — Direct it — 5.0s
Editor card (product UI). Three lines with audio tags typed in as pills: "[whispers] I have a secret." / "[excited] We did it!" / "[laughs]". Each line's waveform renders in that character as its tag lands. Caption: "Direct the delivery."
Sequential/interaction: yes, tags typed one by one (held, readable).
Audio intent: ostinato enters, soft drops on each pill.
Transition mood: push → Scene 4.

### Scene 4 — Dialogue — 3.4s
Two speakers (Speaker 1 / Speaker 2) trade turns in a conversation thread. The active speaker's waveform lights up. Caption: "Multi-speaker dialogue."
Transition mood: blur crossfade → Scene 5.

### Scene 5 — Languages — 2.8s
"Hello" rolls through languages in big serif, landing on "70+ languages".
Audio intent: soft impact on the landing.
Transition mood: light sweep → Scene 6.

### Scene 6 — Logo — 3.9s
The orb settles, the ElevenLabs wordmark, then "Eleven v3", then "The most expressive Text to Speech model". Hold.
Audio intent: final hit, chord rings out.

**Music mood for this video:** cinematic
**Audio summary:** silence and a heartbeat become a voice, then the score opens up under the narration and closes on one big hit.
