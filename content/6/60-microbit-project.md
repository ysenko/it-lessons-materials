---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 60
title: Складання проєктів на платформі Micro:Bit. Гра «Камінь, ножиці, папір»
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
  .step-instruction {
    background-color: #e3f2fd;
    border-left: 5px solid #2196f3;
    padding: 15px;
    border-radius: 8px;
    text-align: left;
  }
  .screenshot-placeholder {
    border: 3px dashed #90a4ae;
    border-radius: 8px;
    background-color: #f5f5f5;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 200px;
    color: #90a4ae;
    font-size: 18px;
    text-align: center;
  }

---

# Складання проєктів на платформі Micro:Bit

## 🏫 Урок **60**

---

## 🎯 Сьогодні ми навчимося

- 🔧 Використовувати змінні та випадкові числа в MakeCode
- 🧠 Будувати умовну логіку з кількома варіантами
- 🎮 Створити повноцінну гру «Камінь, ножиці, папір»

---

## 🔍 Перевірка знань

1. Що таке Micro:Bit?
2. Як називається середовище для його програмування?
3. Що таке **подія** у програмуванні?
4. Що таке **змінна**?

---

## 🎮 Наша мета сьогодні

<section class="card">

Ми запрограмуємо гру **«Камінь, ножиці, папір»** на Micro:Bit:

- 🪨 Струснув — Micro:Bit «кидає» камінь, ножиці або папір
- 🎲 Кожного разу — **випадковий** результат
- 💡 Символ відображається на LED-матриці пристрою

</section>

