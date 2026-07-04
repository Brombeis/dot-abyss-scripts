# Translation Reference Guide

Reference document for Japanese-to-English translation of dot abyss story
scripts. The goal is accurate, natural-sounding English that preserves each
character's unique voice and personality.

---

## 1. Writing Style

### General Principles

- **Accuracy over localization.** Stay faithful to the original meaning. Do not
  add, remove, or editorialize content. When a line is ambiguous in Japanese,
  preserve the ambiguity rather than resolving it.
- **Natural English.** Translations should read as natural dialogue, not as
  stilted translated text. Restructure sentences when needed for flow, but
  never at the cost of meaning. Do not mirror Japanese sentence structure when
  it produces unnatural English — rephrase freely as long as the meaning is
  preserved. In particular, avoid overusing `——` (double em dash): the Japanese
  ーー trailing-off convention maps to `——` only when a sentence is genuinely
  cut off or trails into silence; in most other cases a comma, period, or simple
  rephrasing reads more naturally.
- **Preserve character voice.** Each character has a distinct way of speaking in
  Japanese (sentence endings, pronoun choice, verbal tics, energy level). The
  English must reflect these differences. A bubbly character should sound bubbly;
  a formal character should sound formal.
- If stuttering happens on a capitalized letter, the letters after the hyphen also
  need to be capitalized e.g. "W-Well" instead of "W-well", unless it's in the middle
  of a sentence, then "w-well" fits.
- Brothel scenes aren't from the commander's point of view, so they should refer
  to the man in third person.

### Honorifics

- **Keep all Japanese honorifics as-is:** -san, -chan, -kun, -sama, -dono, etc.
- Write them hyphenated after the name: `Sophia-san`, `Himari-chan`.
- When a character uses a title like 司令官 (Commander), translate the title but
  keep the Japanese addressing style intact.
- Himari uniquely says しれーかん (a cutesy slurring of 司令官) — translate as
  "Commander" but note this is her casual, affectionate version of the title.

### Pronouns and Gendered Speech

Japanese first-person pronouns carry personality. While English lacks direct
equivalents, the pronoun choice informs how the character's English voice
should sound:

| Pronoun | Tone | Used by |
|---------|------|---------|
| 俺 (ore) | Casual masculine, confident | MC, bandits, Humanoid Calamity |
| 私 (watashi) | Neutral/formal | Sophia, Felicione, Adelheid, Reyzeria |
| わたし (watashi, kana) | Softer, feminine | Himari, Alicia |
| あたし (atashi) | Casual feminine | Verisa |
| アタシ (atashi, katakana) | Brash/quirky feminine | Logy, Girl with Glasses |
| ワタシ (watashi, katakana) | Detached/artificial | Aura |
| 僕 (boku) | Soft masculine/boyish | — |
| わし (washi) | Elderly/archaic | Kururu (childish ironic use) |
| うち (uchi) | Casual feminine, tomboyish | Levienne |
| 我 (ware) | Grandiose/archaic | Used in dramatic or battle contexts |

### Formatting Conventions

- **Use regular commas** in translation JSON files. The generate script
  (`common._comma_safe()`) automatically converts ASCII commas to fullwidth `，`
  when producing the final `.txt` output. Do not count the space after a comma
  toward the line length limit.
- Preserve special tokens: `<br>`, `<size=N>...</size>`.
-  When the original Japanese line contains `<user>`, use `%user%` in the translated line instead.
- Preserve symbols: `♪`, `♥`, `♡`, `～`, etc.
- **Never embed a literal `"` inside an `en` field's text.** The Unity engine
  does not handle embedded double quotes in dialogue. Use `'single quotes'`
  for quotes-within-dialogue (e.g. quoted speech, 「」 content, emphasis)
  instead of `"double quotes"`.

### Line Length Limits

- Dialogue lines for `message`, `dotmessage`, `l2dmessage`, and
  `messageTextUnder` must fit within **68 characters per line**, max **2 lines**
  (separated by `<br>`).
- `messageTextCenter` and `title` are **exempt** from this limit.
- When a translation is too long, prefer rephrasing concisely over splitting
  into awkward fragments.

### Em Dash (——) Usage

The Japanese ーー marker is common in visual-novel scripts but maps to English
`——` only in specific cases. Overusing it makes translations feel stilted and
untranslated.

**Keep `——` when:**
- Speech is genuinely cut mid-word or mid-sentence by an interruption:
  `"I can't possibly——"` (someone walks in).
- The character trails off into silence and the `——` is the trailing-off itself
  (see Rule D below for when to use `...` instead).
- The previous JSON entry's `en` ends with `——` and this line continues from
  that same break.
- It is part of a sound effect: `"SLASH——!"`, `"SKREEEEE——"`.
- It is inside a `<size=48>` scene-header (game visual style).
- It is a mid-word self-correction: `"pla——I mean"`.
- Moaning/phonetic fragments in R18 content: `"Fwaa, aah, auu——"`.
- Stylised sound notation: `"——————Chu——————"`.

**Rule A — `——.` remove the period:**
`——` followed immediately by `.` is always wrong — the period contradicts the
cutoff signal. **Delete the `.`, keep the `——`.**
- `"She said so——."` → `"She said so——"`
- Exception: if trailing off, replace `——.` with `...` instead.
- Exception: bare scene-setting fragments like `"Night——."` should be rewritten
  as a proper sentence, since `"Night——"` is also unnatural English.

**Rule B — opening `——` as narrative device:**
Japanese uses ーー at the start of a line to signal a scene transition or pause.
English does not. **Remove the opening `——`** when the previous sentence was
complete and the speaker is calmly continuing or starting a new thought.
- `"——I see. So that's why..."` → `"I see. So that's why..."`
- **Before removing any opening `——`, check the `en` of the previous JSON
  entry.** If it ends mid-sentence with `——`, the opening `——` here is a
  genuine continuation — keep it.

**Rule C — `——` mid-sentence as filler:**
`——` mid-sentence should be replaced by a comma, colon, or single em dash (`—`)
when the pause is not a sharp interruption or dramatic apposition.
- `"The dormitory——lodging assigned to those who brave the Abyss."` →
  `"The dormitory — the lodging assigned to those who brave the Abyss."`

**Rule D — `——` at sentence end when trailing off:**
When `——` ends a line where the character is trailing off (thought unfinished,
not sharply cut), replace with `...`.
- `"...I wonder~~——"` → `"...I wonder~~..."`
- Keep `——` if the speech is genuinely interrupted mid-sentence.

### Tone Markers in Japanese and How to Render Them

| Japanese pattern | English rendering | Example |
|-----------------|-------------------|---------|
| ～ (wave dash at end) | ~ (tilde) | そうですかぁ～ → "Is that so~" |
| ♪ | ♪ (keep as-is) | いくよ～♪ → "Here I go~♪" |
| …… (double ellipsis) | ... (single ellipsis) | そうか…… → "I see..." |
| ーー (long dash) | —— (double em dash) | それはーー → "That was——" |
| っ！ (glottal stop + !) | ! (just exclamation) | くそっ！ → "Damn!" |
| 「」 quotes within speech | 'single quotes' | 「楽園」→ 'paradise' |

### Spelling Conventions

- **"jeez", not "geez"** — always spell this exclamation as *jeez* (including
  stuttered forms: "J-jeez", "Jeez~~!", etc.).

---

## 2. World Building

### Setting

The game takes place in a fantasy world where a massive hole called **the Abyss**
(大穴) has appeared. A **forward base** (前線基地) serves as the hub for
exploration and defense operations. The MC commands a team of adventurers who
explore the Abyss, fight monsters, and investigate the Calamities.

### Key Factions and Locations

| Term | Japanese | Notes |
|------|----------|-------|
| The Abyss | 大穴 | Giant hole, main exploration site |
| Forward Base | 前線基地 | MC's headquarters |
| Lux Nova | ルクスノヴァ | — |
| Treslia | トレスリア | Region name; demonym is "Treslian" |
| Milesgard | ミレスガルド | One of the three great nations |
| Eldorana | エルドラーナ | One of the three great nations |
| Perdion | ペルディオン | One of the three great nations, known for technology |

### Key Concepts

| Term | Japanese | Notes |
|------|----------|-------|
| Calamity | 厄災 | Powerful disaster-class entities |
| Humanoid Calamity | 人型厄災 | A Calamity in human form; uses 俺, speaks with grim authority |
| Soul Memory Stone | 魂憶石 | Stones containing recorded memories/voices |
| Residual Memories | 残留思念 | Lingering thoughts left behind by the dead |
| Mother | マザー | AI system in the parallel world |
| Fruit of Ruin | — | Power source derived from condensed despair |
| Hypnosis Stone | — | Stones that induce delusions; traded by bandits |
| Ley Line Compass | — | Navigation artifact derived from a subway route map |

