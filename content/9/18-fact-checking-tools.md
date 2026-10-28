---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 9 клас
header: 🏫 Урок 18
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
    max-width: 100%; /* Ensures the image scales within its space */
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
  .acronym-letter {
    color: #d32f2f;
    font-weight: 900;
  }

---

# Інструменти для виявлення фейків

## 🏫 Урок **18**

---

## 🛡️ Пригадуємо: техніка безпеки

<div class="important-to-remember text-medium-small text-left">

- 🖥️ Сідаємо рівно, відстань до екрана — довжина витягнутої руки.
- 🚫 Без їжі, напоїв та верхнього одягу в кабінеті інформатики.
- 🔌 Не чіпаємо кабелі, роз'єми, задню панель монітора чи системного блока.
- ⚡ Не вмикаємо/вимикаємо комп'ютер самостійно, не відкриваємо системний блок.
- 🔥 Побачили дим, почули незвичний звук або сталася помилка — одразу повідомляємо вчителя.

</div>

---

## 🎯 Сьогодні ми

- 🔎 Опануємо метод швидкої перевірки **SIFT**.
- 🖼️ Навчимося шукати **за зображенням** за допомогою Google Lens і ШІ.
- 🔬 Дізнаємося про метод глибокого розслідування **5W1H**.
- ⌨️ Попрацюємо **медіадетективами**: перевіримо допис і чотири фото.

---

## 🔄 Пригадаймо

<div class="card text-medium-small text-left">

- 🕵️ Що таке **фейк**, **діпфейк**, **маніпуляція**?
- 🐞 Які **«баги» мозку** використовують творці фейків? Наведіть приклад.
- 🚩 Назвіть 3–4 **ознаки фейку**.
- 🧭 Які кроки **алгоритму перевірки** повідомлення ми вивчили?

</div>

---

## 📡 Історія одного фейку

<div class="card text-medium-small text-left">

🦠 2020 рік, початок пандемії COVID-19. У соцмережах поширюються дописи й відео: **вежі зв'язку 5G «викликають коронавірус»**. Хештеги **#5GKills** та **#Stop5G**.

🔥 Наслідки у Великій Британії: люди **підпалювали вежі 5G**, пошкодили зв'язок зі **швидкою допомогою**, нападали на інженерів.

✅ Фейк викрили науковці, фактчекери (**FullFact.org**) та офіційні заяви уряду.

</div>

<div class="important-to-remember text-medium-small text-left">

❓ Як би ви діяли на місці фахівця з кіберзахисту? Що можна було перевірити, **перш ніж поширити** такий допис?

</div>

---

## 🧰 Набір медіадетектива

<div class="important-to-remember text-medium-small text-left">

🪄 Чарівної кнопки «перевірити фейк» **не існує**. Але є методи й інструменти, які перетворюють пасивного читача на **медіадетектива**.

</div>

<div class="grid-container">
<div class="card text-medium-small text-left">

🔎 **SIFT**
«Швидкий сканер» на кожен день

</div>
<div class="card text-medium-small text-left">

🖼️ **Пошук за зображенням**
Звідки це фото?

</div>
<div class="card text-medium-small text-left">

🔬 **5W1H**
«Мікроскоп» для глибокого розслідування

</div>
</div>

---

## 🔎 Метод SIFT

<div class="card text-medium text-left">

✋ <b class="acronym-letter">S</b>top — Зупинись

🕵️ <b class="acronym-letter">I</b>nvestigate the source — Досліди джерело

📰 <b class="acronym-letter">F</b>ind better coverage — Знайди краще висвітлення

🧵 <b class="acronym-letter">T</b>race claims — Простеж до оригіналу

</div>

---

## ✋ S · 🕵️ I

<div class="card text-medium-small text-left">

✋ **Зупинись.** Найголовніший крок! Перш ніж клікати, репостити чи обурюватися — **зроби паузу**. Фейки розраховані на миттєву емоційну реакцію.
❓ *Які емоції викликає в мене цей допис?*

</div>

<div class="card text-medium-small text-left">

🕵️ **Досліди джерело.** Відкрий **нову вкладку** й введи в пошук назву сайту, сторінки чи ім'я автора.
❓ *Це авторитетне ЗМІ з історією чи «сайт-одноденка»? Цей «експерт» справді фахівець у цій темі?*

</div>

---

## 📰 F · 🧵 T

<div class="card text-medium-small text-left">

📰 **Знайди краще висвітлення.** Найпотужніший крок! Що про цю подію пишуть **інші надійні ЗМІ** та **офіційні джерела**?
✅ Пишуть кілька відомих видань — швидше за все, правда.
🚩 Кричить лише один сайт, а всі мовчать — майже напевно **фейк**.

</div>

<div class="card text-medium-small text-left">

🧵 **Простеж до оригіналу.** Знайди **першоджерело** цитати, фото чи відео.
📸 Фото «жахливих руйнувань» може виявитися знімком п'ятирічної давнини з іншої країни.

</div>

---

## 🖼️ Пошук за зображенням: Google Lens

<div class="grid-container">
<div class="card text-medium-small text-left">

❓ **Що це?**
Сервіс Google, який знаходить, **де ще** в інтернеті є це зображення, чи воно **оригінальне** і **що на ньому**.

