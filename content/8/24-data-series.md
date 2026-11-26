---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 24
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
  .notebook {
    background-color: #f1f8e9;
    border-left: 6px solid #8bc34a;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
  }
  .notebook::before {
    content: "✍️ Запишіть у зошит";
    display: block;
    font-size: 0.8em;
    font-weight: bold;
    color: #558b2f;
    margin-bottom: 5px;
  }

---

# Зображення рядів даних

## 🏫 Урок **24**

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

## 🎯 Сьогодні ми дізнаємося

- 🔁 Як додати діаграму та налаштувати її основні складові (повторення).
- 📊 Що таке **ряди даних** і **категорії** діаграми.
- 🔀 Як додавати ряди та міняти місцями рядки й стовпці.
- 🎨 Як змінити вигляд окремого ряду, точки чи осі діаграми.

---

## 🕷️ Що це за малюнок?

<div class="grid-container">
<div class="image-center">

![h:480px](./assets/24/spider-chart.svg)

</div>
<div class="text-medium-small text-left">

🤔 Як ви думаєте, **де** намальовано цей малюнок?

<div class="important-to-remember text-small">

💡 Це **діаграма** з електронної таблиці! Вона складається з 10 графіків — кожен із них окремий **ряд даних** зі своїм кольором.

</div>

🏠 Як отримати такий малюнок — дізнаєтеся вдома (ДЗ за бажанням).

</div>
</div>

---

## 🎬 Дивимося відео (1–4)

<div class="grid-container">
<div class="card image-center text-small">

**1. Як додати діаграму**
⏱️ 1:46

![w:150px](./assets/24/qr-video-1.svg)

▶️ <a href="https://www.loom.com/share/cf393c65edc14185b39b54bb2e493527" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**2. Налаштовуємо зовнішній вигляд**
⏱️ 2:33

![w:150px](./assets/24/qr-video-2.svg)

▶️ <a href="https://www.loom.com/share/e3f7a424082c416a83fd325ba84d98c9" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**3. Ряди даних і категорії**
⏱️ 2:06

![w:150px](./assets/24/qr-video-3.svg)

▶️ <a href="https://www.loom.com/share/a9c707b52da24cf7aa1dfe5b23143675" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**4. Міняємо місцями рядки і стовпці**
⏱️ 1:15

![w:150px](./assets/24/qr-video-4.svg)

▶️ <a href="https://www.loom.com/share/e71127d2093448ca8a360b7761b943b9" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
</div>

<div class="important-to-remember text-small">

🎧 Навушники! Під час перегляду знайдіть відповіді: **1)** що таке ряд даних; **2)** де змінити колір лінії ряду. 📱 QR-код відкриває відео на телефоні.

</div>

---

## 🎬 Дивимося відео (5–8)

<div class="grid-container">
<div class="card image-center text-small">

**5. Діаграма як об'єкт**
⏱️ 0:58

![w:150px](./assets/24/qr-video-5.svg)

▶️ <a href="https://www.loom.com/share/e6d43ceb0c2e48ada4b7de7b050f77c7" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**6. Оформлення рядів**
⏱️ 1:14

![w:150px](./assets/24/qr-video-6.svg)

▶️ <a href="https://www.loom.com/share/e8befe92c28f4412bd28112a2279f5ec" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**7. Осі**
⏱️ 1:31

![w:150px](./assets/24/qr-video-7.svg)

▶️ <a href="https://www.loom.com/share/46d3d03d334b450e93af6e0afc4080f0" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
<div class="card image-center text-small">

**8. Швидке налаштування діаграми**
⏱️ 0:48

![w:150px](./assets/24/qr-video-8.svg)

▶️ <a href="https://www.loom.com/share/f94c33c123b84e8ebe68315a9651c980" target="_blank" rel="noopener noreferrer">Дивитися</a>

</div>
</div>

<div class="important-to-remember text-small">

⏩ Не встигаєте? Увімкніть швидкість **1,2×** у налаштуваннях відео.

</div>

---

## 📌 Головне

