---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 16
style: |
  .grid-container {
    display: grid;
    grid-template-columns: 50% 50%;
    align-items: start;
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
    border: 2px solid #333;
    border-radius: 12px;
    padding: 15px;
  }
  .important-to-remember {
    background-color: lightyellow;
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

# 🤖 Чи можна беззаперечно довіряти ШІ?

## 🏫 Урок **16**

![bg left:30% 80%](https://img.icons8.com/color/480/artificial-intelligence.png)

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке "упередженість штучного інтелекту".
- ❓ Звідки вона виникає (дані, люди, стереотипи).
- 🧐 Чому результатам роботи ШІ не можна довіряти беззаперечно.

---

## 🧠 Мозковий штурм

Де ми щодня стикаємося зі Штучним Інтелектом?

<div class="grid-container">
  <div class="borderless">
    <div class="card borderless">
      <span class="emoji-large">🎬</span>
      Рекомендації (YouTube, TikTok)
    </div>
    <div class="card borderless">
      <span class="emoji-large">📸</span>
      Фільтри (Instagram)
    </div>
  </div>
  <div class="borderless">
    <div class="card borderless">
      <span class="emoji-large">🗣️</span>
      Помічники (Siri, Google)
    </div>
    <div class="card borderless">
      <span class="emoji-large">⌨️</span>
      Автокорекція (Клавіатура)
    </div>
  </div>
</div>

---

## 🤔 Поміркуйте

Чи завжди ШІ дає ідеально правильні та справедливі поради?

---

## 🤖 Що таке Штучний Інтелект (ШІ)?

<div class="card text-medium-small important-to-remember">

**Штучний інтелект (ШІ)** – це технологія, яка намагається імітувати людський інтелект для виконання завдань (наприклад, розпізнавання зображень, переклад мови, прийняття рішень), що потребують людського інтелекту.

</div>

---

## 🧐 Що таке Упередженість ШІ?

Уявіть, що ШІ – учень. Якщо він вчиться за підручниками, де є помилки, він "вивчить" ці помилки і буде їх повторювати.

<br>

<div class="important-to-remember card">

**Упередженість ШІ (AI Bias)** – це систематичні несправедливі або неточні результати роботи ШІ.

</div>

---

## 📂 Причина №1: Проблема в даних

<span class="text-medium">

ШІ вчиться на даних, які ми йому даємо.

</span>

<div class="card text-medium-small">

### 👩‍⚕️ Приклад: "Лікар"

Якщо ми покажемо ШІ 1000 фото, де 900 лікарів – це чоловіки, ШІ зробить висновок: **"Лікар = Чоловік"**.

<br>

- **Наслідок:** Він буде гірше розпізнавати жінок-лікарів.
- **Висновок:** Дані, на яких вчився ШІ, були незбалансовані.

</div>

<p class="text-medium">🗑️ "Сміття на вході = Сміття на виході"</p>

---

## 👨‍💻 Причина №2: Людський фактор

<div class="grid-container text-medium">
  <div class="card">

### 🧑‍🔬 Розробники

Розробники можуть (навіть не навмисно) внести власні упередження.

<br>
<br>

_Приклад:_ Система розпізнавання облич, яку тестували лише на світлій шкірі, погано працює для людей з темною шкірою.

  </div>
  <div class="card">

### 🌍 Стереотипи

ШІ "вивчає" шкідливі стереотипи.

<br>
<br>
<br>

_Приклад:_ ШІ для прийому на роботу навчився на старих даних, що "технічні посади – для чоловіків", і почав відхиляти резюме жінок.

  </div>
</div>

---

## 💡 Головна думка уроку

<div class="card">

🤖 Штучний інтелект – це не магія. Це інструмент.

Він лише **віддзеркалює** ті дані та помилки, які в нього заклали люди.

</div>

<br>

<div class="important-to-remember card">

**✍️ Запам'ятайте:**
Штучному інтелекту **НЕ МОЖНА** довіряти беззаперечно. Результати його роботи **ЗАВЖДИ** потрібно перевіряти.

</div>

---

## 🖥️ Практична частина

### 🔍 Вправа: "Дослідники упереджень"

<div class="text-medium-small task">

**Мета:** Побачити на практиці, як ШІ "думає" і на яких даних він вчиться.

**Інструмент:** Гра від Google **"Quick, Draw!"**

</div>

![bg right:40%](https://img.icons8.com/color/480/paint-palette.png)

---

## 🕹️ Інструкція до "Quick, Draw!"

<div class="text-medium-small">

1. Відкрийте веббраузер (Chrome або Edge).
2. Перейдіть на сайт: **[quickdraw.withgoogle.com](https://quickdraw.withgoogle.com/)**
3. Натисніть "Let's Draw!" (Нумо малювати!).
4. Ваше завдання: за 20 секунд намалювати слово, яке запропонує ШІ, щоб він його вгадав.
5. Зіграйте один раунд (6 малюнків).
6. **Після гри:** Натисніть на свої малюнки, щоб побачити, з чим ШІ їх порівнював.

<br>

<div class="text-medium">

**❓ Подумайте:** Чому ШІ не вгадав деякі ваші малюнки?

</div>

---

## 🏠 Домашнє завдання

<div class="task">

1. 📰 Знайдіть в інтернеті реальний приклад (новину) про упередженість ШІ. Прочитайте новину та розкажіть про неї в класі.

2. 📝 Запишіть у зошиті свої роздуми про те, у якій професії ви б найбільше боялися упередженого ШІ і чому?

</div>
