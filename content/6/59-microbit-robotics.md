---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 59
title: Практичне програмування роботів. Складання проєктів на платформі Micro:Bit
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

# 🤖 Практичне програмування роботів

## 🏫 Урок **59**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке **робототехніка** і з чого складається робот
- 🔭 Цікаві факти про сучасних роботів у світі
- 🔧 Що таке **Micro:Bit** і що він вміє
- ✏️ Як програмувати Micro:Bit в **MakeCode**

---

## ⚡ Пригадаємо

<div class="text-medium">

1. Що таке **алгоритм**? Наведіть приклад.
2. Що ми вже вміємо робити у **Scratch**?
3. Чи може програма керувати **фізичним пристроєм**?

</div>

<div class="important-to-remember">

💡 Сьогодні ми дізнаємося, що **так!** — і побачимо як саме.

</div>

---

## 🌍 Роботи навколо нас

<section class="grid-container">
<div class="card text-left text-medium-small">

🦾 **Boston Dynamics**
Роботи, що ходять, стрибають і виконують завдання

</div>
<div class="card text-left text-medium-small">

🏥 **Хірургічний Da Vinci**
Проводить операції з точністю до 1 мм

</div>
<div class="card text-left text-medium-small">

🚀 **Марсохід Perseverance**
Досліджує іншу планету без участі людини

</div>
<div class="card text-left text-medium-small">

📦 **Склади Amazon**
Сотні роботів переміщають товари 24/7

</div>
</section>

**Що спільного між усіма цими пристроями?** 🤔

---

## 🤖 Що таке робот?

<div class="card">

**Робот** — пристрій, здатний виконувати дії **автоматично або за програмою**, не потребуючи постійної участі людини.

</div>

<div class="card">

**Робототехніка** — галузь науки і техніки, що займається проектуванням, створенням та застосуванням роботів.

</div>

Роботи працюють у 🏥 медицині, 🏭 промисловості, 🚀 космосі, 🏠 побуті.

---

## ⚙️ З чого складається робот?

<div class="text-medium-small">

| Компонент | Роль | Приклад |
| --- | --- | --- |
| 🌡️ Датчик / сенсор | «Органи чуття» — зчитують інформацію | температура, відстань, освітленість |
| 🧠 Мікроконтролер | «Мозок» — обробляє дані, приймає рішення | Micro:Bit, Arduino |
| 🦾 Маніпулятор | «Руки і ноги» — здійснює дії у світі | мотор, LED-матриця |
| 💻 Програма | «Інтелект» — алгоритм поведінки | Scratch, MakeCode |

</div>

---

## 🔄 Як це працює разом?

<div style="text-align: center; margin: 20px 0;">

<div class="card text-medium">

🌡 **Датчик** — зчитує середовище

</div>

<div class="card text-medium">

🧠 **Мікроконтролер** — обробляє та вирішує

</div>

<div class="card text-medium">

🦾 **Маніпулятор** — виконує дію

</div>

</div>

---

## 🔄 Приклад: кімнатний термостат

<section class="grid-container">
<div class="text-left text-medium-small">

🌡️ **Датчик**
вимірює температуру в кімнаті

⬇️

🧠 **Мікроконтролер**
порівнює з бажаною температурою

⬇️

🦾 **Маніпулятор**
вмикає або вимикає обігрів

</div>
<div class="text-left text-medium-small">

Те ж саме у робота:

- 👁️ Камера бачить перешкоду
- 🧠 Комп'ютер аналізує
- 🦿 Двигуни зупиняються

**Програма** визначає, що робити в кожній ситуації!

</div>
</section>

---

## 🌟 Цікаві факти про роботів

<section class="grid-container">
<div class="card text-left text-small">

🤸 **Boston Dynamics Atlas**
Виконує паркур і сальто — подивіться самі!

