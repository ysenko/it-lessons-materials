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

# Crashy Bird на Micro:Bit 🐦

## 🏫 Урок **62**

---

## 🎮 Що таке Crashy Bird?

<section class="grid-container">
<div class="text-left text-medium">

Це гра схожа на **Flappy Bird**!

- 🐦 Ти керуєш птахом
- 🧱 Летять перешкоди
- ⬆️⬇️ Кнопки A і B — вгору і вниз
- 💀 Вдарився — гра закінчилась

Сьогодні ми запрограмуємо її **самі**!

</div>
<div class="image-center">

![w:320px](./assets/62/crashy-bird-demo.jpg)

</div>
</section>

---

## 🎯 Сьогодні ми навчимося

- 🐦 Створювати спрайти та керувати ними кнопками
- 🧱 Генерувати перешкоди за допомогою циклів і масивів
- ➡️ Рухати об'єкти та видаляти їх зі сцени
- 💡 Використовувати лічильник і залишок від ділення
- 💀 Перевіряти зіткнення та завершувати гру

---

## 🚀 Починаємо! Відкриваємо MakeCode

<section class="task text-medium">

## ⌨️ Підготовка до роботи

1. Відкрий браузер і перейди на сайт:
   **https://makecode.microbit.org**
2. Натисни кнопку **«Новий проект»**
3. Введи назву проекту: **Crashy Bird**
4. Натисни **«Створити»**

</section>

---

## 🎬 Дивись відео та будуй разом

<section class="grid-container">
<div class="text-left text-medium-small">

Відео покаже всі **7 кроків** від початку до кінця:

1. 🐦 Додаємо птаха
2. ⬆️⬇️ Птах літає
3. 🧱 Перешкоди
4. ➡️ Перешкоди рухаються
5. 🧹 Прибираємо перешкоди
6. ♾️ Нові перешкоди постійно
7. 💀 Кінець гри

🔗 [**https://youtu.be/4JxKdH1i2t8**](https://youtu.be/4JxKdH1i2t8)

</div>
<div class="image-center">

![w:280px](./assets/62/qr-video.png)

</div>
</section>

---

## 🎉 Вітаємо! Гра готова!

<section class="grid-container">
<div class="text-left text-medium-small">

Ти запрограмував справжню гру! Ось що ти використав:

- 🐦 **Спрайти** — об'єкти на LED-екрані
- 📋 **Масив** — список спрайтів-перешкод
- 🔁 **Цикли** — для руху та перевірки
- 🎲 **Випадковість** — для дірок у перешкодах
- 🔢 **Залишок від ділення** — для ритму появи
- 💥 **Перевірка координат** — для зіткнень

</div>
<div class="image-center">

🎮

**Ти — розробник ігор!**

</div>
</section>

---

## 🤔 Рефлексія

<section class="grid-container">
<div class="text-left text-medium">

Обговоримо разом:

- 💬 Який крок був **найважчим**?
- 💬 Яку помилку ти **допустив і виправив**?
- 💬 Навіщо потрібен **масив** у цій грі?
- 💬 Що означає **`ticks % 3 = 0`**?

</div>
<div class="text-left text-medium">

Підніми руку, якщо:

- ✋ Виконав усі 7 кроків
- ✋ Виконав хоча б кроки 1–5
- ✋ Хочеш показати свою гру класу

</div>
</section>

---

## 🏠 Домашнє завдання

<section class="task text-medium">

## 📝 Для тих, хто не встиг завершити гру на уроці

1. Відкрий [**makecode.microbit.org**](https://makecode.microbit.org)
2. Знайди або створи проект **Crashy Bird**
3. Переглянь відео та дороби кроки, які залишилися

🔗 [https://youtu.be/4JxKdH1i2t8](https://youtu.be/4JxKdH1i2t8)

</section>
