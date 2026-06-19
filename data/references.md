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
| あたし (atashi) | Casual feminine | Belisa |
| アタシ (atashi, katakana) | Brash/quirky feminine | Logy, Girl with Glasses |
| ワタシ (watashi, katakana) | Detached/artificial | Aura |
| 僕 (boku) | Soft masculine/boyish | — |
| わし (washi) | Elderly/archaic | Kururu (childish ironic use) |
| 我 (ware) | Grandiose/archaic | Used in dramatic or battle contexts |

### Formatting Conventions

- **No ASCII commas** in translated text. Use fullwidth `，` instead (the game
  script parser splits on ASCII commas and an unescaped comma will corrupt the
  entire line).
- Preserve special tokens: `<user>`, `<br>`, `<size=N>...</size>`.
- Preserve symbols: `♪`, `♥`, `♡`, `～`, etc.

### Line Length Limits

- Dialogue lines for `message`, `dotmessage`, `l2dmessage`, and
  `messageTextUnder` must fit within **73 characters per line**, max **2 lines**
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
| ーー (long dash) | -- (double hyphen) | それはーー → "That was--" |
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
| Tresria | トレスリア | Region name |
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
| エミリー | Emily | Female | |
| エメルダ | Emeralda | Female | |
| エルミア | Elmia | Female | |
| エレクトラ | Electra | Female | |
| カーラ | Carla | Female | |
| クルル | Kururu | Female | |
| クロエ | Chloe | Female | |
| シェリル | Cheryl | Female | |
| シャオレイ | Xiaolei | Female | |
| シャノン | Shannon | Female | |
| シルヴィア | Sylvia | Female | |
| ジェンマ | Gemma | Female | |
| スティーラ | Stila | Female | |
| セレスト | Celeste | Female | |
| ソフィア | Sophia | Female | |
| ダリア | Dahlia | Female | |
| テルー | Teru | Female | |
| ニナ | Nina | Female | |
| ノエミ | Noemi | Female | |
| ハツネ | Hatsune | Female | |
| ヒナギ | Hinagi | Female | |
| ヒマリ | Himari | Female | |
| ヒュメナ | Humena | Female | |
| ピコ | Pico | Female | |
| フィルム | Film | Female | |
| フェイリン | Feilin | Female | |
| フレイヤ | Freya | Female | |
| フレデリカ | Frederica | Female | |
| ヘイリー | Hailey | Female | |
| ベティ | Betty | Female | |
| ホノカ | Honoka | Female | |
| マニョリア | Magnolia | Female | |
| マリナ | Marina | Female | |
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
| ヴィーラ | Veera | Female | |

### Non-Playable / Supporting Characters

| Japanese | English | Gender | Notes |
|----------|---------|--------|-------|
| ロジー | Logy | Female | Self-proclaimed genius scientist |
| ゴレイヌ | Goleinu | Male | Logy's robot assistant |
| アリシア | Alicia | Female | Base administrator |
| アーデルハイト | Adelheid | Female | |
| シエナ | Shiena | Female | |
| レイゼリア | Reyzeria | Female | |
| フェリシオーネ | Felicione | Female | |
| アウラ | Aura | Female | |
| ルディア | Ludia | Female | |
| 警備ロボット | Security Robot | — | |
| 女性の声 | Female Voice | — | |
| 男性の声 | Male Voice | — | |
