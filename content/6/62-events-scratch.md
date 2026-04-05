---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 62
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

# Події у Scratch 🚀

*Організація взаємодії між об’єктами*

## 🏫 Урок **62**

---

## 🎯 Сьогодні ми дізнаємося

- ❓ Що таке **подія** в програмуванні.
- ⌨️ Як керувати героями за допомогою клавіш та мишки.
- 📱 Як об'єкти спілкуються між собою за допомогою **повідомлень**.
- 🛠️ Як створити справжню командну роботу спрайтів.

---

## 🧠 Пригадаймо!

<div class="grid-container">
  <div class="grid-item">

### 🐱 Спрайт

Це об'єкт (герой), який виконує команди.

  </div>
  <div class="grid-item">

### 🛠️ Властивості

Розмір, колір, напрямок, координати X та Y.

  </div>
  <div class="grid-item">

### 📜 Скрипт

Послідовність блоків, що задають дії.

  </div>
</div>

---

## ⚡ Що таке подія?

<div class="important-to-remember">

**Подія** — це сигнал для комп'ютера, що пора запускати певний скрипт. Без події жодна програма не почне працювати!

</div>

<div class="grid-container">
  <div class="text-left">

### Основні події:

- 🟢 Зелений прапорець
- ⌨️ Клавіша клавіатури
- 🖱️ Натиснуто на спрайт

  </div>
  <div class="image-center">

![w:350px](./assets/62/scratch-events.png)

  </div>
</div>

---

## 💬 Аналогія: Чат класу

Уявіть, що ваші спрайти — це учні в групі Viber або Telegram.

- 👩‍🏫 **Вчитель** (один спрайт) пише: *"Завтра всі принесіть змінне взуття!"*
  (Це блок **«Оповістити»**)
- 🔔 **Учні** (інші спрайти) отримують сповіщення.
  (Це блок **«Коли я отримаю»**)
- 👟 **Кожен реагує по-своєму**: хтось іде чистити кросівки, хтось шукає пакет для взуття, а хтось ігнорує.

---

## 🛠️ Блоки повідомлень

<div class="grid-container text-medium">
<div class="text-left">
<div class="card">

**Оповістити [повідомлення]**

Надсилає сигнал усім об'єктам.

</div>
<div class="card">

**Коли я отримаю [повідомлення]**

Чекає на свій сигнал і запускає скрипт.

</div>
</div>
<div class="image-center">

![w:350px](./assets/62/scratch-broadcast.png)
![w:350px](./assets/62/scratch-receive.png)

</div>
</div>

<div class="text-small">

> 💡 **Порада**: Давай повідомленням зрозумілі назви, наприклад: `старт_гри`, `день`, `ніч`, `вогонь`.

</div>

---

## 🧪 Демонстрація: «Магічна кнопка»

<div class="task text-medium-small">

Спробуємо створити таку взаємодію:

1. 🔘 **Спрайт Кнопка**:
   - При натисканні на неї — оповістити `танцюй`.
2. 🐻 **Спрайт Ведмідь**:
   - Коли отримає `танцюй` — повторити 5 разів:
     - змінити ефект колір на 25
     - змінити розмір на 10
     - чекати 0.5 сек
     - змінити розмір на -10
     - чекати 0.5 сек

**Результат**: ведмідь «пульсує» та змінює колір після кожного натискання! ✨

</div>

---

## 💻 Практичне завдання (на вибір)

<div class="grid-container text-medium-small">

<div class="task">

### 📘 Рівень 1: Діалог 🗣️

1. **Кіт** (`Cat`):
   - **Коли натиснуто 🟢** $\rightarrow$ Каже "Привіт!" $\rightarrow$ Оповіщає `вітання`.
2. **Собака** (`Dog`):
   - **Коли я отримую** `вітання`:
   - Чекає 1 сек $\rightarrow$ Каже "Гав! Радий бачити!".

</div>

<div class="task">

### 🌟 Рівень 2: Лабораторія ✨

1. **Чарівник** (`Wizard`):
   - **Коли спрайт натиснуто** $\rightarrow$ Оповіщає `магія`.
2. **Предмет** (`Star` або `Crystal`):
   - **Коли я отримую** `магія`:
   - **Повторити 10 разів**:
     - Повернути на 36°
     - Змінити ефект колір на 25

**Результат**: предмет обертається і переливається кольорами! 🌈

</div>

</div>

---

## ❓ Питання для роздумів

1. Чи може один спрайт надіслати повідомлення сам собі? 🤔
2. Що станеться, якщо два спрайти будуть чекати на одне і те саме повідомлення? 👥
3. Чому блоки повідомлень кращі, ніж блок "чекати 2 секунди"? ⏳

---

## 🏠 Домашнє завдання

- 📖 Прочитати розділ підручника про події та оповіщення (с. 209-213).
- 📝 Записати в зошит 3 приклади подій із реального життя (наприклад: дзвінок у двері → ви йдете відчиняти).