<div class="notebook text-small text-left">

- **Ряд даних** — набір значень однієї величини, які на діаграмі зображено однаково (одним кольором, однією лінією). Назва ряду — у **легенді**.
- **Категорії** — підписи значень на горизонтальній осі.
- Додати діаграму: виділити дані **разом із заголовками** → **Вставлення → Діаграма**.
- **Редактор діаграм**: *Налаштування* — **що** показує діаграма (тип, дані, ряди); *Оформлення* — **як** вона виглядає (заголовки, легенда, ряди, осі).
- Швидкий спосіб — **двічі клацнути** потрібну складову діаграми.

</div>

---

<section class="task">

## 🧩 Завдання 1: Лікарня діаграм 🏥

<div class="text-small">

Відкрий <a href="https://kahoot.it" target="_blank" rel="noopener noreferrer">kahoot.it</a>, введи **PIN-код** від вчителя та своє ім'я. Для кожної «хворої» діаграми обери **діагноз** 🩺 і **лікування** 💊.

</div>

<div class="grid-container">

![w:340px](./assets/24/chart-a.svg)
![w:340px](./assets/24/chart-b.svg)

</div>
<div class="grid-container">

![w:340px](./assets/24/chart-c.svg)
![w:340px](./assets/24/chart-d.svg)

</div>

</section>

---

<section class="task">

## ⌨️ Завдання 2: Кліматичний паспорт Києва 🌡️

<div class="grid-container text-tiny">
<div>

1. 📋 Відкрий <a href="https://docs.google.com/spreadsheets/d/1mtVacPisTTuriM2e_nYk9ZwrAJSqsfCwxG4YGYSDqHU/copy" target="_blank" rel="noopener noreferrer">таблицю з даними</a> і натисни **Зробити копію**.
2. ✏️ Перейменуй копію на `Урок24_Прізвище`.

У таблиці вже є середня температура в Києві (°C) по місяцях — `A1:C13`:

| Місяць | Вдень | Вночі |
|---|---|---|
| Січ | -1 | -6 |
| … | … | … |
| Лип | 27 | 17 |
| … | … | … |
| Гру | 1 | -4 |

</div>
<div class="text-small">

### 🟢 Середній
1. Побудуй діаграму **Графік** з двома рядами.
2. Назва «Клімат Києва: температура вдень і вночі», осі «Місяць» і «Температура, °C», легенда **знизу**.

### 🟡 Достатній
1. `D1` — `Середня`, `D2` — `=AVERAGE(B2:C2)`, скопіюй до `D13`.
2. **Додай ряд** «Середня» до діаграми.
3. Кольори: «Вдень» 🔴, «Вночі» 🔵, «Середня» ⚪ **пунктир**; точки 7 px.

</div>
</div>

</section>

---

<section class="task">

## ⌨️ Завдання 2 (продовження)

### 🔴 Високий

<div class="text-medium-small">

1. 🏷️ Увімкни **мітки даних** для ряду «Вдень».
2. 🌞 Виділи найтеплішу точку (липень) іншим кольором і більшим розміром: *Ряд даних → Форматувати точку даних → Додати*.
3. 🔀 Скопіюй діаграму (`Ctrl+C` / `Ctrl+V`). У копії **поміняй місцями рядки й стовпці** і зміни тип на **стовпчасту**.
4. ✍️ У `F1` запиши: скільки рядів даних стало і яка з двох діаграм краще показує зміну температури протягом року?

</div>

</section>

---

## 🏠 Домашнє завдання

<div class="text-medium-small">

1. 📖 Опрацювати конспект уроку.
2. 📚 Опрацювати матеріали підручника **с. 96–98**.
3. 🌡️ Завершити практичну роботу «Кліматичний паспорт Києва» (до 🟡 достатнього рівня включно).
4. 🕷️ *(За бажанням)* Завдання 14 (с. 96): побудувати в Google Таблицях графіки функцій (крок 0,5) на одній діаграмі й з'ясувати, яке зображення вони утворюють.

</div>
