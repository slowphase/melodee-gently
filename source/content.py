"""Melodee, Gently: the text.

Markup inside strings (expanded by build.chips):
    [[EDIT]]   a button chip       [[@KNOB 1]]  a knob chip       [[~SAVED]]  text as shown on screen
Every instruction was checked against the Melodee 1.6.1 manual (web/manual at tag v1.6.1)
and, where the manual is silent, the 1.6.1 firmware source. See docs/VERIFICATION.md.
"""
import figures as F

FW = "1.6.1"
ED = "v1.1"


def steps(start, *items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ol class="steps" style="counter-reset: s {start - 1}">{lis}</ol>'


def box(kind, label, body):
    return f'<div class="callout {kind}"><span class="lab">{label}</span>{body}</div>'


def fig(svg, cap="", cls=""):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="{cls}">{svg}{c}</figure>'


def opener(n, title, lede, time, need, save, keys=False, run=None, screen=""):
    """The panel drawing is filled in by build.py: it lights every control the lesson's numbered steps use
    and numbers each one with the first step that uses it. screen names an example screen (build.SCREENS)."""
    run = run or f"Lesson {n} · {title}"
    return f"""
<section class="lesson" id="l{n}">
  <div class="run">{run}</div>
  <div class="kicker">Lesson {n}</div>
  <h2>{title}</h2>
  <p class="lede">{lede}</p>
  <div class="youneed">
    <div><b>Time</b>{time}</div>
    <div><b>You need</b>{need}</div>
    <div><b>You'll save</b>{save}</div>
  </div>
  <!--PANEL:{screen}-->
"""


# ===========================================================================
# FRONT MATTER
# ===========================================================================
COVER = f"""
<section class="cover">
  <div class="series">A Gently book</div>
  <div class="art">{F.cover_art()}</div>
  <h1>melodee, <span>gently</span></h1>
  <div class="sub">from first note to first song</div>
  <div class="rule"></div>
  <div class="blurb">A calm, illustrated beginner's guide to the five classic synths inside Melodee,
  and to turning them into a song of your own. No music theory needed.</div>
  <div class="meta">Documents Melodee {FW} for the M-VAVE FM-1 <span class="r">slowphase · {ED}</span></div>
</section>
"""

IMPRINT = f"""
<section class="imprint">
  <div class="run">Melodee, Gently</div>
  <div class="imp-top">
    <h3 class="imp-title">melodee, <em>gently</em></h3>
    <p class="imp-sub">From first note to first song</p>
  </div>
  <div class="imp-body">
  <p><b>Edition {ED}</b>, documenting <b>Melodee {FW}</b> on the M-VAVE FM-1. Melodee changes quickly.
  If your startup screen shows a different version, some names and screens may differ from this book.
  The stable manual at <span class="url">keremimo.github.io/melodee</span> always wins over this book.</p>
  <p>Every instruction was checked against the official Melodee {FW} manual and, where the manual says less, against the
  {FW} firmware source. It hasn't all been tried on a physical FM-1 yet. If something doesn't match your unit,
  please open an issue on this book's GitHub page.</p>
  <p>Written by <b>slowphase</b>. Part of the Gently series, alongside <em>SLOOP, Gently</em>, <em>MPC, Gently</em> and
  <em>Shrub, Gently</em>.</p>
  <p>This book is licensed under <b>Creative Commons Attribution-ShareAlike 4.0</b> (CC BY-SA 4.0). You may share and adapt
  it, as long as you credit it and share your version under the same licence.</p>
  <p class="small">Melodee is by Kerem Kilic (Ellic Studio), based on Felucca by Leo Kuroshita and Hügelton Instruments, and is
  licensed GPL-3.0-only. This book is an independent community guide. It is not affiliated with or endorsed by
  Ellic Studio, Hügelton Instruments, M-VAVE, Sequential, Casio, Akai or Commodore. M-VAVE, FM-1, Prophet-5, CZ-1,
  DX7, MPC and other names are trademarks of their respective owners. The book contains no screenshots; every
  illustration is drawn for it.</p>
  <p class="small">Melodee is field-testing firmware with no warranty. Installing any custom firmware is at your own risk.</p>
  </div>
</section>
"""

CONTENTS_ITEMS = [
    ("welcome", "Welcome"), ("panel", "Meet the panel"), ("movein", "Before you begin: moving in"),
    ("l1", "1 · Hello, Melodee"), ("l2", "2 · Five instruments in one box"), ("l3", "3 · Playing without wrong notes"),
    ("l4", "4 · Chords do the heavy lifting"), ("l5", "5 · Your first patterns"), ("l6", "6 · Making it move"),
    ("l7", "7 · Space and polish"), ("l8", "8 · Your first song"), ("mpc", "Optional: into the MPC"),
    ("sheets", "Engine cheat sheets"), ("holds", "Holds, taps and where things live"),
    ("midi", "MIDI and Bluetooth, briefly"), ("changes", "Coming from 1.5.1? What changed"),
    ("trouble", "If something goes wrong"), ("glossary", "Glossary"),
]

WELCOME = f"""
<section class="front" id="welcome">
  <div class="run">Welcome</div>
  <div class="kicker">Welcome</div>
  <h2>A little box with five big synths inside</h2>
  <p class="lede">Melodee turns your FM-1 into a small studio: five classic instruments, a sequencer, effects and a
  song arranger. This book walks you through all of it, one calm evening at a time.</p>
  <p>Inside Melodee live five instruments, each modelled on a famous synth from the 1970s and 80s. There's a warm
  polysynth in the style of the Prophet-5, a glassy six-operator FM engine compatible with the DX7, the Casio CZ-1's
  phase distortion, the Commodore 64's SID chip and a set of drum machines. Around them sits a sequencer that can
  record what you play, chord tools that keep every key inside your chosen scale, and an arranger that turns loops into a
  finished song.</p>
  <p>That's a lot. This book doesn't try to cover every page and setting; the official manual does that. Instead it
  takes one path through Melodee, the path from your first note to your first song, and explains each idea as you
  meet it.</p>
  <h3>How the book works</h3>
  <ul class="plain">
    <li><b>Eight lessons, one song.</b> From Lesson 3 onwards you build one project. By Lesson 8 it's a short
    finished song with an intro, a middle and an ending.</li>
    <li><b>Every lesson ends with something saved.</b> If you only have half an hour, finish a lesson, save, and
    put the FM-1 down.</li>
    <li><b>Only the controls you need are lit.</b> Each lesson starts with a panel drawing. Ignore everything that
    isn't lit.</li>
    <li><b>No music theory needed.</b> Where a little theory helps, it's in a "Why it works" box you can skip.</li>
  </ul>
  <h3>The boxes</h3>
  {box("try", "Try this", "A small detour for fun. Skip it if you're short on time.")}
  {box("why", "Why it works", "The idea behind what you just did, in plain words.")}
  {box("warn", "Careful", "Something that can lose your work. Amber is only ever used for this.")}
  {box("saved", "Saved today", "What you've made by the end of the lesson.")}
  <h3>Contents</h3>
  <ul class="toc">{"".join(f'<li><a href="#{a}">{b}</a></li>' for a, b in CONTENTS_ITEMS)}</ul>
</section>
"""

PANEL = f"""
<section class="front" id="panel">
  <div class="run">Meet the panel</div>
  <div class="kicker">Before the lessons</div>
  <h2>Meet the panel</h2>
  <p class="lede">Melodee uses the same handful of moves everywhere. Learn these five and you can find your way
  around any page.</p>
  {fig(F.fm1_panel(hl=("MASTER", "SELECT", "PRESETS", "ALGORITHM", "KNOB 1", "KNOB 2", "KNOB 3", "KNOB 4", "OCT-", "OCT+",
       "FX", "SCL", "ENV", "LFO", "EDIT", "GLO", "HOME", "SAVE", "ARP", "SEQ", "PLAY", "REC", "SCREEN"), keys_hl=True), "", "panelfig")}
  <table class="ref">
    <tr><th>Control</th><th>What it does</th></tr>
    <tr><td>[[@MASTER]]</td><td>Overall volume.</td></tr>
    <tr><td>[[@ALGORITHM]]</td><td>Chooses the track you're working on. The screen takes that track's colour.</td></tr>
    <tr><td>[[@PRESETS]]</td><td>Browses sounds. On an engine's edit pages it jumps between sections instead.</td></tr>
    <tr><td>[[@SELECT]]</td><td>Turns the pages of whatever section is open. On Stage it changes the tempo (BPM) by default.</td></tr>
    <tr><td>[[@KNOB 1]] to [[@KNOB 4]]</td><td>The four controls on the page you're looking at. On Stage, the four sound knobs of the selected track.</td></tr>
    <tr><td>[[FX]] [[SCL]] [[ENV]] [[LFO]] [[EDIT]] [[GLO]] [[ARP]] [[SEQ]]</td><td>Each opens its family of pages. Press it again for the next page.</td></tr>
    <tr><td>[[HOME]]</td><td>Back to Stage. Tap again on Stage for the chord view. Hold for the settings menu.</td></tr>
    <tr><td>[[SAVE]]</td><td>Tap to save a sound (tap again for projects). Hold to save your project to its slot.</td></tr>
    <tr><td>[[PLAY]]</td><td>Starts and stops.</td></tr>
    <tr><td>[[REC]]</td><td>Arms the selected track for recording. Hold to Capture what you just played.</td></tr>
    <tr><td>[[OCT-]] [[OCT+]]</td><td>On Stage they shift the octave. Everywhere else they mean back and enter.</td></tr>
  </table>
  <h3>The five moves</h3>
  <ul class="plain">
    <li><b>[[OCT+]] goes in, [[OCT-]] comes out.</b> Off Stage, the octave buttons are Enter and Esc. [[OCT-]] always
    closes the innermost thing first, so pressing it a few times always gets you home.</li>
    <li><b>[[@SELECT]] turns pages.</b> Whatever section you're in, [[@SELECT]] flips through its pages, both ways.</li>
    <li><b>On lists, [[@KNOB 2]] picks the row and [[@KNOB 1]] changes it.</b> The settings menu works like this.</li>
    <li><b>Hold [[OCT+]] for a sheet.</b> Many pages hide a short list of actions, such as Init sound or Copy to….</li>
    <li><b>Hold [[EDIT]] to undo.</b> It undoes the last sound or pattern change, or the last recording.</li>
  </ul>
  {fig(F.nav_fig())}
  {box("why", "Reading the lights", "The key and button lights share one simple language. Dark means nothing is there. Dim means something is there. Bright means it's happening now. A slow pulse means it's waiting, for example a pattern queued to start at the end of the loop.")}
</section>
"""

MOVEIN = f"""
<section class="front" id="movein">
  <div class="run">Before you begin · Moving in</div>
  <div class="kicker">Before you begin</div>
  <h2>Moving in</h2>
  <p class="lede">Installing Melodee takes a few minutes. Doing it carefully takes a few more, and that's time well
  spent.</p>
  {box("warn", "Back up first", "Whatever is on your FM-1 now won't come with you. Different firmwares store music in different ways. Save or export anything you care about using your current firmware's own tools before you start. If you're updating an older Melodee, make a backup with the Melodee web editor's backup tools and export your projects and user sounds: older firmware can't read what 1.6 saves, so that backup is your only way back.")}
  <h3>What you need</h3>
  <ul class="plain">
    <li>A computer with <b>Chrome or Edge</b>. Other browsers can't talk to the FM-1 over USB.</li>
    <li>A <b>data</b> USB cable, plugged straight into the computer. Charge-only cables won't work, and hubs can cause trouble.</li>
    <li>Your FM-1, powered and connected.</li>
  </ul>
  <h3>Coming from another firmware</h3>
  <p>If your FM-1 runs official firmware or an older Melodee, go straight to the install steps. If it runs another
  custom firmware (SLOOP, Shrub, GR!MM and so on), leave it the way that firmware recommends first. Many use
  TransitFM1 as a safe stop between firmwares, or a return to official V15. Once the FM-1 is running TransitFM1 or V15,
  carry on below.</p>
  <h3>Installing</h3>
  {steps(1,
    "Open <span class='url'>keremimo.github.io/melodee</span> in Chrome or Edge and choose the <b>installer</b>.",
    f"Connect the FM-1 and choose the <b>stable</b> channel. It should offer Melodee {FW}.",
    "Press <b>Install</b>. Leave the cable alone until writing finishes. Don't let the computer sleep.",
    f"When the FM-1 restarts, the startup screen shows the firmware version. Check it says {FW}.",
  )}
  {box("warn", "Updating from Melodee 1.5.1 or earlier without the web installer?", "If you use something else, such as Firmware Hub, <b>install twice</b>. The first install moves your old preset banks to a new home and shows <b>Setup unfinished</b>. The second install writes the factory sounds. The web installer handles this in one go. The first start after an update may show <b>MIGRATING PRESETS</b>: leave the power connected until it finishes.")}
  <h3>If it says "Setup unfinished"</h3>
  <p>Melodee keeps its factory sounds, the Rubik font and the Bluetooth program in their own area of memory. If they're
  missing, the FM-1 starts with <b>Setup unfinished</b> and <b>Factory sounds missing</b>. Your own sounds are safe.
  Open the installer and press <b>Finish setup</b>, which writes only those files. Stop playback and switch Bluetooth
  off first. Pressing [[OCT+]] (CONTINUE) starts without them, with only the INIT sounds and no Bluetooth.</p>
  <h3>If the screen stays black</h3>
  <ul class="plain">
    <li><b>Three short key-light flashes</b> mean the FM-1 is in its MIDI update loader. Reconnect and press Install
    again.</li>
    <li>To force that rescue, hold [[OCT-]] <b>alone</b> while switching on. Holding [[OCT-]] and [[OCT+]] together is
    calibration, not rescue.</li>
    <li>One long flash, or a unit the computer sees as <b>UBOOT</b>, needs the <b>fm1-recover</b> tool from the release
    downloads. Follow RECOVERY.md in its archive carefully.</li>
  </ul>
  <h3>Leaving Melodee later</h3>
  <p>Use <b>Back up and install TransitFM1</b> in Melodee's installer, then the next firmware's own installer once
  the FM-1 shows <b>TRANSIT</b>. The installer saves a full backup first. For Baud Girl, install official V15 first
  instead. A trip through official firmware doesn't keep your Melodee projects, so keep that backup.</p>
  {box("saved", "Ready", f"Melodee {FW} is installed and your old work is backed up. Time to make some noise.")}
</section>
"""

# ===========================================================================
# LESSON 1
# ===========================================================================
L1 = opener(1, "Hello, Melodee",
    "Before making anything, learn to walk around. In this lesson you'll meet Stage, try a few sounds, and save your very first one.",
    "30 minutes", "Melodee installed", "Your first user sound",
    keys=True, screen="stage") + f"""
  <h3>Stage, your home base</h3>
  <p>Switch on. After the startup screen (which shows the version) you land on <b>Stage</b>, Melodee's home page.
  It shows four rows, one per track. On a fresh FM-1 they hold four starting sounds: <b>It's a Prophet</b>,
  <b>FM6 SOLID BASS</b>, <b>CZ-1 SYNTH.LEAD 1</b> and the <b>808 kit</b>. If someone has already saved a template or a
  boot project, you'll see theirs instead. That's fine.</p>
  {steps(1,
    "Play the keys. You're playing track 1, the Prophet.",
    "Turn [[@ALGORITHM]] to step through the tracks. The screen takes each track's colour, and the keys now play that track. Track 4 is the drum kit: each key is a different drum.",
    "Back on track 1, press [[OCT-]] or [[OCT+]] to shift the keyboard down or up. A badge such as [[~+1]] appears at the top. Press both together to reset.",
    "Turn [[@KNOB 1]], [[@KNOB 2]], [[@KNOB 3]] and [[@KNOB 4]] in turn while you hold a note. The strip at the bottom shows what each knob shapes. On the Prophet they're CUTOFF, RES, ENV and REL.",
    "Tap [[HOME]] while on Stage. This is the <b>chord view</b>: the notes you play light up on a wheel. Tap [[HOME]] again to come back.",
  )}
  <h3>Browsing sounds</h3>
  {steps(6,
    "On track 1, turn [[@PRESETS]]. The sound browser opens. Keep turning [[@PRESETS]] (or [[@KNOB 2]]) to move through sounds. Each one loads when the knob rests.",
    "Turn [[@KNOB 1]] to choose a list: ALL, FAV, RECENT, or a category such as BASS, LEAD or PAD. [[@KNOB 3]] marks the current sound as a favourite.",
    "Found one you like? Press [[OCT+]] to keep it. Changed your mind? [[OCT-]] puts back the sound you had. Holding [[EDIT]] also returns to the sound you had before browsing.",
  )}
  {box("why", "Sounds and patterns are separate", "Loading a sound never changes the notes a track plays. Later, when your tracks have patterns, you can swap sounds freely without losing a note.")}
  <h3>Save your first sound</h3>
  {steps(9,
    "Pick any Prophet sound on track 1 and make it your own: turn [[@KNOB 1]] (CUTOFF) and [[@KNOB 4]] (REL) on Stage until you like it.",
    "Make sure nothing is playing, then tap [[SAVE]]. The USER page opens, showing the 384 shared user slots (U001 to U384).",
    "Turn [[@KNOB 1]] or [[@KNOB 2]] to an empty slot. Press [[OCT+]]: the slot's sheet opens on <b>Save here</b>. Press [[OCT+]] again.",
    "The NAME screen appears. Type with the white keys like an old phone keypad: press a key again quickly to step A, B, C. [[@KNOB 1]] moves the cursor. The black keys switch to ←, SPACE, →, DEL and 123. Press [[OCT+]] to save.",
    "Turn [[@PRESETS]] and find your sound. User sounds are listed after their engine's factory sounds.",
  )}
  {box("why", "Can't hear anything?", "Work through the short checklist in <a class='pref' href='#silent'>If something goes wrong</a> on page <a class='pnum' href='#silent'></a>.")}
  {box("try", "Try this", "Hold [[HOME]] to open the settings menu. [[@KNOB 2]] moves down the list and [[@KNOB 1]] changes a setting. Try <b>COLOR</b> for a different theme, then press [[OCT-]] to leave. Every page in this book works the same in any colour.")}
  {box("saved", "Saved today", "Your first user sound, in the shared bank. You know Stage, the browser, and the five moves.")}
</section>
"""

# ===========================================================================
# LESSON 2
# ===========================================================================
def eng_card(name, color, dark, what, listen, knobs, tryit):
    tc = "#14111C" if dark else "#fff"
    return f"""
  <div class="eng">
    <div class="eng-h" style="background:{color};color:{tc}">{name}</div>
    <div class="eng-b">
      <p>{what}</p>
      <p><b>Stage knobs:</b> {knobs}</p>
      <p><b>Listen for:</b> {listen}</p>
      <p class="engtry"><b>Try:</b> {tryit}</p>
    </div>
  </div>"""


L2 = opener(2, "Five instruments in one box",
    "Each of Melodee's engines makes sound in a different way. This lesson is a listening tour: no deep editing, just ears, a few presets and a few knob turns.",
    "40 minutes", "Lesson 1", "One favourite from each engine",
    keys=True, screen="browser") + f"""
  <p>The four starting tracks already cover four of the five engines: track 1 is a Prophet, track 2 is FM6, track 3 is
  CZ-1 and track 4 is a drum kit. You'll borrow track 3 to visit the SID chip at the end.</p>
  {fig(F.engine_strip(), "Each engine has its own colour in this book. Look for it on the cheat sheets at the back.")}
  {steps(1,
    "Turn [[@ALGORITHM]] to the track for the engine you're visiting.",
    "Turn [[@PRESETS]] to browse that engine's sounds. Play a few on the keys. Keep any you like with [[OCT+]].",
    "When you find a favourite, turn [[@KNOB 3]] in the browser to mark it <b>FAV</b>. Favourites survive power-off.",
    "Back on Stage, turn the four sound knobs and listen to what changes.",
  )}
  {eng_card("PROPHET · track 1", F.ENGINE["PROPHET"], False,
    "Modelled on the Sequential Prophet-5, the polysynth behind countless 80s records. Two oscillators feed a warm four-pole filter. Melodee includes Sequential's own 200 factory programs.",
    "how the sound opens up and closes down as you turn CUTOFF. That sweep is the Prophet's signature.",
    "CUTOFF · RES · ENV · REL", "turn [[@KNOB 1]] (CUTOFF) slowly while holding a chord.")}
  {eng_card("FM6 · track 2", F.ENGINE["FM6"], True,
    "Six-operator FM synthesis, compatible with the Yamaha DX7. In FM, one oscillator wobbles another's pitch very fast, which creates new, often bell-like tones. Great for electric pianos, bells, glassy pads and punchy basses.",
    "the clear, metallic, glassy character. FM is bright in a different way from the Prophet.",
    "MLVL · MRAT · MEG · DTUN", "[[@KNOB 1]] (MLVL) changes how hard the modulator pushes, so how bright the tone is. [[@KNOB 2]] (MRAT) changes the modulator's ratio, which can turn a tone into a bell.")}
  {eng_card("CZ-1 · track 3", F.ENGINE["CZ-1"], True,
    "Casio's phase distortion synth from the mid 80s, with all 64 of Casio's factory tones. Instead of filtering a wave, it bends the shape of the wave itself.",
    "a slightly digital, buzzy brightness that softens beautifully.",
    "WAVE · DCW · DETUNE · VIBRATO", "[[@KNOB 2]] (DCW) is how far the wave is bent: low is soft and round, high is bright.")}
  {eng_card("DRUM · track 4", F.ENGINE["DRUM"], False,
    "Synthesised drum machines: the TR-808 and TR-909, a CR-78 style rhythm box, a SID chip kit and two-operator FM drums. On a drum track each key plays a different drum.",
    "the 808's deep, boomy kick against the 909's punchier one.",
    "TUNE · TONE · DECY · SNAP", "turn [[@PRESETS]] on track 4 to swap between the kits.")}
  <h3>Visiting the SID chip</h3>
  {steps(5,
    "Turn [[@ALGORITHM]] to track 3 and turn [[@PRESETS]] to open the browser. Turn [[@KNOB 4]] (ENGINE) until it reads <b>INIT SID</b>. Track 3 is now a SID.",
    "Turn [[@KNOB 2]] to explore the 32 SID factory sounds. Mark your favourite with [[@KNOB 3]], then press [[OCT+]].",
  )}
  {eng_card("SID", F.ENGINE["SID"], False,
    "The sound chip from the Commodore 64, modelled from real 6581 and 8580 chips. It's the simplest engine on the FM-1, so it's quick to dial in a sound.",
    "the gritty, unmistakable sound of 80s computer game music.",
    "WAVE · PW · CUT · RES", "[[@KNOB 2]] (PW, pulse width) on a pulse wave: it changes from hollow to thin and nasal.")}
  {box("try", "Try this", "Turn [[@PRESETS]] and set [[@KNOB 1]] to <b>FAV</b>. Your five favourites are now in one short list, one from each engine.")}
  {box("why", "Don't worry about these tracks", "Lesson 3 starts a fresh project with the four starting sounds, so nothing you changed today will get in the way. Your favourites and user sounds stay.")}
  {box("saved", "Saved today", "Five favourites, one per engine, in the FAV list.")}
</section>
"""

# ===========================================================================
# LESSON 3
# ===========================================================================
L3 = opener(3, "Playing without wrong notes",
    "Today you start the project you'll keep building until the end of the book. You'll choose its key, switch on Melodee's safety rails, and set up an arpeggiator that plays for you.",
    "40 minutes", "Lessons 1 and 2", "Your book project, with a scale and an arp",
    keys=True, screen="scales") + f"""
  <h3>Start a new song</h3>
  {steps(1,
    "Make sure nothing is playing. Tap [[SAVE]] twice: the first tap opens USER (sounds), the second opens <b>PROJECT</b>.",
    "Turn [[@KNOB 1]] right, past the slots 01 to 32 and past <b>T</b> (the template), to <b>+</b> (New song). Press [[OCT+]].",
    "The KEY screen: set [[@KNOB 1]] ROOT to <b>A</b>, [[@KNOB 2]] SCALE to <b>Natural minor</b> (shown as MIN) and [[@KNOB 3]] TEMPO to <b>90</b>. Press [[OCT+]].",
    "The ROLES screen gives each of the four tracks a role. Leave all four on <b>KEEP</b> and press [[OCT+]]. Stage shows the four starting sounds again, with empty patterns.",
    "Hold [[SAVE]]. The screen says [[~NEW PROJECT: PICK SLOT]] with a free slot chosen. Press [[OCT+]], type a name such as GENTLY, and press [[OCT+]] to save.",
  )}
  {box("why", "Why KEEP?", "With no template saved, KEEP gives you the power-on sounds: Prophet, FM6 bass, CZ-1 lead and the 808. The rest of the book assumes those four. If you've saved a template, its sounds appear instead. In that case, go back and choose roles, or set the sounds by hand later.")}
  {box("why", "Autosave", "From now on, when the project is stopped and untouched for five seconds, Melodee saves it to its slot by itself. Holding [[SAVE]] still saves straight away. You can switch AUTOSAVE off in the [[HOME]] hold menu.")}
  <h3>Safety rails</h3>
  {fig(F.scale_fig())}
  {steps(6,
    "Press [[SCL]]. The SCALES page shows your scale on [[@KNOB 2]] and ROOT on [[@KNOB 3]]. Check they read MIN (Natural minor) and A.",
    "Turn [[@KNOB 4]] (QNT) to <b>SNAP</b>. Now every key you press stays inside your chosen scale, black keys too. Play freely. Some notes feel more settled than others, and that pull is part of what makes music interesting.",
  )}
  {box("why", "Why it works", "A scale is a set of notes that sound good together. A natural minor uses A, B, C, D, E, F and G, which happen to be the white keys. With SNAP, a black key drops to the scale note just below it. ROOT, scale and QNT belong to the whole project, so every track follows them.")}
  <h3>Let the arpeggiator play</h3>
  {fig(F.arp_fig(), "An arpeggiator plays the notes you hold one at a time, over and over.")}
  {steps(8,
    "Turn [[@ALGORITHM]] to track 3 (the CZ-1 lead).",
    "Press [[ARP]] (until the ARP page, if you've been here before). Set [[@KNOB 1]] MODE to <b>UP</b>, [[@KNOB 2]] RATE to <b>1/16</b>, [[@KNOB 3]] OCT to <b>2</b>, and [[@KNOB 4]] GATE to about halfway.",
    "Hold three keys together: the 3rd, 5th and 7th white keys from the left (A, C and E). Melodee plays them in turn, up through two octaves.",
    "Press [[ARP]] again for <b>ARP 2</b>. Turn [[@KNOB 3]] HOLD on: the arp keeps going after you let go. Play a different three keys to change it. Turn HOLD off again when you're done.",
    "Leave the arpeggiator on (MODE UP) for track 3. You'll use it in Lesson 8. Hold [[SAVE]] to save.",
  )}
  {box("try", "Try this", "On the ARP page, try MODE <b>UPDN</b> (up then down) or <b>RND</b> (random). On ARP 2, lower PROB so some notes skip at random.")}
  {box("saved", "Saved today", "Your book project, in A natural minor at 90 BPM, with SNAP on and an arpeggiator ready on track 3.")}
</section>
"""

# ===========================================================================
# LESSON 4
# ===========================================================================
L4 = opener(4, "Chords do the heavy lifting",
    "You don't need to know a single chord shape. Press one key, and Melodee builds the chord for you, in tune with the scale you chose in Lesson 3.",
    "30 to 40 minutes", "Your project from Lesson 3", "A pad sound and a chord progression",
    keys=True, screen="chord") + f"""
  <h3>A soft pad</h3>
  {steps(1,
    "Turn [[@ALGORITHM]] to track 1 (the Prophet) and turn [[@PRESETS]] to open the browser.",
    "Turn [[@KNOB 1]] to the <b>PAD</b> list, then turn [[@KNOB 2]] and audition a few. Choose a soft, slow pad and press [[OCT+]].",
    "Check it's still a Prophet sound: back on Stage, the knob strip reads CUTOFF, RES, ENV and REL. Lesson 6 relies on that.",
  )}
  <h3>Build your first chord</h3>
  {fig(F.one_key_chord())}
  {steps(4,
    "Press [[SCL]] until you reach the <b>CHORD</b> page. Its pages go SCALES, then the SCL settings list, then CHORD, and [[SCL]] remembers where you last were. CHORD puts its settings straight on the four knobs.",
    "Turn [[@KNOB 1]] (CHRD) to [[~MIN]]. Every key now plays a minor chord. Play up the white keys and listen: some chords sound a little out of place.",
    "Now turn [[@KNOB 1]] on to [[~AUTO]]. Each key still gives the chord's root, but Melodee picks a chord that stays inside your scale, so the chords sit comfortably together. The CHORD page names each chord as you play it.",
    "Turn [[@KNOB 2]] (VOIC) from [[~CLOSE]] to [[~OPEN]]. Same notes, spread wider: bigger and softer.",
    "Set [[@KNOB 3]] (STRUM) to [[~1/32]] and [[@KNOB 4]] (STROKE) to [[~DOWN]]. Each chord now ripples up from the bottom like a gentle harp. Set STRUM back to OFF if you prefer a solid chord. Your screen may label STROKE as DIR.",
  )}
  {fig(F.voicing_fig(), "Voicing changes how a chord's notes are stacked, not which notes they are.")}
  {box("why", "Why it works", "A chord is three or more notes played together. In A natural minor, some chords on each root fit the scale and some don't. MIN forces a minor chord everywhere, so a few land outside the scale. AUTO looks at the scale (and at what your other tracks are playing) and picks one that fits. With CLOSE voicing it even chooses nearby inversions so the chords flow smoothly into each other.")}
  <h3>Find a progression</h3>
  <p>A <b>chord progression</b> is a short list of chords played one after another. Here's a classic one that suits
  A minor. Press each key for a slow count of four.</p>
  {fig(F._svg(552, 130, F.keyboard(lit={0, 1, 2, 4}, labels={2: "1", 0: "2", 4: "3", 1: "4"}, x0=16, y0=10, w=520, h=96)), "Press A, then F, then C, then G: the 3rd, 1st, 5th and 2nd white keys from the left.")}
  {steps(9,
    "Play A, F, C, G slowly, round and round, until it feels like a little journey. Swap in other keys if you like: AUTO keeps every one in the scale. Remember your four keys. You'll record them in Lesson 5.",
    "Hold [[SAVE]] to save. The chord settings are saved with track 1.",
  )}
  {box("try", "Try this", "Switch CHRD to [[~AUTO2]] and play a slow tune with one finger. The key you press is always the top note, with harmony filled in underneath. Instant piano player. Switch back to AUTO before Lesson 5.")}
  {box("try", "Quick layer", "Hold [[SCL]] from any page: the keys set the ROOT, and the knobs set root, scale, chord and voicing. Let go to return. Double-press [[SCL]] to lock the layer open; press it again to close it.")}
  {box("saved", "Saved today", "A Prophet pad on track 1 with AUTO chords, and a four-chord progression in your fingers.")}
</section>
"""

# ===========================================================================
# LESSON 5
# ===========================================================================
L5 = opener(5, "Your first patterns",
    "A pattern is one looping phrase on one track. Today you'll make three of them, each a different way: drums step by step, chords by Capture, and a bassline recorded live.",
    "45 to 60 minutes (two sittings is fine)", "Your project and your four chords", "Drums, chords and bass, playing together",
    keys=True, screen="grid") + f"""
  <p>Press [[SEQ]] and keep pressing it to see the sequencer's pages: <b>NOTES</b> (the notes themselves),
  <b>PATTERN</b> (this track's loop length and speed), <b>TEMPO</b> (the whole song's speed), <b>PATTERNS</b> (every
  track's patterns) and <b>SONG</b>. [[@SELECT]] turns through them both ways.</p>
  <h3>Part 1: drums, step by step</h3>
  {fig(F.drum_grid_fig())}
  {steps(1,
    "Turn [[@ALGORITHM]] to track 4 (the 808). Press [[SEQ]] until you reach <b>NOTES</b>. On a drum track it's a grid: eight lanes down, 16 steps across.",
    "Press the <b>1st black key</b> to choose the KICK lane (you'll hear it). Then press white keys <b>1, 5, 9 and 13</b>. Each press puts a kick on that step.",
    "Press the <b>2nd black key</b> for SNARE, then white keys <b>5 and 13</b>.",
    "Press the <b>4th black key</b> for HATCL (closed hi-hat), then every other white key: <b>1, 3, 5, 7, 9, 11, 13 and 15</b>.",
    "Press [[PLAY]]. There's your beat. Press [[PLAY]] again to stop. A wrong step? Choose its lane and press the white key again to remove it.",
  )}
  {box("why", "The eight lanes", "The first eight black keys pick the lanes: KICK, SNARE, CLAP, HATCL, HATOP, TOM, RIM and BELL. Hold the 9th black key while you press a white key to add an accent. The last two black keys page through longer patterns. A pattern starts at 16 steps of 1/16, which is one bar.")}
  {box("try", "Try this", "Turn [[@PRESETS]] on track 4 and try the 909, CR78 and FM kits. Your pattern stays exactly the same; only the drum sounds change.")}
  <h3>Part 2: chords, by Capture</h3>
  <p>Capture is Melodee's kindest feature. While the music runs, it quietly listens to the track you've selected. When
  you've played something you like, hold [[REC]] and it writes what you just played into the pattern. Nothing is kept
  until you hold [[REC]], so you can rehearse as long as you like.</p>
  {fig(F.capture_fig())}
  <h3>First, a rehearsal</h3>
  {steps(6,
    "Tap [[HOME]] for Stage and turn [[@ALGORITHM]] to track 1, your pad. Choose the track before you start: Capture only listens to the selected track, and switching tracks clears what it heard.",
    "Press [[PLAY]]. Count out loud with the kick drum: <b>one, two, three, four</b>, one count per kick. Each group of four counts is one bar.",
    "Play chord 1 on <b>one</b> and hold it for the whole bar. On the next <b>one</b>, change to chord 2. Then chords 3 and 4, one per bar. Go round a few times until the changes feel easy. Mistakes don't matter yet.",
  )}
  <h3>The take</h3>
  {steps(9,
    "When you're ready, play the four chords once more, one per bar. When the next <b>one</b> arrives, <b>don't</b> play chord 1. Instead, hold [[REC]] for about a second, until the screen says [[~CAPTURED 4 BARS]]. Hold it any time in that bar, the sooner the better, but always before you play another note.",
    "Listen. Track 1's row on Stage now shows notes, and the pad plays your four chords in order, starting with chord 1, going round every four bars with the drums. Press [[PLAY]] to stop.",
    "To tidy the timing, go to [[SEQ]] NOTES with the music stopped. <b>Hold [[OCT+]]</b> for the pattern tools and choose <b>Quantize</b>.",
    "Turn [[@KNOB 1]] to <b>1</b> (one step) and press [[OCT+]]. Every note now sits on the nearest step.",
  )}
  {box("why", "Not quite right? Undo and go again", "Hold [[EDIT]] straight away to undo the capture, then start again from the rehearsal. Always undo first: capturing again over notes adds the new chords on top of the old ones.<br/><br/><b>It says 1 BAR or 2 BARS, or the loop starts on chord 2?</b> You probably held [[REC]] a bar late, or after playing chord 1 again. A first chord played just before the beat can also be missed, so aim for the beat or a touch after.<br/><b>It says RECORDING?</b> A track is armed: tap [[REC]] to disarm it, then try again. A quick tap of [[REC]] arms recording, so hold it rather than tapping.<br/><b>It says NOTHING TO CAPTURE?</b> Check track 1 is selected, and that you didn't switch tracks after playing.")}
  {box("why", "How Capture decides", "Capture looks back over the last four bars. If you haven't played anything in the current bar, the take ends where that bar began; if you have, it ends at the end of the current bar. On an empty pattern it keeps 1, 2 or 4 bars, whichever fits what you played, and sets the pattern's length to match. That's why holding [[REC]] on the empty <b>one</b> gives you exactly bars 1 to 4.")}
  {box("try", "Need a click?", "Hold [[HOME]], turn [[@KNOB 2]] to AUDIO CLICK and [[@KNOB 1]] to ON. CLICK LEVEL sets its volume. Press [[OCT-]] to leave.")}
  <h3>Part 3: bass, recorded live</h3>
  {steps(13,
    "Turn [[@ALGORITHM]] to track 2 (FM6 SOLID BASS). Press [[SEQ]] until <b>PATTERN</b> and turn [[@KNOB 1]] LEN to <b>64</b>, so the bass loop is as long as your chords.",
    "Press [[SEQ]] until <b>TEMPO</b> and turn [[@KNOB 3]] QNT to <b>1/16</b>. Recordings will now snap to the nearest step when they finish.",
    "Tap [[HOME]] for Stage and press [[OCT-]] once or twice so the bass sits low.",
    "Hold [[REC]] and press [[PLAY]] straight away: recording starts from the top. Play the same four keys as your chords, one long note per bar, starting on the first kick of each bar.",
    "After the fourth bar, press [[PLAY]] to stop, which finishes the take. Tap [[REC]] to disarm. Listen back. Hold [[EDIT]] to undo it if you want another go.",
    "Hold [[SAVE]].",
  )}
  {box("why", "Different lengths, one groove", "Each track can have its own pattern length. Your drums loop every bar, while the chords and bass loop every four bars. The drums simply go round four times. That's how small loops build big music.")}
  {box("saved", "Saved today", "A drum beat, a four-bar chord pattern and a bassline, all looping together.")}
</section>
"""

# ===========================================================================
# LESSON 6
# ===========================================================================
L6 = opener(6, "Making it move",
    "Real music breathes. Today you'll make your pad swell in, let an LFO slowly sweep its tone, and record a knob move that plays back every loop.",
    "40 minutes", "Your project from Lesson 5", "A pad that swells, sways and sweeps",
    screen="ampenv") + f"""
  <h3>Part 1: a slow swell</h3>
  {steps(1,
    "Turn [[@ALGORITHM]] to track 1 (the pad) and press [[ENV]]. On a Prophet, [[ENV]] opens the Prophet's own envelope pages: FLT ENV, AMP ENV and ENV MOD. Press [[ENV]] until you reach <b>AMP ENV</b>.",
    "Turn [[@KNOB 1]] (ATK, attack) up. Now each chord fades in slowly instead of starting at once.",
    "Turn [[@KNOB 4]] (REL, release) up too, so each chord fades out gently after it ends. Press [[PLAY]] to hear it with the pattern, then stop.",
  )}
  {box("why", "Envelopes", "An envelope shapes a sound over the life of a note: Attack (how quickly it arrives), Decay (how quickly it settles), Sustain (the level it holds) and Release (how long it fades after you let go). The Prophet has two: FLT ENV shapes the brightness, AMP ENV shapes the volume.")}
  <h3>Part 2: let an LFO sway it</h3>
  {fig(F.lfo_fig())}
  {steps(4,
    "Still on track 1, press [[LFO]] until you reach the Prophet's own <b>LFO</b> page (it comes before the shared LFO pages). Turn [[@KNOB 1]] RATE low for a slow sway, and turn [[@KNOB 3]] TRI on.",
    "Press [[LFO]] again for <b>WHEEL</b>. Turn [[@KNOB 1]] INITIAL up a little. This is how much the LFO is applied all the time.",
    "Press [[LFO]] again for <b>WHEEL 2</b> and turn [[@KNOB 3]] FILTER on. Play a chord: the brightness now rises and falls by itself. Too much? Lower INITIAL.",
  )}
  <h3>Part 3: record a knob move</h3>
  {fig(F.motion_fig())}
  {steps(7,
    "Stop the music and tap [[HOME]] for Stage. With track 1 selected, tap [[REC]] to arm it.",
    "Press [[PLAY]]. Over the four bars, slowly turn [[@KNOB 1]] (CUTOFF) down and back up again. Don't play any keys.",
    "At the end of the fourth bar, press [[PLAY]] to stop, then tap [[REC]] to disarm.",
    "Press [[PLAY]]. Your knob move plays back every loop. A <b>MOTION</b> page now appears in the [[SEQ]] pages, with one lane for each control you moved.",
    "Not right? Hold [[EDIT]] to undo the take, and go again.",
  )}
  {box("warn", "Keep it light", "A project shares a pool of 64 motion events across all its patterns. If the screen says MOTION FULL, the pool is used up. One or two gentle moves per project is plenty for now.")}
  {box("try", "Hands-free tweaks", "Hold [[LFO]] while turning any sound knob. The change lasts only while you hold it, then springs back, which is perfect for live tweaks. Press [[OCT+]] while still holding [[LFO]] to keep the change.")}
  {box("try", "Vibrato on the lead", "Select track 3 and press [[LFO]] for CZ VIBRATO. Turn [[@KNOB 3]] DEPTH up a little (it's silent at 0), [[@KNOB 2]] for RATE, and [[@KNOB 4]] DELAY so the wobble fades in after each note starts.")}
  {steps(12,
    "Hold [[SAVE]].",
  )}
  {box("saved", "Saved today", "Your pad now fades in, sways with an LFO, and sweeps once every loop.")}
</section>
"""

# ===========================================================================
# LESSON 7
# ===========================================================================
L7 = opener(7, "Space and polish",
    "A little space and a balanced mix turn loops into music. Today you'll add a shared reverb, an echo on the lead, and set the levels.",
    "40 minutes", "Your project from Lesson 6", "A mixed loop with reverb and echo",
    screen="reverb") + f"""
  {fig(F.fx_flow_fig(), "Each track has its own note effects, then sends some of its sound to one shared effects rack.")}
  <h3>Part 1: a shared reverb</h3>
  {steps(1,
    "Turn [[@ALGORITHM]] to track 1 and press [[FX]]. The track's rack opens: three note-effect slots, then a <b>Shared</b> row. Turn [[@KNOB 2]] down to the Shared row.",
    "Turn [[@KNOB 4]] (SEND) to about 40%. That's how much of the pad goes to the shared effects.",
    "Press [[OCT+]] on the Shared row to open the <b>SHARED</b> rack. Turn [[@KNOB 2]] to slot <b>A</b> and press [[OCT+]]. The effect browser opens.",
    "Turn [[@KNOB 1]] to the <b>Space</b> family and [[@KNOB 2]] to <b>REVERB</b>. Press [[OCT+]] to confirm.",
    "On the reverb's page, [[@KNOB 2]] is SIZE, [[@KNOB 3]] is DAMP and [[@KNOB 4]] is TONE. Play with SIZE while the loop runs. Leave [[@KNOB 1]] (MIX) where it is.",
    "Press [[OCT-]] to step back out: to SHARED, to the rack, then to Stage.",
    "Turn [[@ALGORITHM]] to track 3 (the lead), press [[FX]], turn [[@KNOB 2]] to the Shared row and turn [[@KNOB 4]] SEND up a little too. It shares the same reverb. Play a few keys to hear it: the lead has no pattern yet.",
  )}
  {box("why", "Why shared?", "Every track sends to one shared rack of three slots (A, B and C, in a chain). It's like all your instruments playing in the same room. Only one reverb can run at a time, so sharing it is both kinder to the FM-1 and better sounding.")}
  <h3>Part 2: an echo on the lead</h3>
  {box("why", "The lead plays by hand, for now", "Track 3 has no pattern yet. You'll record its part in Lesson 8. Until then it only sounds when you play it, so play a few notes on the keys while you set the echo. The arp from Lesson 3 is still on: hold a key or two and the echo follows every note. Once the lead has its own pattern in Lesson 8, it will loop with the others.")}
  {steps(8,
    "On track 3, press [[FX]]. Turn [[@KNOB 2]] to the first slot and [[@KNOB 1]] to <b>NOTE ECHO</b>. [[@KNOB 4]] sets its LEVEL (how loud the repeats start).",
    "Press [[OCT+]] to open the slot. Play a few notes as you set TIME to a tempo division such as 1/8, and DECAY to how quickly the repeats fade.",
    "Press [[OCT-]] until you're back on Stage.",
  )}
  <h3>Part 3: balance the mix</h3>
  {steps(11,
    "Press [[GLO]] for the MIXER. [[@KNOB 1]] is LEVEL and [[@KNOB 2]] is PAN for the selected track. Turn [[@ALGORITHM]] to move between tracks.",
    "With the loop playing, start with the drums and bass, then bring the pad in underneath. For the lead, play along by hand while you set its level, and pan it a little to one side if you like. You can fine-tune it in Lesson 8 once it loops.",
    "For quick changes, hold [[GLO]] from any page: the knobs become track levels and the keys mute and solo tracks. Let go to return.",
    "Press [[HOME]] when you're happy.",
    "Hold [[SAVE]].",
  )}
  {box("try", "Punch effects", "Hold [[FX]] and press a key. One of 27 effects hits the whole mix: tape stop, reverse, filter sweeps, stutters and more. Let go of the key and it's gone. These keys play no notes. Turn [[@KNOB 1]] while holding [[FX]] to see which key does what.")}
  {box("saved", "Saved today", "A mixed loop with a shared reverb, an echo on the lead, and balanced levels.")}
</section>
"""

# ===========================================================================
# LESSON 8
# ===========================================================================
L8 = opener(8, "Your first song",
    "Time to turn your loop into a song. You'll make a busier drum pattern and a lead part, then arrange them into an intro, a middle and an ending.",
    "Two sittings of 30 to 40 minutes", "Everything from Lessons 3 to 7", "A finished short song",
    keys=True, screen="song") + f"""
  <h3>Part 1: a busier drum pattern</h3>
  <p>Each track has 16 pattern slots. On the PATTERNS page the 16 white keys choose them: the first white key is pattern 1,
  the second is pattern 2, and so on.</p>
  {steps(1,
    "Stop the music. Turn [[@ALGORITHM]] to track 4 and press [[SEQ]] until <b>PATTERNS</b>.",
    "<b>Hold the 1st white key</b> for about a second. A dialog opens. Press the <b>2nd white key</b>: pattern 1 is copied to pattern 2.",
    "Tap the 2nd white key to select pattern 2.",
    "Turn [[@SELECT]] back to <b>NOTES</b>. The drum grid shows pattern 2. Press the 3rd black key (CLAP) and add claps on white keys <b>5 and 13</b>. Press the 5th black key (HATOP) and add an open hi-hat on white key <b>15</b>.",
    "Press [[PLAY]] to hear it, then stop.",
  )}
  <h3>Part 2: a lead part</h3>
  {steps(6,
    "Turn [[@ALGORITHM]] to track 3 (the CZ-1 lead, with the arp from Lesson 3). Press [[SCL]] until the CHORD page and set [[@KNOB 1]] CHRD to <b>AUTO</b>. Now one key gives the arp a whole chord.",
    "Press [[SEQ]] until <b>PATTERN</b> and set [[@KNOB 1]] LEN to <b>64</b>.",
    "Hold [[REC]] and press [[PLAY]] straight away. Hold each of your four keys for one whole bar: A, F, C, G. The arp plays, and the notes it plays are what gets recorded.",
    "After the fourth bar, press [[PLAY]] to stop and tap [[REC]] to disarm. Listen. Hold [[EDIT]] to undo and try again if you like.",
  )}
  {box("why", "What gets recorded", "With the arp on, Melodee records the notes the arp plays, not the keys you held. What plays back is exactly what you heard.")}
  <h3>Part 3: arrange the song</h3>
  {fig(F.song_grid_fig(), "The plan. Each section lasts one loop of track 1, which is four bars.")}
  <p>On the SONG page, [[@KNOB 1]] picks a section, [[@KNOB 2]] a track, [[@KNOB 3]] that track's pattern (turn it below
  P1 for <b>REST</b>), and [[@KNOB 4]] stretches a block over the following sections. Edits happen while stopped.</p>
  {steps(10,
    "Stop the music and press [[SEQ]] until <b>SONG</b>. It's empty.",
    "<b>Intro.</b> On an empty song the cursor sits on the empty column. Press [[OCT+]]: a new section full of rests appears. Turn [[@KNOB 2]] to track 1 and [[@KNOB 3]] to <b>P1</b>. The intro is just the pad.",
    "<b>Section A.</b> Turn [[@KNOB 1]] right, past the last section, to the empty column at the end, and press [[OCT+]] to add a section there. Select it with [[@KNOB 1]] and set tracks 1, 2 and 4 to <b>P1</b> with [[@KNOB 2]] and [[@KNOB 3]]. Leave track 3 resting.",
    "<b>Section B.</b> With section A selected, <b>hold [[OCT+]]</b> and choose <b>Duplicate section</b>. The copy goes right after it. Turn [[@KNOB 1]] to the copy and set track 4 to <b>P2</b> and track 3 to <b>P1</b>. Then duplicate this B section once more.",
    "<b>A again.</b> Go to the end column, press [[OCT+]] to add a section, select it, and set tracks 1, 2 and 4 to P1.",
    "<b>The ending.</b> Add one more section at the end the same way, with only tracks 1 and 2 on P1. The drums and lead rest.",
    "Turn [[@KNOB 1]] to section 1 and press [[PLAY]]. The song plays from the selected section and stops at the end. The ruler shows minutes and seconds.",
  )}
  <h3>Part 4: a finishing touch</h3>
  {steps(17,
    "Turn [[@KNOB 1]] to the last section and tap [[FX]]. The punch editor opens with four lanes.",
    "Turn [[@KNOB 1]] to choose an effect: a tape stop or a slow filter sweep suits an ending. [[@KNOB 3]] sets START and [[@KNOB 4]] END, in steps. For the last bar of a 64-step section, set START to <b>49</b> and END to <b>64</b>.",
    "Press [[PLAY]] to audition it, then stop and press [[OCT-]] to go back to SONG.",
    "Play the whole song from section 1. Then hold [[SAVE]]. Well done: that's a song.",
  )}
  {box("try", "A different sound for one section", "Select a block (a section and track), press [[OCT+]] and choose <b>Set preset</b>. Browse as usual and press [[OCT+]] to give just that block its own sound, such as a brighter lead in the second B. Remove preset puts it back.")}
  {box("try", "Jam it instead", "With no song playing, Melodee logs every loop of track 1 as you switch patterns live on the PATTERNS page ([[@KNOB 1]] to [[@KNOB 4]] queue each track's next pattern). Go to SONG and hold [[REC]] (Take jam) to turn that jam into an arrangement.")}
  {box("try", "Loop song", "Press [[OCT+]] on SONG and switch on <b>Loop song</b> to have the song go back to the start forever. Lovely for background listening.")}
  {box("saved", "Saved today", "A finished song, about a minute long, with an intro, a middle, a busier section and an ending. Your first.")}
</section>
"""

# ===========================================================================
# MPC
# ===========================================================================
MPC = f"""
<section class="lesson" id="mpc">
  <div class="run">Optional · Into the MPC</div>
  <div class="kicker">Optional</div>
  <h2>Into the MPC</h2>
  <p class="lede">If you have an Akai MPC Sample, your Melodee parts make great raw material. This chapter is a short
  bridge to <em>MPC, Gently</em>.</p>
  {fig(F.mpc_fig())}
  <h3>The reliable way: record the audio</h3>
  <p>The simplest path is to record what you hear. Connect the FM-1's audio output to your MPC Sample's audio input
  with a suitable cable, and sample each part the way <em>MPC, Gently</em> shows you.</p>
  {steps(1,
    "On the FM-1, use the GLO mixer to <b>solo</b> the part you want (hold [[GLO]]; the keys mute and solo).",
    "Start the song or pattern with [[PLAY]], and record a few loops into the MPC.",
    "Repeat for each part: pad, bass, lead, drums. Back on the MPC, chop, pitch and rearrange them.",
  )}
  {box("try", "Clean stems by USB", "Connected to a computer, Melodee is a USB audio device. Hold [[HOME]] and set USB INPUT to <b>4 TRACKS</b> to record four separate stems, one per track, in your computer's audio app.")}
  <h3>Going further, by USB</h3>
  <p>Melodee can also host USB MIDI gear from its own USB-C port. Melodee's notes list the MPC Sample as tested with
  this. The FM-1 supplies no USB power, so the MPC must be powered by itself.</p>
  {box("try", "Play Melodee from the MPC's pads", "Hold [[HOME]] and set USB HOST to ON (it's off again at every power-on). Press [[SCL]] and set QNT to <b>MPC</b>. Turn on the MPC's Pad MIDI Out. Now MPC pad banks E, F, G and H play Melodee tracks 1 to 4, in your scale. Set QNT back to SNAP afterwards, because QNT is shared by the whole project.")}
  {box("warn", "Clock: new and untested", "Melodee 1.6.1 is the first version that sends MIDI clock. With GLO > GLOBAL > CLK on <b>INT</b>, it sends clock, Start and Stop over USB, so gear set to follow external clock can stay in time. Melodee's own notes say this hasn't yet been tried with real gear. Treat it as an experiment, and check your MPC's manual for how to follow incoming clock.")}
</section>
"""

# ===========================================================================
# BACK MATTER
# ===========================================================================
def sheet(n, name, color, dark, lede, flow, knobs, find, where, moves, notes):
    tc = "#14111C" if dark else "#fff"
    sub = "#3A2F58" if dark else "#EDE9FF"
    kt = "".join(f'<td><span class="n">KNOB {i + 1}</span><span class="v">{k}</span></td>' for i, k in enumerate(knobs))
    wl = "".join(f"<li><b>{a}:</b> {b}</li>" for a, b in where)
    mv = "".join(f'<div class="move"><b>{a}</b> {b}</div>' for a, b in moves)
    return f"""
<section class="sheet" {'id="sheets"' if n == 1 else ''}>
  <div class="run">Engine cheat sheets</div>
  <div class="band" style="background:{color}">
    <div class="k" style="color:{sub}">Engine {n} of 5</div>
    <h2 style="color:{tc}">{name}</h2>
    <p style="color:{tc}">{lede}</p>
  </div>
  {fig(flow) if flow else ''}
  <div class="cols">
    <div>
      <h3 style="color:{color if color not in ('#6D5BD0',) else '#A396F2'}">The four Stage knobs</h3>
      <table class="knobs"><tr>{kt}</tr></table>
      <h3>Finding sounds</h3>
      <p>{find}</p>
      <h3>Where things live</h3>
      <p>Press [[EDIT]]. [[@PRESETS]] jumps between sections, [[@SELECT]] turns the pages inside one. Tap [[EDIT]] again for the section map.</p>
      <ul>{wl}</ul>
    </div>
    <div class="moves">
      <h3>Three moves to try</h3>
      {mv}
      <p class="note">{notes}</p>
    </div>
  </div>
</section>"""


SHEETS = "".join([
    sheet(1, "Prophet", F.ENGINE["PROPHET"], False,
          "Warm, round and a little unstable, like the late-70s polysynth it's modelled on. Brass, pads, basses and sync leads.",
          F.prophet_flow(), ["CUTOFF", "RES", "ENV", "REL"],
          "[[@PRESETS]] runs from INIT through Sequential's 200 factory programs, then your own user slots (U001 to U384).",
          [("Oscillators", "OSC A, OSC B, B WAVES"), ("Mixer and filter", "MIXER, FILTER"),
           ("Envelopes", "FLT ENV, AMP ENV, ENV MOD"), ("Movement", "POLYMOD, MOD FLT, LFO, WHEEL, WHEEL 2"),
           ("Voice", "UNISON, BEND, VOICE")],
          [("Dark to bright.", "Hold a chord and turn [[@KNOB 1]] slowly from closed to open. That sweep is the classic Prophet sound."),
           ("Squelchy bass.", "On a bass preset, raise [[@KNOB 2]] a little, then [[@KNOB 3]]. Short notes now go \"bwow\"."),
           ("Huge and wobbly.", "In the Voice section, open UNISON, switch it on, set VOICES (up to 5) and add some DETUNE. One note becomes a wall of sound.")],
          "<b>Bonus:</b> on the MOD FLT page, VINTAGE adds gentle drift, like an old synth that's been loved for decades. On the FILTER page, MODEL switches between the SSI and CURTIS four-pole filters. A Prophet track can play up to eight voices."),
    sheet(2, "FM6", F.ENGINE["FM6"], True,
          "Six-operator FM, compatible with the DX7. Glassy, bell-like and bright: electric pianos, bells, plucks and punchy basses.",
          None, ["MLVL", "MRAT", "MEG", "DTUN"],
          "[[@PRESETS]] runs through FM6's factory voices and INIT VOICE, then your user slots. DX7 librarians can send a 32-voice bank over USB into 32 consecutive user slots.",
          [("Voice", "ALGO (32 algorithms, with a chart), PITCH EG, PITCH LV, FM LFO, FM LFO 2"),
           ("Each operator", "FREQ, OUT, EG RATE, EG LVL, SCALE, CURVE. On operator pages, [[@PRESETS]] picks the operator"),
           ("Controllers", "FM BEND, FM PORTA, FM WH/FT, FM BR/AT")],
          [("Brighter, darker.", "Turn [[@KNOB 1]] (MLVL). More modulation means more overtones, so a brighter, edgier tone."),
           ("Into a bell.", "Turn [[@KNOB 2]] (MRAT) a few steps. Changing the modulator's ratio can turn a soft tone metallic and bell-like."),
           ("A pluck.", "Turn [[@KNOB 3]] (MEG) to change how the modulator's envelope behaves: the brightness at the start of each note, then fading.")],
          "In FM, operators either make sound (carriers) or bend another operator's sound (modulators). The algorithm decides which is which. Don't worry about the theory: turning MLVL and MRAT teaches you more than a diagram can."),
    sheet(3, "CZ-1", F.ENGINE["CZ-1"], True,
          "Casio's phase distortion synth. A digital brightness that softens beautifully: brass, strings, buzzy leads and gentle pads.",
          None, ["WAVE", "DCW", "DETUNE", "VIBRATO"],
          "[[@PRESETS]] runs through Casio's 64 factory tones (A-1 BRASS 1 to H-8 TYPHOON SOUND), then your user slots, which start empty.",
          [("Common", "CZ TOOLS, CZ LINE, CZ DETUNE, CZ VIBRATO, CZ WINDOW"),
           ("Each line", "WAVE, TOUCH, and three eight-step envelopes: PIT (pitch), WAV (brightness) and AMP (volume). [[@PRESETS]] picks the line")],
          [("Soft to bright.", "Turn [[@KNOB 2]] (DCW). It sets how far the wave is bent: low is round, high is bright."),
           ("Thicker.", "Turn [[@KNOB 3]] (DETUNE) for a chorus-like thickness when both lines play."),
           ("Gentle vibrato.", "Turn [[@KNOB 4]] (VIBRATO), or set it up properly on the CZ VIBRATO page, where DEPTH must be above 0.")],
          "A CZ tone is built from one or two <b>lines</b>, each a chain of pitch, wave shaping and volume. The CZ-1's envelopes have eight steps rather than four, which is how its tones move so much. The FM-1's own keys send a fixed velocity, so touch settings matter only over MIDI or from the sequencer."),
    sheet(4, "SID", F.ENGINE["SID"], False,
          "The Commodore 64's sound chip, modelled from real 6581 and 8580 chips. Gritty, characterful and the quickest engine to program.",
          None, ["WAVE", "PW", "CUT", "RES"],
          "[[@PRESETS]] runs through the 32 SID factory presets, then your user slots.",
          [("Chip", "MODEL: 6581 or 8580 per note, or C64 6581 / C64 8580 for one voice per track"),
           ("Sound", "WAVE, STACK, PW"), ("Filter", "CUT, RES, MODE, DRIVE")],
          [("Hollow to nasal.", "On a pulse wave, turn [[@KNOB 2]] (PW, pulse width) and listen to the tone thin out."),
           ("Two oscillators.", "Set STACK to OCT, FIFTH or DETUNE to add a second oscillator."),
           ("Chip arpeggio.", "Set MODEL to a C64 chip and the voice to POLY, then hold a chord: it becomes the fast arpeggio heard in classic game music.")],
          "WAVE includes combined waves (TRI+SAW and so on), measured from real chips. The 6581 and 8580 filters sound noticeably different: the 6581 is grittier."),
    sheet(5, "Drum", F.ENGINE["DRUM"], False,
          "Synthesised drum machines on one track: TR-808, TR-909, a CR-78 style box, a SID chip kit and two-operator FM drums.",
          None, ["TUNE", "TONE", "DECY", "SNAP"],
          "[[@PRESETS]] on a drum track browses the kits: 808, 909, SID, SID DIGI, CR78 and FM.",
          [("Sound (whole kit)", "KIT (with TUNE, TONE, DECY), HIT (SNAP, ACC, KICK, DRV)"),
           ("Drum (one at a time)", "DRUM SOUND and DRUM MIX: black keys pick the lane, white keys the drum"),
           ("Lanes", "LANES and LANES 2: a level for each of the eight lanes")],
          [("Deep and slow.", "Turn [[@KNOB 1]] (TUNE) down and [[@KNOB 3]] (DECY) up for a big, booming kit."),
           ("Softer kick.", "On the HIT page set KICK to ROUND to soften the kick's click, or PUNCH to keep it."),
           ("Crunch.", "On the HIT page raise DRV for drive into a soft clip, with the level kept steady.")],
          "In the sequencer, a drum track's NOTES page is a grid: the white keys are the 16 steps of the page, and the first eight black keys pick KICK, SNARE, CLAP, HATCL, HATOP, TOM, RIM and BELL."),
])

HOLDS = f"""
<section class="back" id="holds">
  <div class="run">Holds, taps and where things live</div>
  <div class="kicker">Reference</div>
  <h2>Holds, taps and where things live</h2>
  <table class="ref">
    <tr><th>Hold this</th><th>To do this</th></tr>
    <tr><td>[[HOME]]</td><td>Open the settings menu (COLOR, AUTOSAVE, AUDIO CLICK, USB and more).</td></tr>
    <tr><td>[[EDIT]]</td><td>Undo. While held, [[OCT-]] undoes further and [[OCT+]] redoes.</td></tr>
    <tr><td>[[SAVE]]</td><td>Save the project to its slot. A new project asks for a slot first.</td></tr>
    <tr><td>[[REC]]</td><td>Capture what you just played on the selected track. On SONG: Take jam.</td></tr>
    <tr><td>[[OCT+]]</td><td>Open the page's sheet of actions (Init sound, Copy to…, Duplicate section…).</td></tr>
    <tr><td>[[SCL]]</td><td>Quick layer: ROOT on the keys; root, scale, chord and voicing on the knobs.</td></tr>
    <tr><td>[[GLO]]</td><td>Quick layer: mute and solo on the keys, levels on the knobs, TAP tempo.</td></tr>
    <tr><td>[[SEQ]]</td><td>White keys pick patterns 1 to 16; black keys pick tracks.</td></tr>
    <tr><td>[[FX]]</td><td>Punch effects on the keys, over the whole mix.</td></tr>
    <tr><td>[[LFO]]</td><td>Temporary knob tweaks that spring back when you let go.</td></tr>
    <tr><td>a pattern key</td><td>On PATTERNS: copy it (press another key), delete it (press it again), halve or double it.</td></tr>
  </table>
  <p class="small">Double-press [[SCL]], [[GLO]] or [[FX]] to lock its layer open. Press it again to close.</p>
  <table class="ref">
    <tr><th>Where is…</th><th>Go here</th></tr>
    <tr><td>Scale, root, QNT</td><td>[[SCL]] SCALES</td></tr>
    <tr><td>Chords, voicing, strum</td><td>[[SCL]] until CHORD</td></tr>
    <tr><td>Arpeggiator</td><td>[[ARP]] (ARP, ARP 2)</td></tr>
    <tr><td>Notes, drum grid</td><td>[[SEQ]] NOTES</td></tr>
    <tr><td>Pattern length and speed</td><td>[[SEQ]] PATTERN (LEN, DIV, SWG, GATE)</td></tr>
    <tr><td>Tempo, swing, recording grid</td><td>[[SEQ]] TEMPO (BPM, SWG, QNT)</td></tr>
    <tr><td>Patterns for every track</td><td>[[SEQ]] PATTERNS</td></tr>
    <tr><td>Song arrangement</td><td>[[SEQ]] SONG</td></tr>
    <tr><td>Recorded knob moves</td><td>[[SEQ]] MOTION (appears once there is some)</td></tr>
    <tr><td>Envelopes</td><td>[[ENV]] (the engine's own pages on Prophet, FM6 and CZ-1)</td></tr>
    <tr><td>LFO and mod matrix</td><td>[[LFO]] (the engine's own LFO first, then LFO, LFO 2, LFO DEST, MOD)</td></tr>
    <tr><td>Effects</td><td>[[FX]] (track rack, then SHARED)</td></tr>
    <tr><td>Mixer, clock, tuning</td><td>[[GLO]] (MIXER, GLOBAL, SYSTEM)</td></tr>
    <tr><td>Save a sound</td><td>Tap [[SAVE]]: USER</td></tr>
    <tr><td>Projects, new song</td><td>Tap [[SAVE]] twice: PROJECT</td></tr>
    <tr><td>Sound designer</td><td>Hold [[HOME]]: SOUND DESIGNER</td></tr>
  </table>
</section>
"""

MIDI = f"""
<section class="back" id="midi">
  <div class="run">MIDI and Bluetooth, briefly</div>
  <div class="kicker">Reference</div>
  <h2>MIDI and Bluetooth, briefly</h2>
  <p class="lede">You don't need any of this to make music on the FM-1. It's here for when you're curious.</p>
  <h3>Eight tracks, not four</h3>
  <p>Tracks 1 to 4 can use any engine. Tracks 5 to 8 are <b>MIDI tracks</b>: they make no sound themselves, but play
  external gear over USB or Bluetooth, with the same scales, chords, arps, patterns and songs. Add one from Stage: hold
  [[OCT+]] and choose <b>Add track</b>. A MIDI track's [[@KNOB 1]] sets its output channel. Tracks 1 to 4 can also
  choose MIDI Track as their engine.</p>
  <h3>Clock</h3>
  <p>[[GLO]] GLOBAL, [[@KNOB 3]] CLK chooses who keeps time. On <b>INT</b> (the default) the FM-1 leads and, new in
  1.6.1, sends MIDI clock, Start and Stop over USB and Bluetooth. On USB, TRS or BLE it follows that input instead.
  CLK is a device setting: loading a project doesn't change it.</p>
  <h3>MIDI LEARN</h3>
  <p>Hold [[HOME]], go to MIDI LEARN and press [[OCT+]]. Turn a knob on any track page, then move a controller. Up to
  16 bindings, kept only until power-off.</p>
  <h3>Bluetooth MIDI</h3>
  <p>Hold [[HOME]], go to BLUETOOTH and press [[OCT+]]. Turn the Radio on (music must be stopped). Set Mode to
  <b>VISIBLE</b> so a Mac, iPad or phone can connect to "Melodee", or <b>CONNECT OUT</b> to find a Bluetooth MIDI
  controller. If a PIN appears, enter all six digits on the other device, leading zeros included. One connection at a
  time; no Bluetooth audio.</p>
  <h3>USB host</h3>
  <p>Hold [[HOME]] and set USB HOST to ON to plug a USB MIDI keyboard or synth into the FM-1 itself. While it's on,
  there's no computer connection, and it switches off at every power-on. The FM-1 supplies no USB power.</p>
  <h3>The web editor</h3>
  <p>Melodee's web editor (Chrome or Edge, over USB) has sound and mixer controls, full editors for FM6, Prophet and
  CZ-1, the user sound library, SysEx import and export, and complete backup and restore. Some 1.6 features, such as
  timed punches and song presets, are edited on the device only.</p>
</section>
"""

CHANGES = f"""
<section class="back" id="changes">
  <div class="run">Coming from 1.5.1</div>
  <div class="kicker">Reference</div>
  <h2>Coming from 1.5.1? What changed</h2>
  <p class="lede">A short list for owners updating from Melodee 1.5.1, drawn from the 1.6.0 and 1.6.1 release notes.</p>
  <h3>New in 1.6.0</h3>
  <ul class="plain">
    <li><b>Longer songs:</b> 64 sections, per-track rests, blocks that stretch across sections, a minutes:seconds ruler, Loop song.</li>
    <li><b>Timed punch FX</b> in song sections: up to four per section.</li>
    <li><b>A preset for each block or pattern</b>, stored as an independent copy.</li>
    <li><b>16 patterns</b> on tracks 1 to 4, and <b>32 project slots</b> in one shared storage pool.</li>
    <li><b>Two new kits:</b> CR78 and FM.</li>
    <li><b>Bluetooth MIDI</b>, <b>MIDI LEARN</b> and <b>USB VOLUME</b>; editing note lengths while the sequence plays.</li>
  </ul>
  <h3>New in 1.6.1</h3>
  <ul class="plain">
    <li><b>MIDI clock out:</b> with CLK on INT, the FM-1 sends clock, Start and Stop. Not yet tried with real gear.</li>
    <li><b>No more drift:</b> the internal clock now runs on exact musical units. Synced LFOs lock to the song.</li>
    <li><b>CLK is a device setting:</b> loading a project no longer changes it.</li>
  </ul>
  {box("warn", "Before you update", "Back up on your current firmware first. Older firmware can't read what 1.6 saves and refuses backups made on 1.6. CZ-1 tracks now sit 6 dB lower in the mix and the limiter starts later, so check your balance. From 1.5.1 or earlier through Firmware Hub, install twice. Stored data is unchanged between 1.6.0 and 1.6.1.")}
</section>
"""

TROUBLE = f"""
<section class="back" id="trouble">
  <div class="run">If something goes wrong</div>
  <div class="kicker">Reference</div>
  <h2>If something goes wrong</h2>
  <h3 id="silent">I can't hear anything</h3>
  <p>Work down this list. Most silences are one of these.</p>
  <ul class="check">
    <li><b>Volume.</b> Turn [[@MASTER]] up. It's the FM-1's overall volume.</li>
    <li><b>Headphones or speakers.</b> If you're using them, check they're plugged into the FM-1's audio output, switched on and turned up.</li>
    <li><b>The right track.</b> The keys play the selected track: turn [[@ALGORITHM]] and watch the screen's colour change. Tracks 5 to 8 are MIDI tracks and make no sound of their own.</li>
    <li><b>Mute and solo.</b> Press [[GLO]] for the MIXER and check [[@KNOB 4]] (MUTE) is off for the track, and [[@KNOB 1]] (LEVEL) is up. If one track is soloed (hold [[GLO]]; the keys mute and solo), the others go quiet.</li>
    <li><b>Notes in the pattern.</b> On Stage, each track's row shows its pattern as dots: a hit is the track's colour, a rest is faint. A row of faint dots means an empty pattern, which plays nothing even while [[PLAY]] runs. On [[SEQ]] PATTERNS, patterns with notes glow.</li>
    <li><b>Is it playing?</b> Press [[PLAY]]. A song stops by itself after its last section.</li>
    <li><b>The sound itself.</b> A pad with a very slow attack takes a while to fade in. Try another preset to rule this out.</li>
  </ul>
  <table class="ref">
    <tr><th>You see</th><th>Try this</th></tr>
    <tr><td>Install stops or fails</td><td>Unplug and replug. Use a data cable in a direct port, Chrome or Edge, and press Install again.</td></tr>
    <tr><td>Setup unfinished, Factory sounds missing</td><td>Press Finish setup in the installer, or install again. Your own sounds are safe.</td></tr>
    <tr><td>STORAGE FULL</td><td>Erase a project you no longer need: tap [[SAVE]] twice for PROJECT, choose the slot, press [[OCT+]] and choose Erase. Then save again.</td></tr>
    <tr><td>PATTERN STORAGE FULL</td><td>The project's patterns are full (about 1,450 set steps). Clear an unused pattern.</td></tr>
    <tr><td>RECORDING FULL</td><td>The project's 1,024 recorded notes are used up. Clear or replace recorded parts.</td></tr>
    <tr><td>MOTION FULL</td><td>The 64 motion events are used up. Clear a lane on the MOTION page.</td></tr>
    <tr><td>STOP TO EDIT, STOP FIRST</td><td>That edit only works while stopped. Press [[PLAY]] to stop.</td></tr>
    <tr><td>AT LOOP END</td><td>Not an error: the change waits for the track's loop to finish.</td></tr>
    <tr><td>Three short key flashes</td><td>The MIDI update loader is running. Press Install again.</td></tr>
    <tr><td>Melodee Update on screen</td><td>Also the update loader. Press Install again with a working package.</td></tr>
    <tr><td>Black screen, seen as UBOOT</td><td>Use the fm1-recover tool from the release downloads and follow RECOVERY.md.</td></tr>
    <tr><td>Notes sound out of key</td><td>Check [[SCL]]: QNT, ROOT and scale are shared by the whole project.</td></tr>
  </table>
  <p>Report Melodee bugs on Melodee's GitHub Issues page, not to Felucca or M-VAVE. Report mistakes in this book on
  this book's GitHub page.</p>
</section>
"""

GLOSSARY_ITEMS = [
    ("Arpeggiator", "Plays held notes one at a time in a pattern."),
    ("Capture", "Hold REC to keep what you just played on the selected track, even though you weren't recording."),
    ("Chord", "Three or more notes played together."),
    ("Cutoff", "Where a filter starts removing high frequencies. Lower is darker."),
    ("Engine", "One of Melodee's instruments: Prophet, FM6, CZ-1, SID, Drum, or MIDI Track."),
    ("Envelope", "Shapes a sound over a note's life: Attack, Decay, Sustain, Release."),
    ("FM", "Frequency modulation: one oscillator bends another's pitch very fast, making new tones."),
    ("LFO", "Low frequency oscillator: a slow, steady wobble that moves a setting for you."),
    ("Motion", "Knob moves recorded into a pattern."),
    ("Pattern", "One looping phrase on one track. Each of tracks 1 to 4 has 16."),
    ("Phase distortion", "The CZ-1's method: bending a wave's shape to change its brightness."),
    ("Progression", "A short sequence of chords."),
    ("QNT", "Two different things: on SCL it keeps keys in the scale; on TEMPO it snaps recordings to a grid."),
    ("Resonance", "A ringing emphasis at the filter's cutoff."),
    ("Root", "The home note of a scale or chord."),
    ("Scale", "A set of notes that sound good together."),
    ("Section", "One row of a song: which pattern each track plays, or a rest."),
    ("Send", "How much of a track goes to the shared effects."),
    ("Stage", "Melodee's home page, where you play and see every track."),
    ("Step", "One slot in a pattern. Sixteen steps of 1/16 make one bar."),
    ("Track", "One part of your music, with its own sound and patterns."),
    ("Voicing", "How a chord's notes are stacked."),
]

GLOSSARY = f"""
<section class="back" id="glossary">
  <div class="run">Glossary</div>
  <div class="kicker">Reference</div>
  <h2>Glossary</h2>
  <dl class="gloss">{"".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in GLOSSARY_ITEMS)}</dl>
  <div class="credits">
    <h3>Thanks and credits</h3>
    <p>Melodee by Kerem Kilic (Ellic Studio), based on Felucca by Leo Kuroshita (@kurogedelic) and Hügelton Instruments.
    Melodee's manual by relyt29, updated by Ellic Studio. FM6 uses msfa from Dexed (Google Inc., Pascal Gauthier). CZ-1 is after
    MAME's uPD933 model by Devin Acker. SID uses reSID by Dag Lem. The 808 kit uses Hügelton's TR-808 circuit models; the
    909 kit is the schwung module 9W9 by AThousandDetails, ported via Charles Vestal's x0x. Effects from SLOOP. Prophet
    factory programs from Sequential; CZ-1 factory tones from Casio. Thanks to everyone who contributes to Melodee.</p>
    <p class="small">Melodee, Gently {ED} by slowphase · CC BY-SA 4.0 · Documents Melodee {FW}.</p>
  </div>
</section>
"""

BOOK = [COVER, IMPRINT, WELCOME, PANEL, MOVEIN, L1, L2, L3, L4, L5, L6, L7, L8, MPC, SHEETS, HOLDS, MIDI, CHANGES, TROUBLE, GLOSSARY]
