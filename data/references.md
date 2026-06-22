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
  never at the cost of meaning.
- **Preserve character voice.** Each character has a distinct way of speaking in
  Japanese (sentence endings, pronoun choice, verbal tics, energy level). The
  English must reflect these differences. A bubbly character should sound bubbly;
  a formal character should sound formal.

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
| 我 (ware) | Grandiose/archaic | Used in dramatic or battle contexts |

### Formatting Conventions

- **Use regular commas** in translation JSON files. The generate script
  (`common._comma_safe()`) automatically converts ASCII commas to fullwidth `，`
  when producing the final `.txt` output. Do not count the space after a comma
  toward the line length limit.
- Preserve special tokens: `<br>`, `<size=N>...</size>`.
- **Do not use `<user>`.** The `<user>` placeholder (player-name substitution)
  crashes the game. When the original Japanese line contains `<user>`, rephrase
  the translation to use "Commander" instead.
- Preserve symbols: `♪`, `♥`, `♡`, `～`, etc.

### Line Length Limits

- Dialogue lines for `message`, `dotmessage`, `l2dmessage`, and
  `messageTextUnder` must fit within **68 characters per line**, max **2 lines**
  (separated by `<br>`).
- `messageTextCenter` and `title` are **exempt** from this limit.
- When a translation is too long, prefer rephrasing concisely over splitting
  into awkward fragments.

### Tone Markers in Japanese and How to Render Them

| Japanese pattern | English rendering | Example |
|-----------------|-------------------|---------|
| ～ (wave dash at end) | ~ (tilde) | そうですかぁ～ → "Is that so~" |
| ♪ | ♪ (keep as-is) | いくよ～♪ → "Here I go~♪" |
| …… (double ellipsis) | ... (single ellipsis) | そうか…… → "I see..." |
| ーー (long dash) | —— (double em dash) | それはーー → "That was——" |
| っ！ (glottal stop + !) | ! (just exclamation) | くそっ！ → "Damn!" |
| 「」 quotes within speech | "double quotes" | 「楽園」→ "paradise" |

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
| クロエ | Chloe | Female | |
| シェリル | Cheryl | Female | |
| シャオレイ | Xiaolei | Female | |
| シャノン | Shannon | Female | |
| シルヴィア | Sylvia | Female | [Profile](#sylvia-シルヴィア) |
| ジェンマ | Gemma | Female | |
| スティーラ | Stila | Female | |
| セレスト | Celeste | Female | |
| ソフィア | Sophia | Female | [Profile](#sophia-ソフィア) |
| ダリア | Dahlia | Female | |
| テルー | Teru | Female | |
| ニナ | Nina | Female | |
| ノエミ | Noemi | Female | |
| ハツネ | Hatsune | Female | |
| ヒナギ | Hinagi | Female | |
| ヒマリ | Himari | Female | [Profile](#himari-ヒマリ) |
| ヒュメナ | Humena | Female | |
| ピコ | Pico | Female | |
| フィルム | Film | Female | |
| フェイリン | Feilin | Female | |
| フレイヤ | Freya | Female | |
| フレデリカ | Frederica | Female | |
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
- **Role:** Isekai'd Japanese high school girl; support/ranged fighter
- **Speech style:** Shy, hesitant, fragmented. Lots of stuttering (う、うん),
  trailing ellipses, unfinished thoughts. Speaks in short bursts rather than
  full sentences. Uses simple, everyday Japanese — no fancy vocabulary or
  formal patterns. References her life in Japan (school, cities, shampoo,
  police) naturally, as someone displaced from a modern world. Deeply insecure
  — calls herself useless, doubts her abilities — but has a quiet inner
  resolve that surfaces in key moments.
- **Translation notes:**
  - **Keep her third-person self-reference:** "Himari wants to help too..."
    "Himari is useless after all..." This is a core character quirk, not
    something to normalize.
  - Stutter and hesitation are part of her voice — preserve them:
    "I-I understand...", "B-but...", trailing "..." at sentence ends.
  - Her speech should feel young and unpolished compared to Sophia or Ludia.
    Simple words, short sentences, no eloquence.
  - When she finds resolve, the shift is subtle — she doesn't suddenly become
    bold. She still stutters, but pushes through: "Himari wants to know too.
    What these people wished for... all of it."
  - Her inner monologues reveal deeper self-doubt than she shows outwardly.
    Translate these with raw honesty: "(Himari really is useless...)"
  - She cares deeply about Shiena and aches to be stronger — these moments
    should sound earnest and pained, not melodramatic.

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