[▶ Дивитись відео](https://www.youtube.com/watch?v=tF4DML7FIWk)

</div>
<div class="card text-left text-small">

🍇 **Робот Da Vinci**
Асистує хірургу — точність до 1 мм!

[▶ Дивитись відео](https://www.youtube.com/watch?v=0XdC1HUp-rU)

</div>
<div class="card text-left text-small">

🚀 **Марсохід Perseverance**
Посадка на Марс у 2021 — відео з борту!

[▶ Дивитись відео](https://www.youtube.com/watch?v=4czjS9h4Fpg)

</div>
<div class="card text-left text-small">

📦 **Amazon: 750 000 роботів**
Переміщають товари по складах 24/7

[▶ Дивитись відео](https://www.youtube.com/watch?v=NZTVgExZqoI)

</div>
<div class="card text-left text-small">

🐝 **RoboBee — Гарвард**
Мікроробот розміром з мурашку!

[▶ Дивитись відео](https://www.youtube.com/watch?v=cyjKOJhIiuU)

</div>
<div class="card text-left text-small">

🎨 **Робот-художник FRIDA**
Малює картини за допомогою штучного інтелекту

[▶ Дивитись відео](https://www.youtube.com/watch?v=vdMnAUtetAE)

</div>
</section>

---

## 🔬 Що таке Micro:Bit?

<section class="grid-container">
<div class="text-left text-medium-small">

**Micro:Bit** — невелика програмована плата (≈ 4×5 см), розроблена BBC для навчання програмування.

Це **справжній мікроконтролер**:

- має вбудовані датчики
- має виконавчі пристрої (LED)
- програмується через Scratch або MakeCode

🎓 Використовується у школах понад 30 країн!

</div>
<div class="image-center">

![w:350px](https://www.voltaat.com/cdn/shop/files/voltaat-deveb-arduino-micro-bit-v2-development-board-built-in-sensors-and-speaker-1211135314_1200x1200.jpg?v=1765716308)

</div>
</section>

---

## 🖥️ Що є на платі Micro:Bit?

<section class="grid-container">
<div class="text-left text-medium-small">

**🌡️ Датчики (сенсори):**

- Температури
- Акселерометр (рух, нахил)
- Компас
- Освітленості (через LED)

</div>
<div class="text-left text-medium-small">

**💡 Виконавчі пристрої:**

- LED-матриця 5×5 (25 вогників)
- Гучномовець (v2)

**📡 Зв'язок:**

- Bluetooth і радіомодуль

**🔘 Керування:**

- Кнопки A і B
- Пін-з'єднувачі (для моторів тощо)

</div>
</section>

---

## 💻 Емулятор Micro:Bit — MakeCode

<section class="grid-container">
<div class="text-left text-medium-small">

**MakeCode** — онлайн-середовище для програмування Micro:Bit.

✅ Не потребує фізичного пристрою
✅ Вбудований **емулятор** (симулятор плати)
✅ Можна натискати кнопки, нахиляти — прямо в браузері!

Програмування: **блоки** або **JavaScript**

</div>
<div class="text-left text-medium-small">

<a href="https://makecode.microbit.org/#editor" target="_blank">🔗 Відкрити MakeCode Micro:Bit</a>

Праворуч — **симулятор** плати.
Зліва — блоки для програмування.
Внизу — завантаження на реальну плату.

</div>
</section>

---

<section class="task text-medium-small">

## ⌨️ Практична робота: перший проєкт у MakeCode

1. Відкрити емулятор: <a href="https://makecode.microbit.org/#editor" target="_blank">makecode.microbit.org</a>
2. Знайти блок **«при запуску»** (категорія «Основні»)
3. Додати: **«показати іконку»** → вибрати символ ♥
4. Знайти блок **«постійно»**
5. Додати: **«показати рядок»** → ввести своє ім'я англійською мовою.

Подивитися на **симулятор** праворуч — він одразу показує результат!

⚠️ Не потрібно нічого завантажувати — симулятор працює прямо у браузері.

</section>

---

## 👁️ Релаксація для очей

<span class="emoji-large">👀</span>

Відірвіться від екрана.
Подивіться у вікно на **далекі предмети** — 30 секунд.
Потім поморгайте очима — 10 разів.

---

## 🤔 Рефлексія

- Що таке **робот**? Чим він відрізняється від звичайної машини?
- Яку роль виконує **мікроконтролер** у роботі робота?
- Що таке **Micro:Bit**? Навіщо він потрібен?
- Який факт із сьогоднішнього уроку вас **найбільше здивував**?

---

## 🏠 Домашнє завдання

Опрацювати підручник — відповідний параграф.

**У зошиті:** знайти **два приклади** роботів, що використовуються сьогодні (не у кіно!).

Для кожного записати:

- 🏷️ Назву та призначення
- 📍 Де використовується
- 🔧 Які датчики або маніпулятори, імовірно, є у цього робота
