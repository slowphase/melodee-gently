# Melodee, Gently v1.1: verification notes

Documented firmware: **Melodee 1.6.1** (tag `v1.6.1`, commit `165d177`).

Every instruction was checked against the official manual shipped with 1.6.1 (`web/manual/index.html`, identical at the tag and at the release merge). Where the manual is silent or vague, the 1.6.1 firmware source was read directly. Nothing has yet been tested on a physical FM-1.

## Facts taken from the source (not stated in the manual)

| Book says | Source |
|---|---|
| Tapping SAVE opens USER first; tapping again goes to PROJECT | `ui.c` open_family: SAVE enters GR_USER, same button again = next page |
| On USER, OCT+ opens the slot sheet already on Save here | `ui.c` slot_save_sheet |
| Holding SAVE on a new project: NEW PROJECT: PICK SLOT, then OCT+ names and saves | `project.c` (ui.act = 4) |
| New song wizard: KEY screen (ROOT, SCALE, TEMPO), OCT+, ROLES screen, OCT+ creates; KEEP with no template = power-on sounds | `ui_new.c` header comment |
| A family button reopens the page last used, so the book says "press X until..." | `ui.c` fam_last |
| On Prophet, FM6 and CZ-1, ENV opens the engine's own envelope pages; the shared ENV/ENV DEST pages are hidden | `ui.c` native_titles, page_visible |
| On those engines, LFO shows the engine's own LFO pages first, then LFO, LFO 2, LFO DEST, MOD | `ui.c` fam_pages |
| Prophet page knob layouts (AMP ENV, LFO, WHEEL, WHEEL 2, MOD FLT, UNISON) | `params.c` PAGES + `prophet_edit.h` |
| VINTAGE is on the MOD FLT page | `params.c` "P5 MOD FLT" |
| CHORD page knobs CHRD, VOIC, STRUM, STROKE (STROKE may show as DIR) | `params.c`, `ui_draw.c` |
| Drum grid: white keys = 16 steps, black keys 1 to 8 = lanes, 9 held = accent, 10/11 = page | `ui.c` drum grid comment, `ui_input.c` grid_keys |
| Lane order KICK SNARE CLAP HATCL HATOP TOM RIM BELL | `eng_drum.c` drum_lane_name |
| Pattern defaults LEN 16, DIV 1/16; tempo default 120 | `params.c` |
| Capture: notes from the last 64 steps set the span; the take ends at the end of the current bar if a note was played in it, else at its start; an empty pattern gets 16, 32 or 64 steps and its LEN set; a pattern with notes is layered over (identical notes skipped); success shows CAPTURED n BARS; refusals say RECORDING or NOTHING TO CAPTURE; EDIT held undoes | `ui_input.c` capture_take |
| Capture listens only to the selected track; switching tracks clears it; the buffer starts afresh at PLAY | `seq.c` cap_select, transport start |
| REC held 0.7 s = Capture; a shorter tap arms recording | `ui_input.c` btn_hold |
| PLAY pressed while REC is down records from the top, and releasing REC afterwards does not toggle arming | `ui_input.c` rec_play (rec_t0 marked used) |
| Chords and the arp apply only to live keys and MIDI, not to sequenced playback, so recorded chord or arp parts aren't doubled | `seq.c` input_on, key_chord_tone |
| Capture records keys held; with the ARP on, armed recording records the arp's notes | `seq.c` input_on, header comment |
| Recording QNT values include 1/16 | `params.c` N_RECQ |
| On SONG, OCT+ on the empty end column adds a section directly; on a section it opens the cell sheet; held OCT+ gives Duplicate section | `ui_popup.c` song_cell_sheet_open, SHEET_SONG |
| Sound browser: KNOB 1 list, 2 sound, 3 FAV, 4 engine | `ui_input.c` GR_BROWSE |
| FM6 Stage knobs MLVL, MRAT, MEG, DTUN | `eng_fm6.c` |

## Example screens

The v1.1 screens show only a page title and the four knob labels and values the manual gives for that page (Stage shows the four default sound names and the documented track colours). They are simplified, marked EXAMPLE, and are not screenshots. The SCALES page's KNOB 1 is labelled FAMILY after the manual's description; the real label may differ.

## Still to confirm on hardware

- Section and punch step numbering on a 64-step track 1 (START 49 / END 64).
- That the cursor lands on a newly added SONG section.
- MIDI clock out to an MPC Sample (Melodee's own notes: untested with real gear).
- Screen wording of the STROKE label, the QNT value names and the SCALES page KNOB 1 label.
- How precisely "a touch before the beat" a first chord can be played before Capture leaves it out (the source excludes notes before the window's first step).
