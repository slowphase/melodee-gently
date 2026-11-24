# Changelog

## v1.1 (25 November 2026)

Documents Melodee 1.6.1, unchanged from v1.0. A focused revision: same look, voice, eight lessons and single project.

- **Panel numbers fixed and now automatic.** Each lesson's panel is generated from its own numbered steps: every control the steps use is lit, and each pink number is the first step that uses it. This fixes Lesson 8, where FX read 21 and SAVE 23 although the lesson ends at step 20 (they're now 17 and 20). It also fixes smaller mismatches elsewhere. Badges were redrawn so they no longer cover neighbouring buttons. The generated list is in `docs/PANEL-NUMBERS.md`.
- **Example screens.** The panel drawings now show a simplified example of the relevant page (Stage, the browser, SCALES, CHORD, the drum grid, AMP ENV, the reverb, SONG), each marked EXAMPLE and captioned as not a screenshot.
- **Capture, rewritten (Lesson 5).** Adds a rehearsal: count four beats per bar with the kick and change chord once per bar. Explains exactly when to hold REC (on the next "one", before playing chord 1 again), what success looks like (CAPTURED 4 BARS, chord 1 first) and how to undo and retry (hold EDIT, and undo before recapturing, because a new capture layers on top). Includes the RECORDING and NOTHING TO CAPTURE messages and a "How Capture decides" box. All checked against the 1.6.1 source.
- **REC + PLAY wording.** Now "hold REC and press PLAY straight away", matching how the firmware reads the gesture.
- **The lead in Lesson 7.** Says plainly that track 3 has no pattern until Lesson 8: play notes by hand to hear the reverb and echo, and set its level roughly for now.
- **Gentler promises.** "Nothing can sound wrong" and "nothing clashes" now say that every key stays inside your chosen scale, without promising every combination sounds equally settled.
- **"I can't hear anything" checklist** added to If something goes wrong: MASTER, headphones or speakers, the selected track (and MIDI-only tracks 5 to 8), mute, solo and level, empty patterns, transport, and slow-attack sounds. Lesson 1 links to it.
- Edition bumped to v1.1. Credits and licence unchanged.

## v1.0 (25 November 2026)

First edition, documenting Melodee 1.6.1.
