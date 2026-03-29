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

# 🚀 Інтерактивні об’єкти у Scratch

## 🏫 Урок **61**

---

## 🎯 Сьогодні ми навчимося

- 🆕 **Створювати** нові спрайти (об'єкти) різними способами.
- ⚡ **Керувати** властивостями через **події**.
- 🎮 **Змінювати** розмір, колір та положення за допомогою клавіш.
- 🛠️ **Працювати** зі спрайтами Planet2, Rocketship та Star.

---

## ⚡ Що таке подія?

Подія — це те, що змушує скрипт працювати.

<section class="grid-container">
<div class="card text-small">
<center>🟢</center>

При натисканні зеленого прапорця (Старт).

</div>
<div class="card text-small">
<center>⌨️</center>

При натисканні певної клавіші на клавіатурі.

</div>
<div class="card text-small">
<center>🖱️</center>

При натисканні мишкою на сам спрайт.

</div>
</section>

---

## 🖱️ Практичне завдання «Космічна лабораторія»

<section class="task text-medium-small">

**Середній рівень (4-6 балів):**
1. Видаліть Кота. Додайте спрайт **Rocketship**.
2. Змініть його назву на **Мій_Корабель**.
3. Складіть скрипт: Коли натиснуто 🟢:
   - `задати розмір 120`
   - `повернути в напрямку 45`
   - `перемістити в x: -150 y: -100`

</section>

---

## ⭐ Оживляємо Зірку

<section class="task text-medium-small">

**Достатній рівень (7-9 балів):**
1. Додайте спрайт **Star** та тло **Stars**.
2. Скрипти для Зірки:
   - При натисканні на саму Зірку: `змінити ефект колір на 25`, `говорити "Привіт!" 2 сек`.
   - При натисканні клавіші **"стрілка вгору"**: `змінити розмір на 10`.

</section>

---

## 🌌 Керування планетою (Високий рівень)

<section class="task text-medium-small">

**Високий рівень (10-12 балів):**
1. Додайте спрайт **Planet2**.
2. Додайте скрипти для Планети:
  - Клавіша **"пропуск"** ➡️ `наступний образ`.
  - Клавіша **"стрілка праворуч"** ➡️ `повернути на 15 градусів`.
  - Клавіша **"a"** (англійська) ➡️ `перейти до випадкової позиції`.

</section>

---

## 🗣️ Рефлексія

- Чи зручніше керувати спрайтом за допомогою клавіш?
- Які ще клавіші можна використати для керування?
- Яка властивість змінювалася при натисканні на Зірку?

---

## 🏠 Домашнє завдання

- Повторити властивості об’єктів (с. 203-208).
- 💡 Придумайте, якими клавішами можна керувати іншими спрайтами.
