---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 03
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

---

# 🌐✨ Використовуємо інтернет

## 🏫 Урок **03**

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

- 🌐 Хто керує інтернетом і чому в нього немає єдиного власника
- 🔌 Як підключитися до інтернету
- 🕰️ Досліджуємо перший вебсайт в історії людства

---

## ⚡ Бліц-опитування

<section class="text-medium">

1. Що перетворює доменне ім'я сайту на IP-адресу?
2. Наведіть приклад домену верхнього рівня.
3. Яку відповідальність може нести людина за порушення законів у цифровій сфері?
4. А хто, на вашу думку, встановлює правила для доменних імен та адрес в інтернеті?

</section>

---

## 🤔 А хто насправді керує інтернетом?

<div class="card text-medium-small">

Часто можна почути: **«Інтернетом керує одна велика компанія (або одна країна), яка може будь-що вимкнути чи заборонити»**.

</div>

> ❓ Чи згодні ви з цим твердженням? Хто, на вашу думку, насправді відповідає за роботу інтернету?

Насправді інтернет **не має єдиного власника** — він децентралізований і складається з мереж, що належать тисячам організацій, компаній і людей у всьому світі. 🌍

---

## 🔌 Як підключитися до інтернету?

<div class="grid-container">
  <div class="text-left text-small">

**Інтернет-провайдер** (Internet Service Provider, ISP) забезпечує доступ до мережі «Інтернет» та пов'язаних з нею послуг.

- ☎️ DSL: підключення через телефонну лінію
- 📺 Cable: підключення через кабельну мережу
- 🧵 PON: підключення через оптоволоконний кабель
- 🛰️ Супутник: підключення через супутниковий сигнал
- 📱 Мобільна мережа: підключення через 4G/5G мережу

  </div>

  <div class="image-center">

![w:400px](./assets/03/various-internet-connections.png)

  </div>
</div>

---

## 🏢 Хто керує інтернетом?

<div class="grid-container">
<div class="grid-item text-medium-small">🌐 <b>ICANN</b><br>управління доменними іменами та IP-адресами</div>
<div class="grid-item text-medium-small">🧑‍🔬 <b>IETF</b><br>стандарти інтернету, як-от TCP/IP</div>
<div class="grid-item text-medium-small">🕸️ <b>W3C</b><br>стандарти Всесвітньої павутини — HTML, CSS</div>
<div class="grid-item text-medium-small">🌍 <b>ISOC</b><br>підтримка розвитку інтернету для всіх людей у світі</div>
</div>

---

## 🏆 Цікаві факти про організації

<section class="text-medium">

- 🌐 **ICANN** заснована у 1998 році, штаб-квартира — у Лос-Анджелесі, США.
- 🧑‍🔬 **IETF** — відкрита група, до якої може приєднатися будь-хто.
- 🕸️ **W3C** створив сер Тім Бернерс-Лі — винахідник Всесвітньої павутини.
- 🌍 **ISOC** підтримує освітні програми з розвитку інтернету у світі.

</section>

---

## 🌟 Цікаві факти про інтернет

<section class="text-medium-small">

- 🌍 Понад 5 мільярдів людей у світі користуються інтернетом.
- 🔎 Щосекунди в Google виконується понад 100 000 пошукових запитів.
- 📨 Перший електронний лист був надісланий у 1971 році.
- 🏛️ Перший вебсайт було створено в 1991 році — і він **досі працює**: [info.cern.ch](http://info.cern.ch)
- 🚀 Найшвидший інтернет у світі — понад 3000 Гбіт/с (Японія, 2022).

</section>

---

## 🧠 Вікторина «Правда чи міф?» — Classtime

<span class="emoji-large">📱</span>

---

## 🕹️ Квест: подорож у 1991 рік

<section class="task text-medium-small">

Відкрийте в парі сайт [info.cern.ch](http://info.cern.ch) — перший вебсайт в історії — і дайте відповіді:

1. Прочитайте текст на головній сторінці. Якою фразою він починається?
2. Відкрийте посилання **«Browse the first website»**. Яким заголовком (H1) підписана ця сторінка?
3. Знайдіть на ній посилання **«History»** і відкрийте його — це хронологія проєкту. Яку подію позначено датою **«March 1989»**? А що відбулося на **«Christmas 1990»**?
4. Порахуйте зображення, кольори та кнопки на сторінці «The World Wide Web project». Порівняйте з головною сторінкою будь-якого сучасного сайту.
5. Поверніться на info.cern.ch і спробуйте посилання **«Browse the first website using the line-mode browser simulator»**. Одним реченням опишіть, чим цей спосіб перегляду відрізняється від сучасного браузера.

</section>

---

## 🏠 Домашнє завдання

<section class="text-medium-small">

1. 📖 Опрацювати підручник, с. 12–14 (Крок 1–2; Крок 3 переглянути ознайомчо)
2. 🖥️ Переглянути презентацію уроку

</section>