Редактор: [makecode.microbit.org/#editor](https://makecode.microbit.org/#editor)

---

<!-- Секція А -->

## 🅐 Крок 1 — Новий проект

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 1.** Відкрийте [makecode.microbit.org/#editor](https://makecode.microbit.org/#editor) та створіть **новий проект**.

</div>
<div class="image-center">

![w:450px](assets/60/step-01.png)

</div>
</section>

---

## 🅐 Крок 2 — Подія «при струшуванні»

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 2.** З категорії **Вхідні дані** оберіть блок **при струшуванні** та перетягніть його на робочу область.

</div>
<div class="image-center">

![w:450px](assets/60/step-02.png)

</div>
</section>

---

## 🅐 Перевіряємо себе

<section class="important-to-remember">

🗣️ Обговоріть з учителем:

- Що ми щойно зробили?
- Яка **подія** запускає нашу програму?
- Чому для гри обрали саме **струшування**?

</section>

---

<!-- Секція Б -->

## 🅑 Крок 3 — Змінна `hand`

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 3.** Перейдіть до категорії **Змінні** та створіть нову змінну з назвою **`hand`**.

</div>
<div class="image-center">

![w:450px](assets/60/step-03.png)

</div>
</section>

---

## 🅑 Крок 4 — Задати значення змінній

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 4.** З категорії **Змінні** оберіть блок **задати hand значення 0** та перетягніть його **всередину** блоку **при струшуванні**.

</div>
<div class="image-center">

![w:450px](assets/60/step-04.png)

</div>
</section>

---

## 🅑 Крок 5 — Випадкове число

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 5.** З категорії **Математика** оберіть **вибрати випадково від 1 до 3** та вставте замість **0** у блоці задати hand.

</div>
<div class="image-center">

![w:450px](assets/60/step-05.png)

</div>
</section>

---

## 🅑 Що ми закодували?

<section class="grid-container">
<div class="text-left text-medium">

| Число | Фігура |
|-------|--------|
| 1 | 🪨 Камінь |
| 2 | 📄 Папір |
| 3 | ✂️ Ножиці |

</div>
<div class="text-left text-medium">

<section class="card">

Змінна `hand` зберігає **випадкове число** від 1 до 3.

Кожне струшування — новий результат!

</section>

</div>
</section>

---

## 🅑 Перевіряємо себе

<section class="important-to-remember">

🗣️ Обговоріть з учителем:

- Навіщо нам потрібна змінна `hand`?
- Які числа може отримати `hand` після струшування?
- Як числа 1, 2, 3 пов'язані з фігурами гри?

</section>

---

<!-- Секція В -->

## 🅒 Крок 6 — Блок «якщо то інакше»

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 6.** З категорії **Логіка** оберіть блок **якщо істина то інакше** та додайте його під блок **задати hand**.

</div>
<div class="image-center">

![w:450px](assets/60/step-06.png)

</div>
</section>

---

## 🅒 Крок 7 — Умова порівняння

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 7.** З категорії **Логіка** оберіть блок **0 = 0** та перетягніть його замість **істина** у блоці якщо.

</div>
<div class="image-center">

![w:450px](assets/60/step-07.png)

</div>
</section>

---

## 🅒 Крок 8 — Порівняємо `hand` з 1

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 8.** З категорії **Змінні** перетягніть `hand` замість першого **0**. Другий **0** замініть на **1**.

</div>
<div class="image-center">

![w:450px](assets/60/step-08.png)

</div>
</section>

---

## 🅒 Крок 9 — Іконка каменю 💎

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 9.** З категорії **Основні** оберіть **показати іконку** та перетягніть у блок **якщо**. Оберіть іконку **Діамант** 💎 — це камінь.

</div>
<div class="image-center">

![w:450px](assets/60/step-09.png)

</div>
</section>

---

## 🅒 Перевіряємо себе

<section class="important-to-remember">

🗣️ Обговоріть з учителем:

- Коли відображається діамант (камінь)?
- Що станеться, якщо `hand` = 2 або 3?
- Чи достатньо одного блоку «якщо» для всієї гри?

</section>

---

<!-- Секція Г -->

## 🅓 Крок 10 — Додати «інакше якщо»

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 10.** Натисніть **+** внизу блоку **якщо то інакше** — з'явиться нова секція **інакше якщо**.

</div>
<div class="image-center">

![w:450px](assets/60/step-10.png)

</div>
</section>

---

## 🅓 Крок 11 — Умова для другої гілки

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 11.** З категорії **Логіка** перетягніть блок **0 = 0** у новий блок **інакше якщо**.

</div>
<div class="image-center">

![w:450px](assets/60/step-11.png)

</div>
</section>

---

## 🅓 Крок 12 — Порівняємо `hand` з 2

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 12.** З категорії **Змінні** перетягніть `hand` замість першого **0**. Другий **0** замініть на **2**.

</div>
<div class="image-center">

![w:450px](assets/60/step-12.png)

</div>
</section>

---

## 🅓 Крок 13 — Іконка паперу ⬛

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 13.** З категорії **Основні** додайте **показати іконку** у блок **інакше якщо**. Оберіть **Великий квадрат** ⬛ — це папір.

</div>
<div class="image-center">

![w:450px](assets/60/step-13.png)

</div>
</section>

---

## 🅓 Перевіряємо себе

<section class="important-to-remember">

🗣️ Обговоріть з учителем:

- При якому значенні `hand` відображається папір?
- Чим **інакше якщо** відрізняється від простого **якщо**?
- Що залишається у блоці **інакше**?

</section>

---

<!-- Секція Д -->

## 🅔 Крок 14 — Іконка ножиць ✂️

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 14.** У секцію **інакше** перетягніть **показати іконку** та оберіть іконку **Ножиці** ✂️.

</div>
<div class="image-center">

![w:450px](assets/60/step-14.png)

</div>
</section>

---

## 🅔 Крок 15 — Тестування 🧪

<section class="grid-container">
<div class="step-instruction text-medium-small">

**Крок 15.** Потрясіть мікроконтролер у **симуляторі** (лівий верхній кут). Перевірте, чи з'являються всі три символи!

</div>
<div class="image-center">

![w:450px](assets/60/step-15.png)

</div>
</section>

---

## 🅔 Перевіряємо себе

<section class="important-to-remember">

🗣️ Обговоріть з учителем:

- Чому ножиці у блоці **інакше**, а не в окремому **інакше якщо**?
- Скільки разів потрібно потрясти, щоб перевірити всі варіанти?
- Ваша програма працює правильно?

</section>

---

## 🧩 Як виглядає повна програма

<section class="card">

```
при струшуванні
  задати hand = вибрати випадково від 1 до 3
  якщо hand = 1
    показати іконку 💎 (Діамант)
  інакше якщо hand = 2
    показати іконку ⬛ (Великий квадрат)
  інакше
    показати іконку ✂️ (Ножиці)
```

</section>

---

## 🤔 Підсумок уроку

- 🎲 Змінна `hand` зберігає **випадкове** число від 1 до 3
- 🔀 Блок **якщо / інакше якщо / інакше** дозволяє обрати **один з кількох варіантів**
- 💎 Кожне число відповідає своїй фігурі гри
- 🧪 Симулятор дозволяє тестувати без фізичного пристрою

---

## 🏠 Домашнє завдання

Придумайте та опишіть словами (або намалюйте блок-схему):

**Як можна вдосконалити нашу гру?**

Наприклад:
- 🏆 Рахувати рахунок перемог
- 🎉 Показувати анімацію при перемозі
- 🔔 Додати звук при програші

Запишіть свою ідею у зошит.
