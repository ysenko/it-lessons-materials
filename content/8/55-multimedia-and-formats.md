---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 55
style: |
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  .grid-item {
    border: 1px solid #eee;
    padding: 15px;
    border-radius: 5px;
    background-color: #fafafa;
  }
  .text-left {
    text-align: left;
    padding: 5px;
  }
  .image-center {
    max-width: 100%;
    height: auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .text-large {
    font-size: 40px;
  }
  .text-medium {
    font-size: 30px;
  }
  .text-medium-small {
    font-size: 25px;
  }
  .text-small {
    font-size: 18px;
  }
  .text-tiny {
    font-size: 14px;
  }
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    background-color: #f9f9f9;
  }
  .important-to-remember {
    background-color: #fff3cd;
    border-left: 6px solid #ffecb5;
    padding: 15px;
    margin: 15px 0;
  }
  .borderless {
    border: 0px;
  }
  .task {
    background-color: #e3f2fd;
    border-left: 5px solid #2196f3;
    padding: 15px;
    border-radius: 8px;
  }
  .emoji-large {
    font-size: 3em;
    text-align: center;
    display: block;
  }

---

# 🎬 Поняття мультимедіа. Формати аудіо- та відеофайлів

## 🏫 Урок **55**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке мультимедіа та які бувають його види
- 🔧 Яке ПЗ використовують для роботи зі звуком і відео
- 🎵 Чим відрізняються формати аудіофайлів
- 🎬 Що таке контейнер і кодек у відеофайлах

---

## 🤔 Запитання для роздумів

<section class="grid-container">
<div class="text-left text-medium-small">

Чому те саме відео на YouTube важить **200 МБ**...

...а без стиснення — **понад 12 ГБ**?

🔍 Відповідь — у сьогоднішній темі!

</div>
<div class="image-center text-large">

🎬 ÷ 60 = 🗜️

</div>
</section>

---

## 🎵 Цікавий факт

<section class="card">

**Народження MP3**

Формат MP3 розробили вчені Інституту Фраунгофера в Німеччині у **1993 році**.

Перша пісня, офіційно конвертована в MP3, — **«Tom's Diner»** Сюзанни Веги.

Сама співачка дізналася про це лише через кілька років! 😲

</section>

---

## 📺 Що таке мультимедіа?

<section class="card">

**Мультимедіа** — це інтеграція кількох форм подання інформації в єдиному середовищі:

🔤 текст · 🖼️ зображення · 🔊 звук · 🎬 відео · 💫 анімація · 🖱️ інтерактивність

</section>

**Приклади:** відеоуроки, подкасти, комп'ютерні ігри, вебсайти, реклама

---

## 📊 Види мультимедіа

<section class="grid-container">
<div class="card text-left text-medium-small">

**📼 Лінійне**

Користувач **не впливає** на перебіг

- Кінофільм
- Аудіозапис
- Радіотрансляція

</div>
<div class="card text-left text-medium-small">

**🖱️ Нелінійне (інтерактивне)**

Користувач **керує** процесом

- Вебсайти
- Відеоігри
- Освітні застосунки

</div>
</section>

---

## 🛠️ ПЗ для роботи з мультимедіа

<section class="grid-container">
<div class="card text-left text-small">

**🎵 Аудіо**

🆓 Audacity, LMMS
💰 Adobe Audition, GarageBand

</div>
<div class="card text-left text-small">

**🎬 Відео**

🆓 DaVinci Resolve, CapCut
💰 Adobe Premiere Pro, Final Cut
🌐 CapCut Web, Canva

</div>
<div class="card text-left text-small">

**▶️ Програвачі**

🆓 VLC, MPV, MPC-HC

</div>
</section>

<section class="important-to-remember">

💡 **VLC** відтворює майже будь-який формат без додаткових кодеків — і це безкоштовно!

</section>

---

## 🎵 Формати аудіофайлів

<section class="grid-container">
<div class="card text-left text-small">

**📦 Без стиснення**
WAV, AIFF

