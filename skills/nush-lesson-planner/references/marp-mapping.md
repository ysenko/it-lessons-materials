# Mapping lesson-plan content to Marp (Gaia) slides

How to turn an approved lesson plan into slides: slide inventory, CSS-class usage, density limits, and Marp-specific gotchas. All slide text is Ukrainian.

## Marp HTML gotcha (read first)

Markdown inside an HTML wrapper renders **only** if there is a blank line after the opening tag and before the closing tag:

```html
<section class="task">

## 🖱️ Практичне завдання
1. Відкрийте програму...

</section>
```

Without the blank lines, the slide shows raw `## 🖱️ Практичне завдання` as literal text. This applies to every `<section>` and `<div>`. Prefer Markdown syntax (`**текст**`, lists, `###`) for all formatting; use HTML only as structural wrappers that carry a CSS class.

## Slide density limits (hard limits — split the slide if exceeded)

Marp slides do not scroll: overflow is silently cut off in the rendered output. Enforce:

- **One `##` heading per slide** (plus the emoji). Never two topics on one slide.
- At default text size: **max 6 one-line bullets** of body content.
- With `text-medium-small`: max ~8 short lines. With `text-small`: max ~12 short lines.
- `grid-container`: **2–4 cards**, each card max **4 short lines**; use `text-small` or `text-tiny` inside cards.
- Numbered task steps: max **5–6 steps per slide**.
- Nesting depth: at most `section > div > div`. No deeper.
- A 45-minute lesson → **12–18 slides** total. If a plan stage doesn't fit one slide, use two; never shrink text below `text-tiny` to force a fit.

## Slide inventory

Cover the plan stages in order. Typical sequence for a combined / new-knowledge lesson:

### 1. Title slide
- `# <emoji> Тема уроку` and `## 🏫 Урок **<номер>**` — nothing else.
- Placeholders in front-matter (`footer:`, `header:`) and on this slide must already be replaced.

### 2. "Сьогодні ми дізнаємося" (lesson goals)
- Heading with `🎯`.
- 3–5 bullets with emoji by kind: `ℹ️` knowledge, `🔧` skills, `✏️` practice.

### 3. Актуалізація / "Пригадаємо попередні уроки"
- Heading with `🔄`.
- Reference the **actual previous lessons** (numbers + topics from the plan), e.g. one `.card` per recent lesson inside a `grid-container`.
- Optionally end with a bridge question (`> 💬 ...`) leading into the new topic.

### 4. Theory slides (one concept per slide)
- `.card` for definitions of new terms.
- `.important-to-remember` for rules, warnings, and key takeaways.
- `.grid-container` for comparing two things or pairing text with an image.
- Facts/statistics slides: `🤯` heading, 3–4 `.card`s, every fact real and dated where relevant.

### 5. Practical work
- Intro slide: `⌨️` or `🖱️` in the heading, `.important-to-remember` block with preparation steps (what to open, whether an account is needed).
- If graded with levels, one slide per level: **🟢 Рівень 1 — Середній / 🟡 Рівень 2 — Достатній / 🔴 Рівень 3 — Високий**, each with numbered steps in a `.task` (or a per-level class appended to the style block) and a short **Критерії** line in `.important-to-remember` + `text-tiny`.
- Levels are cumulative: each starts with "Виконати завдання Рівня N−1".

### 6. Eye relaxation (if computer work ≥ 15 min)
- `## 👁️ Релаксація для очей`, `<span class="emoji-large">😌</span>`, 3–4 short steps in a `.task`.

### 7. Рефлексія
- `🤔` or `🗣️` in the heading; 2–3 discussion questions from the plan as a bullet list.

### 8. Домашнє завдання
- `## 🏠 Домашнє завдання` with an **Обов'язкове:** part and a **За бажанням:** part.

## CSS classes (from `templates/gaia_template.md` — use only these; append new ones, never modify existing)

| Class | Use for |
| --- | --- |
| `.card` | Definitions, facts, self-contained info blocks |
| `.important-to-remember` | Rules, warnings, criteria, key points (yellow) |
| `.task` | Practical/step-by-step instructions (blue) |
| `.grid-container` | Side-by-side cards, comparisons, text + image |
| `.text-left` | Left-align text inside grid cells |
| `.image-center` | Centering an image inside a grid cell |
| `.text-large` … `.text-tiny` | Font-size steps (40 / 30 / 25 / 18 / 14 px) |
| `.emoji-large` | Single big decorative emoji |
| `.borderless` | Remove border from a grid item |

Grid with text + image:

```html
<section class="grid-container">
<div class="text-left text-medium">

Тут опис завдання або теоретичний текст.

</div>
<div class="image-center">

![w:300px](./assets/<lesson-number>/image.png)

</div>
</section>
```

Images: only reference files that exist in `content/<grade>/assets/<lesson-number>/`. If no suitable image exists, design the slide without one — never point at a nonexistent path.