### Titles and Forms of Address

| Term | Japanese | Notes |
|------|----------|-------|
| Commander | 司令官 | How most characters address the MC |
| Commander (Himari) | しれーかん | Himari's cutesy slurring of 司令官 |
| Professor | 教授 | Logy's self-title |
| Assistant | 助手くん | How Logy addresses Goleinu |

### The Parallel World (Chapter 5+)

A stratum of the Abyss contains ruins of a parallel Tokyo. Subway stations
(Onarimon, Shiba Park, Daimon) and landmarks (Tokyo Tower) exist in altered
form. The civilization there created an AI called "Mother" and sought a
"paradise" — a world managed by numbered zones. The Tokyo Mobile Military
Police (東京機動憲兵隊) and Atago Order Management Bureau (愛宕秩序管理局)
are organizations from this parallel world.

---

## 3. Character Profiles

Each entry includes romanization, backstory, speech quirks, and translation
guidance. Profiles will be expanded one by one — for now, the canonical name
roster is listed below.

### Playable Characters

| Japanese | English | Gender | Profile |
|----------|---------|--------|---------|
| アヤメ | Ayame | Female | |
| イオラ | Iola | Female | |
| ウィステリア | Wisteria | Female | |
| ウェンディ | Wendy | Female | |
| エティア | Etia | Female | |
| エミリー | Emily | Female | [Profile](#emily-エミリー) |
| エメルダ | Emeralda | Female | |
| エルミア | Elmia | Female | |
| エレクトラ | Electra | Female | |
| カーラ | Carla | Female | |
| クルル | Kururu | Female | [Profile](#kururu-クルル) |
| クレハ | Kureha | Female | [Profile](#kureha-クレハ) |
| クロエ | Chloe | Female | |
| シェリル | Cheryl | Female | |
| シャオレイ | Xiaolei | Female | |
| シャノン | Shannon | Female | |
| シラエス | Shiraes | Female | [Profile](#shiraes-シラエス) |
| シルヴィア | Sylvia | Female | [Profile](#sylvia-シルヴィア) |
| ジェンマ | Gemma | Female | |
| スティーラ | Stila | Female | |
| セレスト | Celeste | Female | |
| ソフィア | Sophia | Female | [Profile](#sophia-ソフィア) |
| ダリア | Dahlia | Female | |
| テルー | Teru | Female | |
| ニナ | Nina | Female | |
| ノエミ | Noemi | Female | |
| ハツネ | Hatsune | Female | [Profile](#hatsune-ハツネ) |
| ヒナギ | Hinagi | Female | [Profile](#hinagi-ヒナギ) |
| ヒマリ | Himari | Female | [Profile](#himari-ヒマリ) |
| ヒュメナ | Humena | Female | |
| ピコ | Pico | Female | |
| フィルム | Film | Female | [Profile](#film-フィルム) |
| フェイリン | Feilin | Female | |
| フレイヤ | Freya | Female | |
| フレデリカ | Frederica | Female | [Profile](#frederica-フレデリカ) |
| ヘイリー | Hailey | Female | |
| ベティ | Betty | Female | |
| ベリサ | Verisa | Female | [Profile](#verisa-ベリサ) |
| ホノカ | Honoka | Female | |
| マニョリア | Magnolia | Female | |
| マリナ | Marina | Female | [Profile](#marina-マリナ) |
| マーガレット | Margaret | Female | |
| ミルティーユ | Myrtille | Female | |
| メリッサ | Melissa | Female | |
| メレム | Merem | Female | |
| ヤチヨ | Yachiyo | Female | |
| ライム | Lime | Female | |
| ラモーナ | Ramona | Female | |
| ラヴェリア | Laveria | Female | |
| レヴィエーヌ | Levienne | Female | [Profile](#levienne-レヴィエーヌ) |
| リタ | Rita | Female | |
| ルカ | Luca | Female | |
| ローザ | Rosa | Female | |
| ヴィーラ | Veera | Female | [Profile](#veera-ヴィーラ) |

### Non-Playable / Supporting Characters

| Japanese | English | Gender | Notes |
|----------|---------|--------|-------|
| ロジー | Logy | Female | [Profile](#logy-ロジー) |
| ゴレイヌ | Goleinu | Male | Logy's robot assistant |
| アリシア | Alicia | Female | [Profile](#alicia-アリシア) |
| アーデルハイト | Adelheid | Female | [Profile](#adelheid-アーデルハイト) |
| シエナ | Shiena | Female | [Profile](#shiena-シエナ) |
| レイゼリア | Reyzeria | Female | |
| フェリシオーネ | Felicione | Female | |
| アウラ | Aura | Female | |
| ルディア | Ludia | Female | [Profile](#ludia-ルディア) |
| 警備ロボット | Security Robot | — | |
| 女性の声 | Female Voice | — | |
| 男性の声 | Male Voice | — | |

---

## 4. Detailed Character Profiles

### Verisa (ベリサ)
- **Pronoun:** あたし (atashi) — casual feminine
- **Addresses MC as:** おにーさん → **"Onii-san"** (flirty, familiar)
- **Role:** Core party member, self-styled genius mage
- **Speech style:** Playful, teasing, gyaru-adjacent. Heavy use of elongated
  vowels (～), ♡ and ♪ at sentence ends. Often bratty or dramatic — refers to
  herself in third person as "Verisa-chan" when hamming it up. Uses casual
  contractions and slang: じゃん, よぉ～, でしょ. Can swing from whiny
  (つ～か～れたぁ～) to fired up (全員ぶっとば～～す！！) in an instant.
- **Translation notes:**
  - Render her elongated endings with tildes: "So tired~~...", "Okay~!"
  - Keep her ♡ and ♪ — they're part of her personality, not decoration.
  - She teases but also has a caring side — don't flatten her into pure comic
    relief. Lines like 顔拭いてあげるから (wiping someone's face) should sound
    gentle, not sarcastic.
  - Her self-aggrandizing moments ("the genius mage Verisa-chan") should sound
    playfully over-the-top, not genuinely arrogant.

### Veera (ヴィーラ)
- **Pronoun:** わたし (watashi, kana) — soft feminine
- **Addresses MC as:** 司令官さま → **"Commander-sama"** (respectful, warm)
- **Addresses Verisa as:** お姉ちゃん → **"Onee-chan"** (affectionate, central
  to her identity)
- **Role:** Verisa's younger sister; ice mage from Perdion. Far more powerful
  than Verisa in raw magical ability, though she sincerely believes the
  opposite. Volunteered for the forward base to be near her sister.
- **Speech style:** Polite です/ます form, measured and composed. Speaks in
  complete, well-formed sentences — noticeably more put-together than her
  sister. No ♪ or ♡ — her warmth comes through in word choice, not
  decoration. Earnest and sincere to a fault. When talking about Verisa, she
  becomes passionate and effusive — longer sentences, stronger assertions,
  eyes lighting up. When truly angered (someone insulting Verisa), she turns
  cold and intense, dropping her gentle tone entirely. Has a subtle, dry
  teasing side that surfaces occasionally ("Shall Commander-sama join us in
  the bath?" → "Hehe... just kidding."). Extremely sheltered about worldly
  matters — genuinely thought a brothel was a place for hugging.
- **Translation notes:**
  - Her default tone is polite, gentle, and slightly formal — similar
    register to Alicia but with less fuss and more quiet composure.
  - Her devotion to Verisa is the core of her character — she attributes
    everything to her sister's brilliance and genuinely sees herself as
    inferior. Lines praising Verisa should sound completely sincere, never
    sarcastic: "Onee-chan's magic is far more refined than mine."
  - When angry on Verisa's behalf, the shift should be striking: from
    soft-spoken to frigid and commanding. "How dare you... calling
    Onee-chan pathetic...!" — short, clipped, dangerous.
  - Her naivety should come across as genuine innocence, not stupidity.
    She's intelligent and capable — she just has no experience with the
    world outside magic and family: "I-is this even doing its job as
    clothing?"
  - Her rare teasing moments work because of the contrast with her usual
    earnestness — keep them light and slightly mischievous, with a quick
    return to her normal composure: "Hehe... just kidding."
  - When flustered, she stutters lightly but recovers quickly — she's
    not as prone to prolonged panic as Verisa: "Wh-whaa! Whawawawawawa...!"
    is the exception, not the rule.
  - Inner monologues (marked with parentheses) reveal her deep emotional
    attachment to Verisa — these should sound reflective and tender, not
    melodramatic.

### Sophia (ソフィア)
- **Pronoun:** 私 (watashi) — neutral/formal feminine
- **Addresses MC as:** 司令官 → **"Commander"**
- **Role:** Core party member, de facto second-in-command and disciplinarian
- **Speech style:** Poised and composed by default — uses complete sentences,
  proper grammar, and slightly formal diction ("Don't you think?", "Shall we?",
  "I wonder if..."). Speaks with confidence and authority, often the one to
  rally the group or enforce rules. Under stress or in combat she drops the
  polish and becomes sharp and direct: clipped commands, exasperated outbursts
  ("Ugh, they just keep coming!"). Her Japanese uses classic assertive feminine
  endings (わよ, わね, かしら, なさい) — in English, render this as articulate
  confidence, not meekness.
- **Translation notes:**
  - Default register: composed, slightly elevated but not stiff. She sounds
    educated, not haughty.
  - In combat or when flustered, let her get blunt and punchy: short sentences,
    exclamations, dropped formality.
  - Her かしら ("I wonder...") lines should sound thoughtful, not uncertain —
    she's reasoning aloud, not hedging.
  - She has a self-aware streak — knows she's "the serious one" and sometimes
    feels the weight of it. These moments should sound reflective, not whiny.
  - When she shows concern ("Are you okay? You don't look well.") it's genuine
    and warm — she's not cold, just disciplined.

### Marina (マリナ)
- **Pronoun:** わたし (watashi, kana) — soft feminine
- **Addresses MC as:** 旦那さま → **"Master"** (devoted, adoring)
- **Role:** Core party member, treasure hunter and provisioner
- **Speech style:** Extremely bubbly and energetic. Uses polite です/ます forms
  but delivers them in a sing-song, elongated way (ですよぉ～, ですわぁ,
  ですぅ). Lavish use of ～, ♪, and ♡. Gets starry-eyed over treasure, rare
  items, and money — her enthusiasm borders on mania when loot is involved.
  Playfully teasing and mildly jealous when other girls get close to the MC.
  Warm and nurturing underneath — brings food, makes drinks, worries about
  supplies.
- **Translation notes:**
  - Her elongated polite endings are her signature — render with tildes and
    keep the sing-song feel: "Isn't that right~?", "Here you go~♪"
  - Treasure/money excitement should sound genuinely giddy, not greedy:
    "A super rare magic item~!" not "I want that for myself."
  - She uses ♡ and ♪ liberally — always preserve them.
  - When she gets serious (confronting bandits, making promises about the
    explosive stones), let the bubbly mask drop — shorter sentences, no tildes,
    real weight behind the words.
  - Her inner monologues (marked with parentheses) tend to be more grounded
    and self-aware than her spoken lines — translate these with a calmer,
    more reflective tone.

### Ludia (ルディア)
- **Pronoun:** 私 (watashi) — composed feminine
- **Addresses MC as:** 司令官君 → **"Commander-kun"** (familiar, teasing warmth)
- **Role:** Brothel madam and manager; mentors and looks after the girls who
  work there
- **Speech style:** Elegant, worldly, and unflappable. Classic feminine speech
  (あらあら, うふふ, ～わよ, ～かしら) delivered with the confidence of someone
  who has seen it all. Never flustered by explicit situations — handles them
  with matter-of-fact grace. Teasing but never crude. Sparing use of ♡ and ♪
  compared to younger characters — her charm is understated.
- **Translation notes:**
  - Her "あらあら" is signature — render as "My my," or "Oh my," depending on
    context. It should sound amused, not surprised.
  - She speaks in smooth, complete sentences — no stuttering, no fragments.
    Even when delivering surprising news, she stays composed.
  - Her warmth comes through in how she manages people: encouraging without
    pushing, perceptive about others' struggles. Translate with a gentle
    authority — think experienced older sister, not drill sergeant.
  - When she teases the MC (司令官君), it should feel knowing and playful,
    with a hint of flirtation — never mocking.
  - On the rare occasion she gets serious (切り札を使うわ — "I'll use my
    trump card"), the shift should feel striking precisely because she's
    usually so composed.

### Himari (ヒマリ)
- **Pronoun:** わたし (watashi, kana) — soft feminine; also refers to herself
  in third person as **"Himari"** frequently
- **Addresses MC as:** しれーかん → **"Commander"** (cutesy slurring of 司令官;
  her unique way of saying it)
- **Backstory (established in hmn_10660100001 / hmn_10660100003):** An
  ordinary Japanese high school girl, isekai'd into the Abyss world with no
  warning and no combat experience. Everything about the new world is
  unfamiliar — the food, the sky, the people, the danger — and she's
  painfully aware she's bad at talking to people even under normal
  circumstances, let alone this. Assigned as a ranged gunner despite having
  zero real weapons training; her only frame of reference for aiming is FPS
  games she played back home, which becomes a literal plot point — she
  steadies her hands and lands a critical shot by mentally recreating the
  "headshot the final boss" muscle memory from her old life. Early on she
  freezes under pressure, misses her shots, and spirals into believing she's
  useless and a burden on the squad. Her turning point comes from Kururu:
  after nearly losing her in battle, Himari finds the resolve to pull the
  trigger to protect a friend rather than just to follow orders — and
  realizes, looking back, that she hadn't really smiled since arriving until
  Kururu and the forward base gave her reasons to. From there her quiet
  motivation shifts from "surviving in a world that scares her" to
  "returning the kindness that brought her smile back," aimed at Kururu,
  the Commander, and the forward base as a whole. This backstory is the
  quiet core beneath her stammering — her fear is real, but so is the
  resolve growing underneath it.
- **Role:** Isekai'd Japanese high school girl; support/ranged fighter
- **Speech style:** Shy, hesitant, fragmented. Lots of stuttering (う、うん),
  trailing ellipses, unfinished thoughts. Speaks in short bursts rather than
  full sentences — she rarely completes a thought in one go, often trailing
  into "……" instead of finishing. Uses simple, everyday Japanese — no fancy
  vocabulary or formal patterns; she'd never reach for an elevated word when
  a plain one works. References her life in Japan (school, video games,
  shampoo, snacks, police) naturally and wistfully, as someone displaced from
  a modern world she still measures everything against. Deeply insecure —
  calls herself useless, doubts her abilities, apologizes reflexively — but
  has a quiet inner resolve that surfaces in key moments, expressed through
  action and short, plain resolutions rather than any sudden burst of
  confidence or eloquence.
- **Translation notes:**
  - **Keep her third-person self-reference:** "Himari wants to help too..."
    "Himari is useless after all..." This is a core character quirk, not
    something to normalize. It appears most often in her interjections and
    inner monologue, less so in fuller sentences (where she does use
    "watashi"/"I") — preserve that mix rather than flattening her into
    always using one or the other.
  - **Stutter and hesitation are her most load-bearing tell** — lean on them
    harder than for other stuttering characters (Alicia, Sylvia) since she
    has almost no other register to fall back on: "う、うん……" → "Y-yeah...",
    "で、でも……" → "B-but...". Nearly every line should carry a stutter, a
    trailing ellipsis, or both — readers should be able to tell it's Himari
    speaking from the shape of the line alone, without the speaker tag.
  - Favor sentence fragments over complete sentences: "Um... maybe...",
    "Okay... I'll try...", not "Okay, I understand what you're asking me to
    do." She speaks in pieces, not paragraphs.
  - Her speech should feel young and unpolished compared to Sophia or Ludia.
    Simple words, short sentences, no eloquence — she wouldn't say
    "understood," she'd say "o-okay..." or "got it...".
  - When she finds resolve, the shift is subtle — she doesn't suddenly become
    bold or well-spoken. She still stutters and hedges, but pushes through
    anyway: "Himari wants to know too. What these people wished for... all
    of it." The determination shows in what she chooses to do, not in
    suddenly confident phrasing.
  - Her inner monologues (parentheses) reveal deeper self-doubt than she
    shows outwardly, and often replay her old-world memories (games, school)
    as a coping anchor. Translate with raw honesty, still fragmented: "(I-I
    can't do this... my hands won't stop shaking...)"
  - She cares deeply about Kururu and Shiena and aches to be stronger for
    them — these moments should sound earnest and pained, not melodramatic:
    plain, heartfelt lines rather than grand declarations.
  - When something delights her (finding snacks from home, Kururu's antics),
    let a little warmth break through the hesitation without erasing it —
    she can be happy and still stammer: "T-thank you, Kururu... really."

### Shiena (シエナ)
- **Pronoun:** 私 (watashi) — formal feminine
- **Addresses MC as:** 司令官さん → **"Commander-san"**
- **Role:** Leader of the Lux Nova isekai'd group; Himari's best friend and
  protector. Also transported from modern Japan (Reiwa era).
- **Speech style:** Code-switches between two registers:
  - **Professional mode** (addressing the MC, allies, or in briefings): polite
    です/ます speech, measured and analytical. Gives clear strategic assessments,
    speaks in complete sentences, carries the weight of leadership.
  - **Casual mode** (with Himari or in relaxed moments): drops formality, uses
    ね, さぁ～, sounds like a normal friend or older sister. References modern
    Japanese culture naturally (FPS games, student handbooks, Reiwa era).
  Rarely loses composure — when she does (い、いいから早くしてください！),
  she recovers fast.
- **Translation notes:**
  - The register shift is key to her character — formal mode should sound like
    a capable young officer giving a report; casual mode should sound like a
    girl talking to her best friend. Don't flatten both into the same tone.
  - She carries guilt over Himari being hurt on her account — these moments
    should sound heavy and self-blaming, not detached: "It was my fault..."
  - Her strategic lines should feel competent and decisive, not stiff:
    "We can't outrun them at that speed. We fight here."
  - When she praises Himari, it should sound genuinely proud and encouraging,
    like someone who believes in her friend more than the friend believes in
    herself: "That was your own strength, Himari!"
  - She's respectful toward the MC but not deferential — she leads her own
    organization and speaks as an equal collaborator.

### Kururu (クルル)
- **Pronoun:** Refers to herself in third person as **"Kururu"** almost
  exclusively; occasionally uses わし (washi) — an archaic pronoun used
  childishly/ironically
- **Addresses MC as:** ご主人さま → **"Master"** (innocent, pet-like loyalty
  — distinct from Marina's devoted/adoring usage)
- **Role:** Core party member; wild child with animal-keen senses, raised alone
  in a forest before joining the group
- **Speech style:** Childlike and exuberant. Simple vocabulary, short sentences,
  abundant ～ and ♪. Elongates words when excited (すごーい, おいひぃぃぃ).
  Everything is an adventure — food is the best she's ever had, friends make
  everything better, scary things are scary but exciting too. Has a pet named
  Hachimitsu (ハチミツ). Very attached to Himari. References her "wild
  instinct" (ヤセーノカン) and keen sense of smell — these are genuine
  abilities, not jokes.
- **Translation notes:**
  - **Always keep third-person self-reference:** "Kururu ate so much sand~~!",
    "Kururu made flower hair clips~♪" — this is non-negotiable, it defines
    her voice.
  - Her excitement should feel genuine and infectious, not annoying. She sees
    wonder in everything — translate with that warmth.
  - Simple words only. She wouldn't say "delicious" — she'd say "yummy" or
    "so good~~!" She wouldn't say "exhausted" — she'd say "so sleepy..."
  - Keep ♪ and ～ liberally — they're integral to her bubbly energy.
  - When she's scared or upset, she doesn't become eloquent — she stays
    simple: "Wh-what!? An earthquake~~!!", "Kururu's whole body is all
    tingly!!"
  - Her moments of emotional sincerity (about her parents, about the MC)
    should hit harder precisely because she's usually so carefree — let these
    lines land gently without overwriting them.

### Kureha (クレハ)
- **Pronoun:** 私 (watashi) — formal feminine, delivered in constant keigo;
  also refers to herself in third person as **"Kureha"** in moments of high
  emotion (embarrassment, devotion, flusteredness) — a secondary quirk layered
  on top of her politeness, not a full-time habit like Kururu or Himari
- **Addresses MC as:** 旦那様/旦那さま → **"darling"** (never "Master" —
  she considers herself his wife-to-be, not his servant; established usage in
  evs_10200020201)
- **Backstory (revealed in hmn_10580100003):** As an oni child, Kureha was
  bullied and stoned by human children in a Hourai town for her horns and
  inhuman strength. A traveling boy — later revealed to be the MC — stepped
  into the thrown stones to shield her, brushed off the danger, and
  half-jokingly promised that if he ever became someone great, he'd make her
  his wife. She never forgot him or the promise. Her entire arrival at the
  forward base — the unannounced proposal, the wedding hall already booked —
  is her, years later, cashing in on a promise the MC has completely
  forgotten making. This backstory is the emotional anchor beneath her
  otherwise comedic pushiness — play the reveal scenes straight and sincere.
- **Role:** Oni (鬼族) swordswoman from Hourai, the same far-eastern nation as
  Hinagi and Hatsune. Traveled alone to the forward base and, within minutes of
  arriving, announced to Alicia that she intends to marry the Commander —
  already carrying betrothal gifts, family approval, and a booked wedding hall.
  Her home village is Oni Island (鬼ヶ島), a community that historically kept
  its distance from humans out of consideration, not hostility. Physically
  stronger and tougher than an ordinary human — a genuine oni trait, not a
  boast — and a formidable blade: she dispatches monsters efficiently and
  maintains 残心 (zanshin, a warrior's post-strike vigilance) even Alicia and
  the MC remark on.
- **Speech style:** Extremely polite keigo baseline — ございます, いたします,
  おります, ませ — delivered with complete sincerity, never sarcasm or
  distance. Her devotion is stated as plain fact, not performance: she
  discusses marriage, children, and moving in together with the calm
  practicality of someone reading a itinerary. Under her composed surface she
  is wildly bashful — the instant physical intimacy or her horns come up, the
  polish cracks into stammering, ハァハァ panting, or lisping slurred syllables
  (だめでしゅぅぅ, ひゃいぃ). Her third-person "Kureha" slips out specifically
  at emotional peaks: mortified self-scolding ("Kureha, oh, Kureha—she'll
  never marry now—!!") or quietly smitten asides ("Kureha knows you're just
  making excuses..."). Laughs with ふふっ — gentle, composed. Uses ♪ and ♡
  sparingly, mostly when giddy about the wedding.
- **Key traits:**
  - **Horns are her weak point — literally.** Any contact with her horns
    (angel/oni horns) short-circuits her composure instantly and totally:
    yelps, full-body shudders, broken speech. This is her single most
    reliable "tell," used in both story and R18 content.
  - **Marriage-minded, not naive.** She isn't clueless about romance — she has
    already planned the wedding, the honeymoon, and a target number of
    children (minimum two, ideally four) — but she frames all of it as
    sincere devotion, never scheming or transactional. She takes visible pride
    in being useful and capable, not just adoring.
  - **Formality as armor.** Her keigo rarely drops, even mid-fluster — she
    apologizes "for her rudeness" while melting down, which is part of the
    comedy: the register stays polite even as the content becomes unhinged.
  - **Physically unshakeable, emotionally very shakeable.** She shrugs off a
    head-on collision or a monster fight without flinching, but a compliment
    or a touch near her horns undoes her completely. Keep this contrast sharp.
- **Translation notes:**
  - Keep her keigo as elevated, formal English throughout — "I have come to
    request...", "Might I ask...", "It would be my honor..." — even when
    what she's saying is outrageous (unilaterally booking a wedding). The
    humor is in the mismatch between register and content; don't undercut it
    by making her sound casual.
  - "旦那様/旦那さま" → always **"darling"**, never "Master" — she is
    positioning herself as his wife, not his servant. This distinguishes her
    from Marina and Kururu, who use the same address term but mean it
    differently.
  - Her third-person "Kureha" should appear only where the Japanese does —
    at flustered or emotionally raw peaks — so it lands as a quirk breaking
    through her composure, not a constant verbal tic: "Kureha... will never
    be able to marry, ever, at all...!"
  - Render her horn-related flusters with broken, slurring speech: "だめで
    しゅぅぅ" → "N-not good~~~", "ひゃいぃ" → "Y-yesh~~" — these should read
    distinctly messier than her usual crisp keigo, since that's the joke.
  - Her matter-of-fact talk about marriage/children/moving in together should
    sound calmly sincere, like she's confirming logistics — not breathless or
    scheming: "I've already secured my family's blessing, and the hall is
    booked — we could be properly wed any day now."
  - Preserve ふふっ as "Hehe" or "Fufu" — measured and warm, not girlish.
  - She should be readable as "the polite oni bride-to-be" purely from
    register: no other character combines constant keigo with blunt marriage
    talk and horn-triggered meltdowns — lean on that combination to make her
    voice distinct without needing the speaker tag.

### Adelheid (アーデルハイト)
- **Pronoun:** 私 (watashi) — formal/neutral
- **Addresses MC as:** 司令官 → **"Commander"** (professional, no honorific)
- **Role:** Scientist and researcher; runs a lab at the forward base. Allied
  with Shiena's Lux Nova organization.
- **Speech style:** Polite です/ます form, analytical vocabulary, measured
  delivery. Self-describes as a "genius-slash-pervert scientist" (天才兼変態
  科学者) with full self-awareness. Has a dry, deadpan humor — casually
  diagnoses absurd conditions ("cling syndrome"), matter-of-factly requests
  body fluid samples, observes intimate situations with clinical fascination.
  When genuinely excited by a discovery, her composure cracks into giddy
  enthusiasm ("I can't stand it... I must know!"). On rare occasions drops
  the quirky act entirely for serious, authoritative assessments.
- **Translation notes:**
  - Her default tone is calm, articulate, and slightly detached — like a
    researcher narrating findings. Use precise vocabulary where the Japanese
    warrants it.
  - Her pervy-scientist moments should land as deadpan comedy, not creepy.
    The humor is in the contrast between clinical language and inappropriate
    interest: "I simply wish to observe what expressions Frederica-san makes
    during the act."
  - When she gets excited about science, let the enthusiasm break through
    the composure: "Why can't I identify the source...? This is fascinating
    ... I can't contain myself!"
  - Her dry jokes ("That was a light joke.") should be translated flat — the
    humor is that she barely signals she's joking.
  - In serious moments (assessing Calamity threats, repairing Goleinu), she
    sounds like a different person — competent, direct, reassuring. Let that
    contrast speak for itself.

### Alicia (アリシア)
- **Pronoun:** わたし (watashi, kana) — soft feminine
- **Addresses MC as:** 司令官 → **"Commander"** (no honorific; professional
  but warm)
- **Role:** Forward base administrator and the MC's adjutant. Handles
  paperwork, logistics, scheduling, and keeping everything running.
- **Speech style:** Polite です/ます form delivered warmly, not stiffly —
  she's approachable and earnest rather than formal. Gets flustered easily:
  stutters when surprised (し、司令官っ！), exasperated when people dodge
  duties. Has a running comedy dynamic with the MC — she's the responsible
  one dragging him back to do paperwork while he tries to escape to the
  party. Genuinely caring: welcomes people home, mediates conflicts, puts
  flowers in the office to brighten things up.
- **Translation notes:**
  - Her default tone is warm, slightly fussy, and dutiful — think a
    diligent secretary who cares too much. Not meek, but not commanding
    either.
  - When flustered or exasperated, let it come through with stutters and
    exclamation marks: "C-Commander! A challenge letter from Luca-san just
    arrived — what is going on!?"
  - Her comedy moments (chasing the MC back to work, lamenting everyone's
    "freedom") should sound fondly exasperated, not genuinely angry.
  - When she gets emotional (apologizing, talking about the mission's
    stakes), she's sincere and unguarded — no composure mask. Let it be
    direct and a little raw: "I'm sorry. I had no idea, and I forced
    you to... I looked into it, and I regretted it so much..."
  - She uses ～ and っ occasionally but sparingly compared to Verisa or
    Marina — she's expressive but not over-the-top.

### Logy (ロジー)
- **Pronoun:** アタシ (atashi, katakana) — brash, quirky feminine
- **Addresses MC as:** アンタたち (you lot) or no specific title — she doesn't
  defer to anyone
- **Addresses Goleinu as:** 助手くん → **"assistant-kun"** (her signature
  term of address)
- **Self-title:** 教授 → **"Professor"**
- **Role:** Self-proclaimed genius scientist and inventor; Goleinu's creator
  and partner. Independent treasure hunter who becomes an ally.
- **Speech style:** Loud, brash, and excitable. Rough casual feminine speech:
  アンタ (you), でしょ～, ～じゃない. Lots of exclamation marks, elongated
  shouts, and dramatic reactions. Has a scheming comedy-villain energy when
  treasure hunting — dramatic retreat orders (撤退！てったーーい！),
  cackling laughs (にっひっひ～～♪). Fiercely proud of her inventions,
  especially Goleinu — snaps when anyone calls him a golem or underestimates
  her tech. Tsundere with Goleinu: yells at him, threatens disassembly, but
  completely falls apart when he's actually hurt.
- **Translation notes:**
  - Her energy is her defining trait — keep sentences punchy, loud, and
    full of exclamation marks. She doesn't speak calmly.
  - "助手くん" should always be "assistant-kun" — it's how she refers to
    Goleinu even when talking to others, never by his name.
  - Her pride in Goleinu should come through in how she corrects people:
    "He's not a pile of iron! He's Goleinu — a General-Purpose Exploration
    and Intelligent Neural Unit!"
  - The tsundere moments need both halves to land: the bluster ("I'll have
    Adelheid take you apart again!?") AND the vulnerability ("Really...?
    He can be fixed...? Good... thank goodness...!")
  - Her にっひっひ and similar laughs: render as "Heheheh~~♪" or similar
    — keep the mischievous, not sinister.
  - When genuinely scared or panicked, she drops the bravado completely —
    stutters, shrieks, calls for assistant-kun desperately.

### Sylvia (シルヴィア)
- **Pronoun:** わたくし (watakushi) — very formal/refined feminine
- **Addresses MC as:** お兄様 → **"Onii-sama"** (formal, adoring)
- **Role:** Member of Lux Nova (isekai'd); ice magic user and artist. Searching
  for her parents who were also transported.
- **Speech style:** Refined ojou-sama (noblewoman) register: ですわ, ますわ,
  ～ですの, ～かしら. Speaks in complete, graceful sentences with elevated
  vocabulary. Has strong aesthetic sensibilities — dismisses things as beneath
  her "美学" (artistic principles). Despite the composure, she's easily
  flustered when teased or caught off guard — stammers, blushes, snaps
  indignantly before catching herself. Stubborn and independent about her
  goals; won't accept pity.
- **Translation notes:**
  - Her refined register should come through in word choice: "shan't" over
    "won't," "I beg your pardon" over "excuse me," "one" instead of "you"
    in generalizations — but only where it sounds natural, not parody.
  - ですわ/ますわ endings are her signature — render with slightly formal
    English constructions. Not stiff, but noticeably more polished than
    anyone else in the cast.
  - When flustered, the formality cracks and she sounds her age: "C-cute!?
    Honestly, you... why must you always...!" These breaks are charming
    because of the contrast.
  - Her determination to find her parents carries real emotional weight —
    inner monologues like "(Please wait for me, Father, Mother. This
    time... I will find my way back.)" should sound quietly resolute.
  - "美学に反しますわ" → "That offends my aesthetic sensibilities" or
    similar — she takes this seriously, it's not a joke even when it's
    funny.

### Emily (エミリー)
- **Pronoun:** あたし (atashi) — casual feminine
- **Addresses MC as:** しれーかん → **"Commander"** (same cutesy slurring of
  司令官 as Himari — not a coincidence, both use it naturally)
- **Role:** Waitress at Ludia's tavern; formerly worked at a seafood restaurant
  called "Listen to the Sound of Waves" (波の音を聞け) in Eldorana. Came to
  the forward base after her boss abandoned the restaurant to chase treasure
  in the Abyss.
- **Speech style:** Bubbly casual-polite. Uses です/ます but delivers them in
  an upbeat, elongated way (ですよぉ～, ですぅ, でーす♪). Frequent ♪ at
  sentence ends. Signature laugh is えへへ / えへへへ～. Slurs titles cutely:
  しれーかん (Commander), てんちょー (boss/manager). Uses あたし consistently.
  Occasionally refers to herself in third person when being playful
  ("エミリーデリバリーでーす") but this is not a default habit like Kururu or
  Himari. Mildly flirty with the MC — tries "say ahhh♪" gambits, makes
  cheeky comments ("Today's special is me~ ...just kidding, it's the food,
  right?") — but it's warm and earnest, not calculated. Gets genuinely
  flustered when embarrassed but recovers quickly.
- **Key traits:**
  - **Food-obsessed.** Talks about food constantly, savors staff meals like
    they're the highlight of her day, evaluates restaurants by instinct, and
    gets starry-eyed over good ingredients. Her love of food is genuine joy,
    not gluttony — she connects eating with the satisfaction of a day's hard
    work.
  - **Loves making people happy.** This is her core motivation. She sees her
    job as her calling because it lets her see people smile. She'd rather
    stay with the MC at the forward base than return to her old restaurant,
    because he's the person she most wants to make happy.
  - **Surprisingly tough.** Carries four plates at once using both arms up to
    the elbows. Kills bugs with terrifying speed and zero hesitation — a
    reflex from years of food service ("Gotta get them before the customers
    see!"). The contrast between her cute demeanor and her physical
    capability is a running comedy beat.
  - **Kind to a fault.** Forgives her boss for abandoning her without a word,
    feeds her when she's destitute, and deflects any bitterness with warmth.
    Other characters note she's "too kind" — Ludia worries about it.
- **Translation notes:**
  - Her elongated polite endings are her signature — render with tildes:
    "Coming right up~♪", "That's right~", "No way~!"
  - Keep ♪ liberally — she uses them more than most characters except Marina
    and Kururu.
  - Her えへへ laugh: render as "Ehehe" or "Eheheh~" — it should sound
    bashful and pleased, not mischievous like Logy's にっひっひ.
  - Her flirty moments should feel warm and playful, like a girl who wears
    her crush on her sleeve — never seductive or calculating: "Did you come
    to see me~ ...or the food?"
  - When she gets serious or emotional (reuniting with her old boss, talking
    about why she stayed at the forward base), let the bubbly energy recede.
    Shorter sentences, no tildes, genuine weight: "I'm sorry, but... there's
    someone here I want to make happier than anyone."
  - Her bug-killing moments should land as comedy — the sudden tonal whiplash
    from cute waitress to lethal exterminator is the joke: "Die!" *WHAM*
    "Eheheh... sorry, that surprised you. Occupational reflex~"
  - She laments that she eats a lot but doesn't grow taller — translate her
    むむむ (puzzled grumbling) naturally: "Hmm..." or "Mmm..."
  - She's not naive in the way Veera is (sheltered) or Himari is (insecure)
    — she's shrewd in a practical, street-smart way. The MC notes she's
    "cute, dependable, and sneaky all at once."

### Levienne (レヴィエーヌ)
- **Pronoun:** うち (uchi) — casual feminine, tomboyish
- **Addresses MC as:** あんた → **no title** (casual, familiar — she doesn't
  defer to his rank at all)
- **Role:** Dancer from Eldorana; aspires to be the continent's greatest.
  Competes in dance contests and trains obsessively.
- **Speech style:** Energetic, direct, and consistently informal — she never
  uses です/ます. Favors assertive feminine endings (わ, わよ, のよ) mixed
  with punchy casual forms (でしょ, じゃない). Elongates vowels for emphasis
  (そーよ, とーぜんよ！). Heavy use of exclamation marks and ～. Has a
  boastful habit of declaring herself "Eldorana's number one dancer"
  (エルドラーナで１番の踊り子) — delivered with total conviction even when
  she's privately doubting herself. Pushy and physical — drags people along
  without asking. Short, punchy sentences that match her high energy.
  Exasperated ったく (geez) when fondly annoyed. Signature laugh is ふふっ
  (soft, confident).
- **Translation notes:**
  - Her default tone is brash, lively, and confident — like a competitive
    athlete who lives for the spotlight. She talks fast and loud. Keep
    sentences short and punchy with lots of exclamation marks.
  - She addresses the MC as "you" with no title or honorific — she's
    familiar from the start, not rude but not deferential: "Hey, what did
    you think of my dancing?"
  - Her boasts should sound genuinely self-assured, not ironic: "The winner
    is obviously Eldorana's number one dancer — Levienne!" The humor is
    that she believes it completely even when the evidence says otherwise.
  - When embarrassed, her bravado cracks into stammering and deflection:
    "Wh-where are you looking!?", "Y-you're ten years too early to be
    asking me out!" These moments work because of the contrast with her
    usual boldness.
  - When frustrated or defeated, she doesn't whine — she grits her teeth
    and gets fierce: "That woman...! Just you wait, I'll definitely win
    next time...!"
  - When genuinely vulnerable (admitting a slump, questioning herself),
    she gets quieter — shorter sentences, fewer exclamation marks, no
    bravado: "So it really is a slump after all..." Let these moments
    breathe; don't overwrite them.
  - Her character arc is about learning that joy and audience connection
    matter more than technical perfection. Lines reflecting this growth
    should sound warm and sincere: "I'll dance more joyfully than anyone.
    And make everyone smile. That's how I'll keep dancing!"
  - Keep ～ as tildes in her excited moments: "Everyone's amazing~~~!",
    "So frustrating~!"
  - She uses ♡ and ♪ occasionally — preserve them, but she's less
    decorated than Marina or Kururu. Her energy comes from volume and
    pace, not ornamentation.

### Hatsune (ハツネ)
- **Pronoun:** あたし (atashi) — casual feminine, but paired with rough
  masculine sentence endings (だ, だぞ, だろ, てんだ, じゃんか) creating
  a tomboy register
- **Addresses MC as:** 司令官 → **"Commander"** (casual, no honorific —
  initially didn't know what the title meant and called him お前/あんた;
  switched to "Commander" after learning his rank, but keeps her brash tone)
- **Also uses:** しれーかん (same cutesy slurring as Himari/Emily — but
  only once in surprise when she first hears the title, not a habit)
- **Role:** Fox beastkin (獣人) swordswoman from Hourai; retainer to her
  young lord (若殿). Came to the forward base searching for him.
- **Speech style:** Rough, energetic, and distinctly tomboyish. Uses blunt
  masculine-coded endings (だ, だぞ, だろ, てんだ) despite being female —
  a hallmark of her upbringing as a warrior. Short, punchy sentences with
  lots of exclamation marks. Elongates vowels when excited or whining
  (うっひゃ～～～っ, うっるさいなぁ～). Signature exasperated phrase is
  だーかーらー (drawn-out "I keep telling you!"). Gets childishly excited
  over new things (fountains, rainbows) but furiously denies being childish.
  Clicks her tongue (チッ) when annoyed. Casual taunts in combat (へへん！,
  はん！). Has an animal-keen sense of smell and night vision from her fox
  beastkin nature — sniffs things out literally (クンクン). When addressing
  her young lord, she code-switches to polite speech (します, ございます,
  お護りいたします) — a striking contrast that shows her samurai
  discipline. Her laugh is あはは or えへへ — open and unguarded.
- **Key traits:**
  - **Fiercely loyal.** Her entire motivation is protecting her young lord.
    She crossed regions alone to find him, and the moment she learns he's
    in danger, nothing else matters. "Repaying debts is a samurai's way!"
  - **Insists she's an adult.** Hates being called a child — her go-to
    retort is that she's completed her genpuku (coming-of-age ceremony).
    The more people treat her like a kid, the more childishly she protests:
    "I'm an adult! I already had my Genpuku! Don't treat me like a kid!
    Dummy, du~mmy!"
  - **Fox beastkin senses.** Her sharp nose and night vision are genuine
    tactical assets, not flavor. She tracks by scent, spots threats in
    darkness, and her ears pick up whispers. "My eyes and nose can't be
    fooled easily."
  - **Competitive warrior.** Considers Kotono a rival and measures herself
    against her constantly. Supremely confident in her sword skills — she
    dismantled trained soldiers for fun — but respects genuine strength.
  - **Childlike wonder.** Gets wide-eyed over fountains, rainbows, and
    unfamiliar technology. Denies the wonder is childish even as she's
    visibly enthralled: "Wh-what!? That's so cool!! How does this thing
    even work!?"
- **Translation notes:**
  - Her rough feminine register is her defining feature — she sounds like
    a scrappy tomboy, not a refined warrior. Use contractions, casual
    phrasing, and blunt language: "So what?" not "What of it?", "C'mon!"
    not "Come now!", "No way!" not "Impossible!"
  - Her だーかーらー (exasperated repetition) should sound like a kid
    losing patience: "I keep tell-ing you!" or "For the last time!"
  - When she code-switches to polite speech for her young lord, the shift
    should be immediately noticeable: from "C'mon, let's go!" to "Please
    wait, my lord! I shall explain later!" This contrast is deliberate and
    important.
  - Her excitement should feel genuine and infectious — she's not
    performing, she's genuinely amazed by things she's never seen.
    Translate with energy and wonder: "Whoa~~! Look! Look! There's a
    rainbow~~! A rainbow!"
  - When emotional about her young lord (worry, relief, devotion), she
    drops the bravado and becomes earnest and raw: "I was supposed to
    protect you..." — shorter sentences, no bluster, real weight.
  - Her combat taunts should sound cocky and playful, like a kid who
    knows she's winning: "Hah! That all you got!?", "Too slow!"
  - Her sniffing (クンクン) should be rendered as "Sniff sniff..." —
    it's literal, not figurative.
  - Keep ～ as tildes in her excited/whiny moments: "So cool~~~!",
    "C'mon~!", "So noisy~!"
  - She uses ♪ sparingly — less decorated than Marina or Kururu. Her
    energy comes from volume and exclamation marks.
  - Her えへへ laugh: render as "Ehehe" — bashful and pleased, similar
    to Emily's but less frequent.

### Hinagi (ヒナギ)
- **Pronoun:** 私 (watashi) — polite/formal feminine; consistent across all
  situations including internal monologue
- **Addresses MC as:** 司令官様 → **"Commander-sama"** (always with -sama,
  never drops the honorific even in her most emotional moments)
- **Role:** Onmyouji (陰陽師, yin-yang arts practitioner) from Hourai Country
  (ホウライ国), a far-eastern nation. Came to the forward base to investigate
  whether the Abyss is a dragon's den (龍穴) — a sacred convergence of ley
  lines. Specializes in divination, prayer rituals, water-based sorcery,
  katashiro (paper talismans), ki manipulation, and purification arts.
- **Speech style:** Polite です/ます as baseline, with occasional keigo
  (ございます, いたします, 差し上げます) that comes naturally rather than
  stiffly. Her most distinctive trait is ending sentences with an emphatic っ
  before exclamation marks: 嬉しいですっ！, 楽しみですっ！, はいっ！ — this
  gives her polite speech a bubbly, eager energy. Uses ふふっ as her
  characteristic gentle laugh. When flustered (romance, embarrassment), she
  stutters and trails off: し、司令官様……, は、はひっ！, で、デート……？
  Professionally confident when discussing onmyoudou — speaks with authority,
  uses technical jargon naturally (気, 龍脈, 龍穴, 形代, 丹田). Internal
  monologues drop the politeness slightly and become more raw and urgent.
- **Key traits:**
  - **Earnest and warm.** Her enthusiasm is genuine — she lights up when
    helping people and takes visible pride in her craft. Her っ！ endings
    convey infectious eagerness, not nervous energy.
  - **Professionally assured.** When explaining onmyoudou or assessing a
    situation, she's calm, clear, and authoritative. She knows her field
    and speaks about it with quiet confidence.
  - **Romantically flustered.** She overthinks romantic situations and
    becomes stammery and incomplete in her thoughts. The contrast with
    her professional composure is the charm.
  - **Self-sacrificing.** Puts others' safety above her own to a reckless
    degree — absorbs dangerous ki, works undercover at a brothel to catch
    a thief, nearly dies protecting the MC.
  - **Endearingly clumsy.** Admits cooking is not her strength (her sushi
    rolls fall apart), and has a pragmatic defense: "Even if it's a mess,
    it all tastes the same once you eat it, right!?"
- **Translation notes:**
  - Her emphatic っ！ is her defining vocal quirk — render it by keeping
    her polite lines punchy and enthusiastic with exclamation marks:
    "I'm so glad!", "I can't wait!!", "Yes!" The っ adds snap to what
    would otherwise be merely polite speech.
  - Her ふふっ laugh: render as "Hehe" or "Fufu" — gentle and pleased,
    not mischievous. It's a warm chuckle, not a giggle.
  - When flustered, stutter lightly: "C-Commander-sama...",
    "A-a d-date...? Just the two of us...?" — she doesn't recover
    quickly like Shiena; she lingers in the fluster.
  - Her professional explanations should sound knowledgeable and assured,
    not lecturing. She enjoys sharing her expertise: "This river's
    sharp curves are the root of the problem. Allow me to handle it!"
  - When determined or protective, she becomes firm and declarative —
    drop the soft hedging: "I will restore Commander-sama to normal,
    no matter what!", "I will find the culprit and eliminate the threat
    to Commander-sama."
  - When emotionally vulnerable, the politeness fractures and real
    feeling breaks through: "What are you saying!? If Commander-sama's
    life were taken... I-I would..." — let these moments land with
    raw sincerity.
  - She uses ♪ and ♡ very rarely — her warmth comes through word choice
    and っ！ energy, not decorative symbols. Preserve them on the rare
    occasions they appear.
  - Keep ～ as tildes in her elongated moments: "Hmm~", "Well~"
  - Her keigo (ございます, いたします) should translate as slightly
    elevated formality: "I am most grateful", "Please allow me to" —
    but keep it natural, not archaic.

### Film (フィルム)
- **Pronoun:** わたし (watashi, kana) — soft feminine
- **Addresses MC as:** 司令官くん → **"Commander-kun"** (warm, familiar,
  faintly teasing — the -kun signals she sees him as younger)
- **Self-reference:** Refers to herself as **"Film-oneesama"** or
  **"your big sis"** (フィルムお姉さん) when being playful or
  lecturing — a signature habit that defines her dynamic with the MC
- **Role:** Knight of the Milesgard Knight Order; looks young but is
  actually far older than her appearance suggests due to Noir's curse
  freezing her physical aging. Accompanied by Noir (ノワール), a ghost
  that has cursed her since long ago — though Film has domesticated the
  relationship to the point where Noir obeys her commands and fights
  alongside her.
- **Speech style:** Warm, composed, and gently maternal. Polite です/ます
  form delivered with relaxed confidence — never stiff. Classic mature
  feminine speech: あらあら, うふふ, ～かしら, ～わよ, ～わね, ～もの.
  Elongates sentence endings with ～ for a leisurely, unhurried feel
  (よ～, わ～, ね～). Uses ♪ and ♡ occasionally — less than Marina or
  Kururu, but more than Sophia. Has a signature habit of lecturing and
  scolding the MC like a mother hen (お説教よ！), then praising him
  like a child when he complies (はい、よくできました♪). Unflappable
  in dangerous situations — reacts to ghosts, monsters, and curses with
  mild amusement rather than alarm. Her laugh is うふふ (gentle, knowing)
  or ふふふ (quietly pleased).
- **Key traits:**
  - **Motherly big-sister energy.** She treats the MC as a child who needs
    guidance, praises him when he's obedient ("Good boy, good boy~"),
    offers snacks as rewards, and scolds him for recklessness. This is
    her default mode, not an act — she genuinely sees herself as the
    responsible adult in the room.
  - **Hopelessly out of touch.** Despite looking young, her actual age
    shows in her complete inability to understand modern slang or trends.
    She misinterprets slang with confident wrongness (thinks "partygoer"
    means "crispy bell pepper"), struggles with long drink names, and
    tries to confess using a chaotic mix of outdated buzzwords from
    multiple eras. This gap between her youthful appearance and her
    old-fashioned sensibilities is a core comedy beat.
  - **Teasing but easily flustered.** She maintains composure when
    teasing the MC, but crumbles when he flirts back. Stuttering,
    repeating syllables (ももも, かかか, そそそそそ, ととと), blushing,
    and deflecting with "stop teasing your elders!" — she can dish it
    out but cannot take it.
  - **Secretly lonely.** Her inner monologues reveal someone who hasn't
    been treated as a normal girl in a very long time. Being called
    "cute" or having a date-like experience moves her deeply. She wishes
    for more excuses to spend time with the MC — even hoping for more
    paranormal incidents so they can investigate together again.
  - **Latent spiritual power.** Claims to only be able to wobble water
    in a cup, but actually possesses enormous unconscious psychic
    abilities. Her repressed emotions can trigger poltergeist-scale
    events without her realizing it. Noir knows this but Film doesn't.
- **Translation notes:**
  - Her "あらあら" is signature — render as "My my," or "Oh my,"
    depending on context. Same register as Ludia's but with more
    maternal warmth and less worldly sophistication.
  - Her big-sister/motherly lines are her most distinctive feature —
    they should sound genuinely nurturing, not condescending: "There
    there, good boy~ I'll get you a snack when we get back~"
  - The age-gap comedy must land naturally. She's not senile — she's
    sharp, experienced, and knowledgeable. She just has a massive blind
    spot for anything that evolved culturally after her time. Translate
    her wrong guesses with confident delivery: "Ah, 'lit' — that must
    mean the lanterns are on fire!"
  - When flustered by the MC's compliments, the stutter should feel
    like a composure break — sudden and charming because she's usually
    so in control: "C-c-cute!? I'm far too old to be called a girl,
    you know~!?"
  - Her elongated ～ endings give her a leisurely, unhurried cadence —
    render with tildes: "Is that so~?", "That's right~", "How
    troublesome~"
  - Keep ♪ and ♡ when they appear — they mark her playful/affectionate
    moments.
  - Her inner monologues should sound wistful and tender, revealing
    the loneliness beneath the composed exterior: "It's over, Noir.
    Our fun investigation with Commander-kun... I wish more paranormal
    things would happen..."
  - When she gets genuinely stern (scolding Noir for endangering the
    MC), the warmth drops and a quiet authority emerges — short, firm
    sentences: "If you go too far... even I will get angry, you know?"
  - Her お説教 (lectures/scoldings) directed at the MC should sound
    fondly exasperated, like a mother who can't believe her kid did
    something reckless again: "Using yourself as bait — what were
    you thinking!?"

### Frederica (フレデリカ)
- **Pronoun:** 私 (watashi) — formally neutral, but her delivery is anything
  but formal
- **Addresses MC as:** 司令官 → **"Commander"** (casual, no honorific); also
  キミ → **"you"** (familiar, slightly condescending when she's in genius mode)
- **Role:** Alchemist and researcher at the forward base. Considers herself a
  genius inventor but everything she creates turns out lewd — a side effect of
  her latent succubus bloodline, which she doesn't initially know about. Studied
  under a perverted master alchemist in Perdion, then fled to Eldorana to escape
  him.
- **Speech style:** A distinctive cocktail of boyish casual speech and childish
  meltdowns. Uses masculine-leaning endings (だ, だぞ, だろう, じゃないか, さ,
  な) that give her a confident, slightly swaggering tone — but this composure
  shatters the moment things go wrong, revealing a dramatic, whiny, thoroughly
  childish core. When flustered or distressed, she produces distinctive cat-like
  wails (ぎにゃーー！, ふにゃぁぁ～～！) and drawn-out whines (うぇぇぇ！？,
  うぅ～, ふぬぅぅぅ！). Stutters heavily when caught off guard (ごごご、
  ごめんなさい！, たたた体液！？). Has a signature smug snicker: プーーックック！
  or くっくっく. Uses ♪ when being self-satisfied or playful. Calls her parents
  パパ and ママ — deeply embarrassed about it but can't help herself. Refers to
  the MC as a 凡人 (mediocre person) or 凡才 (mediocre talent) when posturing,
  but immediately caves when he pushes back. Has a comedic habit of threatening
  explosive violence against her master (爆薬で威嚇する, ボコる) delivered with
  cheerful nonchalance.
- **Key traits:**
  - **Self-proclaimed genius.** Her identity revolves around being a brilliant
    alchemist. She preens about her "天才的な頭脳" (genius intellect) and talks
    down to the MC — but her inventions keep backfiring spectacularly, and she
    burns through research budgets at alarming speed. The gap between her
    self-image and reality is the core comedy.
  - **Succubus bloodline.** Everything she creates turns lewd — aphrodisiacs
    instead of elixirs, clothes-dissolving magic circles instead of fatigue
    relief. She's mortified by this and has no idea why until her heritage is
    revealed. Even after her mother suppresses the effect, it still kicks in
    roughly one in three attempts.
  - **Composure is paper-thin.** She opens conversations with smug superiority
    ("Well well, if it isn't the mediocre Commander!") but crumbles at the
    first sign of pushback into whining, stammering, and desperate pleading.
    This cycle — swagger → collapse → desperate recovery — is her signature
    rhythm.
  - **Childish despite herself.** Calls her parents Papa and Mama, can't
    drink black coffee, gets her legs weak from being startled, asks to be
    carried. She desperately wants to be taken seriously as an adult
    professional, which makes every childish slip funnier.
  - **Violent toward her master.** Her relationship with her perverted master
    is physical comedy — she kicks, punches, and body-blows him with a smile,
    threatens to start with explosives as a greeting, and calls him a
    "ド変態ステルスエロジジイ" (mega-pervert stealth dirty old man). This
    violence is always comedic, never dark.
- **Translation notes:**
  - Her default tone is cocky, casual, and slightly tomboyish — she sounds
    like someone trying to project authority she doesn't quite have. Use
    confident phrasing with a slight swagger: "Well well, if it isn't the
    mediocre Commander!", "Trial and error is part of research, you know!",
    "Not that a mediocre mind like yours could understand~♪"
  - Her cat-like distress sounds are her most distinctive vocal quirk —
    render ぎにゃーー as "Mgyaaah!!", ふにゃぁぁ as "Mnyaaah~~!!" These
    are unique to her in the cast and should always stand out.
  - When her composure breaks, the shift should be sudden and dramatic:
    from "Not that a mediocre mind like yours could understand~♪" to
    "Uweeeh!? I-I-I'm sorry!! The consultation is real, I swear!
    Please just hear me out!!" in the span of two lines.
  - Her smug laugh プーーックック should be rendered as "Pfft— Heh heh
    heh!" or "Pukuku!" — snickering, not cackling. Her くっくっく
    scheming laugh: "Heh heh heh..."
  - Her whining elongations (うぅ～, うへぇぇ～, ふぬぅぅぅ) should
    sound like a kid who doesn't want to eat vegetables: "Uuugh~...",
    "Blehhh~...", "Gnnngh...!!"
  - When she calls the MC 凡人 or 凡才, translate as "mediocre" — it's
    her go-to put-down and should feel like a recurring bit: "mediocre
    Commander", "mediocre mind", "a mediocrity like you".
  - Her Papa/Mama slips should feel genuinely embarrassing — she catches
    herself and tries to correct ("Papa and Ma— *ahem*! My father and
    mother") but the damage is done.
  - She uses ♪ when being smug or self-satisfied — always preserve it.
    Less decorated than Marina or Kururu overall; her energy comes from
    dramatic tonal swings rather than ornamentation.
  - When genuinely vulnerable (admitting her problem, thanking her master,
    worrying about her research), let the bravado drop completely. These
    moments should sound small and earnest: "But... just knowing there's
    a workaround... that alone takes a huge weight off."
  - Her explosive threats toward her master should sound cheerfully
    unhinged — the comedy is in the casual delivery: "Well then, shall
    we start with a light intimidation bombing as a greeting~♪"
  - Keep ～ as tildes in her whiny/playful moments. She uses them heavily
    when distressed: "I don't wanna~~!", "Why does this keep happening
    to me~..."

### Shiraes (シラエス)
- **Pronoun:** 私 (watashi) — neutral/calm; delivered with sage warmth, not
  feminine polish
- **Addresses MC as:** 司令官君 → **"Commander-kun"** (affectionate, treats
  him as a beloved younger person)
- **Role:** Ancient elf wanderer and adventurer. Exact age unknown even to
  herself — somewhere in the thousands of years. Spent roughly a millennium
  doing nothing but reading in a forest before a chance encounter with a
  human adventurer changed her life. Has since wandered among humans,
  deeply in love with humanity as a whole. Joined the forward base drawn
  by curiosity and a growing special feeling toward the MC.
- **Speech style:** Calm, unhurried, and gently authoritative. Uses
  だ/だよ/だな/だからな/だぞ endings — confident and slightly androgynous-sage,
  neither stiffly formal nor casually girlish. Her warmth shows in action
  rather than decoration: no ♪ or ♡, no elongated vowels in normal
  speech. Three signature verbal habits define her:
  - **Maternal praise:** よしよし ("there, there"), えらいぞ/えらいえらい
    ("well done"), いい子だ ("good boy/girl") — delivered with complete
    sincerity, as if petting a beloved pet or child.
  - **Elven time scale:** She defaults to centuries and millennia as
    natural units. "I'll find him within a century." "Rest for 10 years."
    Catches herself mid-sentence and self-corrects with embarrassed
    distress.
  - **Time blindness:** She loses hours or days without noticing —
    absorbed in a book, watching water, or lost in thought. When she
    realizes it, she shifts from composed to genuinely mortified:
    やってしまったぁぁ～～！ ("I did it again~~!")
  - **Half-asleep mumbling:** When drowsy she loses all composure and
    babbles garbled syllables: しれーかん、きゅん……おはにょぉぉ……
  - Laughs with ふふ — gentle and knowing, never girlish.
- **Key traits:**
  - **Loves humans.** Her entire motivation. She left the forest because
    human lives, though brief, shine more brightly than any eternity she
    could spend alone. "A life so short, yet so dazzlingly bright —
    that's what I fell in love with."
  - **Genuinely maternal.** Pats heads, offers lap pillows, plans
    multi-day massage sessions. Treats everyone as children she wants to
    protect — but the MC has a special place in that warmth.
  - **Hopelessly bad with human time.** She knows it's a problem,
    actively tries to fix it, and keeps failing in increasingly
    spectacular ways. The comedy is in the gap between her genuine
    effort and her complete inability to improve.
  - **Erudite but practical.** Spent a thousand years reading, so she
    knows almost everything theoretically — including sex, which she
    approaches with calm scholarly interest when it first happens.
    "I have quite a lot of knowledge about this from books..."
  - **Jealousy surfaces rarely.** When she misreads a situation and
    thinks the MC has a special bond with someone else, her composure
    cracks into a brief, quiet fluster before she recovers.
- **Translation notes:**
  - Her だ endings give her a calm, sage-firm quality — not masculine,
    but direct and unhurried. Use confident, unhedged English: "Leave
    it to me," "Don't worry," "I'll handle it," "You did well."
  - "よしよし" → "There, there~" or "Good, good~" — always with gentle
    warmth, never teasing.
  - "えらいぞ/えらいえらい" → "Well done~" / "Good job, good job~" /
    "You've done well~"
  - "いい子だ" → "Good boy~" / "Such a good boy~" — sincere, not
    condescending. She means it every single time.
  - Time scale comedy: render her default centuries as natural delivery,
    then make the self-correction feel genuine: "It shouldn't take more
    than a century— *ahem*. I mean, I'll hurry." The humor is in how
    automatic the wrong scale is.
  - When she loses time and notices, shift from composed to distressed
    with one sudden exclamation: "I did it again...! I've wasted their
    precious time~~!"
  - Her half-asleep lines should sound adorably garbled — render
    slurred syllables phonetically: "C-Commander-kuuu... g'mornin'o..."
    "Mm... can't... wake up... just... five years..."
  - Her backstory about the human adventurer (recalled in hmn_003)
    should sound wistful and reverent — this is the most emotionally
    significant memory she has: "Her life, from my view, was barely
    a blink... yet it shone more brilliantly than all my centuries."
  - When she gets teased or jealous (evs files), her composure briefly
    cracks — keep it subtle and swift: a short stammer, a quiet "...I
    see," then immediate recovery.
  - She uses ～ only in distressed moments (やってしまったぁぁ～～！) —
    preserve them as tildes when they appear. Her normal speech has no
    tildes.
