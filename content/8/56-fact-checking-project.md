---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 56
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
  .text-center {
    text-align: center;
  }

---

# Фактчекінг зображень. Як відрізнити справжнє фото від ШІ-генерації

## 🏫 Урок **56**

---

## 🎯 Сьогодні ми навчимося

- 🕵️ Розрізняти справжні фотографії від згенерованих штучним інтелектом.
- 🔍 Використовувати інструменти цифрової перевірки.
- 🌐 Здійснювати зворотний пошук зображень для верифікації контенту.

---

## 🧠 Що потрібно пам'ятати?

<div class="important-to-remember text-medium">

🖼️ **AI-генероване зображення** — це зображення, створене нейромережею на основі текстового запиту (промпту).

🧩 **Артефакти ШІ** — характерні помилки нейромереж (неправильна кількість пальців, дивна текстура шкіри, розмиті фони, нелогічні тіні).

⚠️ **Важливо:** автоматичні детектори можуть помилятися, тому рішення треба приймати за сукупністю ознак.

</div>

---

## 🛠 Наш інструментарій

<div class="grid-container">
  <div class="grid-item text-center">
    <span class="emoji-large">🔍</span>

### Пошук за зображенням

[Пошук зображень Google](https://images.google.com)

  </div>
  <div class="grid-item text-center">
    <span class="emoji-large">🤖</span>

### Детектори ШІ

- [Hive Moderator](https://hivemoderation.com/ai-generated-content-detection)
- [Illuminarty](https://app.illuminarty.ai/)

  </div>
</div>

---

## 🕵️ Практична робота: "Цифровий детектив"

**Ваша місія:** Провести дослідження двох наданих учителем фотографій та створити короткий звіт у Google Документах або MS Word.

<div class="card">

**Що має бути у звіті:**
Оцінка кожного фото (справжнє чи ШІ), ваше обґрунтування та скриншоти перевірок через спеціальні сервіси.

</div>

---

## ⭐️ Завдання 1: Візуальний аналіз

<div class="task">

1. **Уважно розгляньте кожне фото.** Спробуйте знайти "артефакти" ШІ (зверніть увагу на руки, волосся, фон, дивні написи та тіні).
2. **Використайте [Пошук зображень Google](https://images.google.com/)**, щоб знайти, чи публікувалося це фото раніше на надійних ресурсах.
3. **Запишіть у звіт:** "Фото №... : [Справжнє / ШІ], тому що [ваше обґрунтування висновку]".

</div>

---

## ⭐️⭐️ Завдання 2: Автоматична перевірка

<div class="task text-medium">

1. Завантажте кожне зображення у сервіс [Hive Moderator](https://hivemoderation.com/ai-generated-content-detection) та [Illuminarty](https://app.illuminarty.ai/).
2. **Зробіть знімки екрану** результатів, де вказано ймовірність (у відсотках) того, що зображення створене ШІ, та додайте їх у звіт.
3. **Порівняйте та зробіть висновок:** чи збігається ваша власна візуальна оцінка (із Завдання 1) з результатами автоматичних детекторів?
4. **Запишіть у звіт**: "Висновок: Я вважаю, що фото №... [Справжнє / ШІ], тому що [ваше обґрунтування]"

</div>

---

## Фото для перевірки

<div class="grid-container">
  <div class="grid-item image-center">

![w:350px](./assets/55/image-1.png)

  </div>
  <div class="grid-item image-center">

![w:400px](./assets/55/image-2.png)

  </div>
</div>
