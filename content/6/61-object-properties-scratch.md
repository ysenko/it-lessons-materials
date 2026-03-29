---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 61
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

# 🚀 Створення програмних об’єктів

## 🏫 Урок **61**

---

## 🎯 Сьогодні ми навчимося

- 🆕 **Створювати** нові об'єкти різними способами.
- 🎨 **Малювати** власні спрайти у вбудованому редакторі.
- ⚙️ **Керувати** властивостями об'єктів за допомогою коду.
- 🛠️ **Працювати** з координатами та циклами.

---

## 🧐 Пригадаємо: що таке об’єкт у Scratch?

<section class="grid-container">
<div class="card">
<span class="emoji-large">👾</span>
<center><b>Спрайт</b></center>
Це програмний об'єкт, який має ім'я, властивості та може виконувати дії.
</div>
<div class="card">
<span class="emoji-large">📋</span>
<center><b>Властивості</b></center>
Розмір, напрямок, положення (X, Y), образ, видимість.
</div>
</section>

---

## 🛠️ Як створити новий об'єкт?

У Scratch є **4 способи** додати спрайт:

1. 🔍 **Обрати з бібліотеки** (готові малюнки).
2. 🖌️ **Намалювати** (створити власний у редакторі).
3. 🎲 **Сюрприз** (випадковий спрайт).
4. 📤 **Завантажити** (файл з вашого комп'ютера).

---

## 💻 Координати: Де знаходиться об’єкт?

Сцена Scratch — це координатна площина:
- ↔️ **X** (ліво-право): від -240 до 240.
- ↕️ **Y** (низ-верх): від -180 до 180.
- 📍 **(0, 0)** — це самий центр сцени.

---

## 🖱️ Практичне завдання «Космічна лабораторія»

<section class="task text-medium-small">

**Середній рівень (4-6 балів):**
1. Видаліть Кота. Додайте спрайт **Rocketship**.
2. Змініть його назву на **Мій_Корабель**.
3. Складіть скрипт: Коли натиснуто 🟢:
   - `задати розмір 120 %`
   - `повернути в напрямку 45`
   - `перемістити в x: 0 y: 0`

</section>

---

## ⭐ Продовжуємо проект

<section class="task text-medium-small">

**Достатній рівень (7-9 балів):**
1. Додайте спрайт **Star** (Зірка) та тло **Stars**.
2. Скрипт для Зірки (постійно):
   - `перейти до випадкова позиція`
   - `змінити ефект колір на 25`
   - `чекати 1 сек`

</section>

---

## 🌌 Творче завдання (Високий рівень)

<section class="task text-medium-small">

**Високий рівень (10-12 балів):**
1. Додайте з бібліотеки спрайт **Planet2**.
2. Напишіть скрипт, щоб вона постійно падала зверху вниз і знову з'являлася вгорі.

💡 **Підказка:**
У циклі `завжди`:
- `змінити y на -5`
- `якщо y-позиція < -170, то задати y 180`

</section>

---

## 🗣️ Рефлексія

- Який спосіб створення об'єкта вам сподобався найбільше?
- Що було складніше: знайти потрібний спрайт чи налаштувати його рух?
- Яка команда допомагає об'єкту повернутися вгору?

---

## 🏠 Домашнє завдання

- Повторити властивості об’єктів.
- 💡 **Творча ідея:** придумайте, які властивості мав би ваш власний супергерой у Scratch!