</div>
<div class="card text-medium-small text-left">

⚙️ **Як працює?**
- 🌐 [images.google.com](https://images.google.com) → 📷 значок камери → завантаж фото.
- 🖱️ Або в Chrome: **правий клік** на фото → пункт пошуку через **Google Lens**.

</div>
</div>

<div class="task text-medium-small text-left">

🔍 Результат: сайти з цим фото, **схожі зображення**, назва об'єкта чи місця. Старі публікації фото допомагають з'ясувати, **коли** воно з'явилося.

</div>

---

## 🤖 Помічник ШІ в пошуку

<div class="card text-medium-small text-left">

💬 Після пошуку за зображенням можна **поставити запитання** про фото:
- «Що це за місце?»
- «Де зроблено це фото?»
- «Що це за будівля?»

</div>

<div class="important-to-remember text-medium-small text-left">

⚠️ **ШІ теж помиляється** і може «вигадувати» відповіді. Відповідь ШІ — це **підказка**, яку треба **підтвердити джерелами** (крок **F**).

</div>

---

## 🔬 Метод 5W1H

<div class="text-small">

| Запитання | Що з'ясовуємо |
|---|---|
| 👤 **Who? — Хто?** | Хто автор і хто опублікував? Чи є контакти, імена журналістів? |
| 📄 **What? — Що?** | Що саме стверджують? Які докази: документи, номери законів, імена? |
| 📅 **When? — Коли?** | Коли опубліковано? Чи не «консерва» це — стара новина, яку поширюють знову? |
| 📍 **Where? — Де?** | Де відбуваються події? Чи пишуть про це місцеві та інші ЗМІ? |
| 🎯 **Why? — Чому?** | Навіщо це створено: інформувати чи викликати гнів, страх, зібрати перегляди? |
| 🎭 **How? — Як?** | Як подано: спокійно й збалансовано чи мовою маніпуляції («ШОК!»)? |

</div>

---

## ⚖️ SIFT чи 5W1H?

<div class="grid-container">
<div class="card text-medium-small text-left">

🔎 **SIFT**
Швидке щоденне «патрулювання» стрічки новин

</div>
<div class="card text-medium-small text-left">

🔬 **5W1H**
Глибоке розслідування найважливіших і найпідозріліших випадків

</div>
</div>

<div class="important-to-remember text-medium text-left">

✋ **Не довіряй — перевіряй!**

</div>

---

## 👀 Пауза для очей

<div class="card text-medium">

Правило **20-20-20**: кожні 20 хвилин дивіться 20 секунд на предмет на відстані 20 футів (≈ 6 м).

</div>

---

## ⌨️ Практика 1: метод SIFT

<div class="grid-container">
<div class="task text-small text-left">

🔎 Перевірте допис за кроками **SIFT**, користуючись пошуком в інтернеті.

📝 Запишіть у зошит:
- ✋ **S:** що в дописі тисне на емоції?
- 🕵️ **I:** що ви дізналися про джерело?
- 📰 **F:** що пишуть офіційні джерела та надійні ЗМІ?
- 🧵 **T:** звідки взялося твердження? Чи є оригінал?
- ✅ **Висновок:** фейк чи правда?

</div>
<div class="image-center">

![h:430](assets/18/fake-post-winter-holidays.svg)

</div>
</div>

---

## ⌨️ Практика 2: «Де це знято?»

<div class="task text-medium-small text-left">

1. 📂 Відкрийте папку з фото: [🔗 Google Диск](https://drive.google.com/drive/folders/1KZUCqJtRZlYaJ7rhz6XBHvnM5XPxF4pl?usp=sharing)
2. 🖼️ Для кожного з **4 фото** скористайтеся **Google Lens** і **помічником ШІ**.
3. ❓ З'ясуйте: **що** зображено і **де** зроблено фото (місто, країна, назва об'єкта).
4. ✅ Підтвердьте відповідь ШІ **джерелом** (сайт, карта, інші фото).

</div>

<div class="card text-small text-left">

📝 Таблиця в зошиті: **№ фото — що зображено — де зроблено — джерело підтвердження**

</div>

---

## 📊 Обговорюємо результати

<div class="card text-medium-small text-left">

- 🔎 Що ви з'ясували на кожному кроці **SIFT**? Який висновок?
- 🖼️ Що зображено на фото і де їх зроблено?
- 🤖 Чи помилився **ШІ** хоча б раз? Як ви це помітили?
- 🧩 Яке фото було найскладнішим? Що допомогло?

</div>

---

## 🗣️ Рефлексія

<div class="emoji-large">🤔</div>

<div class="card text-medium text-left">

Продовжіть речення:
**«Тепер, коли я бачу сенсаційну новину, я першим ділом...»**

</div>

---

## 🏠 Домашнє завдання

<div class="card text-medium-small text-left">

1. 📖 Опрацювати матеріал підручника, **с. 60–61**.
2. 🎬 Переглянути серію 8 серіалу **«ДезінFAKEція»** (Дія.Освіта): [▶️ Серія 8](https://www.youtube.com/watch?v=Tkhm7Y4yNRo)

</div>