✅ Ідеальна якість
❌ ~30 МБ на 3 хв

*Студійний запис, відеомонтаж*

</div>
<div class="card text-left text-small">

**💎 Без втрат (lossless)**
FLAC, ALAC

✅ 100% якість
✅ -40–60% розміру

*Аудіофіли, архів*

</div>
<div class="card text-left text-small">

**📱 З втратами (lossy)**
MP3, AAC, OGG

✅ ~3–4 МБ на 3 хв
⚠️ Мінімальні втрати

*Стрімінг, щоденне прослуховування*

</div>
</section>

---

## 🎵 Цікавий факт про FLAC

<section class="card">

**FLAC — це як ZIP для звуку**

Формат FLAC стискає аудіо на **40–60%** без жодних втрат якості.

Це означає: якщо розпакувати FLAC-файл, отримаєш **побітово ідентичний** оригінальний запис.

На відміну від ZIP, FLAC спроєктований спеціально для звуку — тому він ефективніший для аудіоданих. 🎧

</section>

---

## 🎬 Формати відеофайлів: ключове розрізнення

<section class="grid-container">
<div class="card text-left text-small">

**📦 Контейнер**
«Упаковка» файлу

- MP4
- AVI
- MKV
- MOV
- WebM

</div>
<div class="card text-left text-small">

**⚙️ Кодек**
Алгоритм стиснення

- H.264
- H.265 / HEVC
- VP9
- AV1

</div>
</section>

<section class="important-to-remember text-medium-small">

⚠️ MP4 — це контейнер, а H.264 — кодек. Одне без одного не існує!

</section>

---

## 🎬 Який формат для чого?

<section class="grid-container">
<div class="text-left text-small">

| Формат | Призначення |
|--------|-------------|
| **MP4** (H.264) | Веб, соцмережі, YouTube |
| **MKV** | Архів фільмів, кілька доріжок |
| **WebM** (VP9/AV1) | Вбудоване відео на сайтах |
| **MOV** | Монтаж на Apple-пристроях |

</div>
<div class="card text-left text-small">

**Порада:**

Знімаєте на смартфон → зберігайте в **MP4**

Архівуєте фільмотеку → використовуйте **MKV**

Публікуєте в TikTok/Instagram → конвертуйте в **MP4**

</div>
</section>

---

## 🎬 Цікавий факт про H.265

<section class="card">

**Магія H.265 (HEVC)**

Кодек H.265 стискає відео **вдвічі ефективніше** за H.264 при тій самій якості.

Саме завдяки H.265 стрімінг **4K-відео** став доступним на звичайних смартфонах і домашньому інтернеті.

📡 Щохвилини на YouTube завантажується понад **500 годин** відео — уявляєш, скільки місця заощаджує стиснення?

</section>

---

<section class="task">

## ⌨️ Практичне завдання

<div class="text-medium">

**Досліджуємо медіафайли у VLC**

1. Відкрий VLC → відкрий будь-який **<a href="https://drive.google.com/file/d/1s5NhK0By-XqalGc6jQ2hKqeSkVs4a_bh/view?usp=sharing" target="_blank">аудіофайл</a>**
2. **Інструменти → Інформація про медіа** (Ctrl+I)
3. Запиши: кодек (codec), частоту дискретизації (sample rate), бітрейт (bitrate)
4. Повтори для **<a href="https://drive.google.com/file/d/1qAj-mfW6y3ilqEW3dXl1qsB0PMsP_n92/view?usp=sharing" target="_blank">відеофайлу</a>** — додай роздільну здатність (video resolution) та fps

🌐 *Немає VLC?* → [mediainfo.js.org](https://mediainfo.js.org/demo/)

</div>
</section>

---

## 🤔 Підсумуємо

- Яка різниця між **MP3** та **FLAC**?
- Чому **MP4** і **H.264** — це не одне й те саме?
- У якому форматі зберегти відео для **TikTok**?
- А для **домашнього архіву**?

---

## 🏠 Домашнє завдання

📖 Опрацюй відповідний параграф підручника с. 207-211
