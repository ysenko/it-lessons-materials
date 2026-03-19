---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 59
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

---

# Етапи побудови комп’ютерної моделі. Проведення експерименту

## 🏫 Урок **59**

---

## 🎯 Сьогодні ми дізнаємося

- 🧪 Що таке «комп'ютерний експеримент».
- 🗺️ Як використовувати готові онлайн-сервіси (Google Карти) як комп'ютерну модель.
- 🔍 Як аналізувати результати та робити висновки.

---

## 🧪 Що таке комп'ютерний експеримент?

<div class="card text-medium important-to-remember">

**Комп'ютерний експеримент** — це процес дослідження моделі за допомогою комп'ютера.

</div>
<div class="card text-medium">

Під час експерименту ми постійно **змінюємо вхідні дані** (умови) та спостерігаємо, як **змінюється результат**. Це дозволяє передбачати майбутнє без реальних витрат і ризиків!

</div>

---

## 🏗️ Як провести компʼютерний експеримент?

<div class="text-medium-small">

Не можна просто сісти за комп'ютер і почати "щось робити". Потрібен чіткий план!

</div>
<div class="grid-container">
 <div class="grid-item important-to-remember text-small">

**5 етапів компʼютерного експерименту:**

1. **Постановка задачі** (Що ми хочемо дізнатися?).
2. **Побудова інформаційної моделі** (Які дані нам потрібні?).
3. **Створення комп’ютерної моделі** (Робота в програмі або сервісі).
4. **Проведення комп’ютерного експерименту** (Тестування моделі).
5. **Аналіз результатів** (Робимо висновки).

  </div>
  <div class="grid-item image-center">

![h:380px](./assets/59/computer_experiment_stages.jpg)

  </div>

</div>

---

## 💻 Практична частина (Етапи 1–2)

<div class="task text-small">

**Експеримент: Найшвидший шлях до столиці 🇺🇦**

*Уявіть, що ми плануємо подорож зі своєї школи до Майдану Незалежності в Києві. Наша мета — провести комп'ютерний експеримент у Google Картах, щоб визначити, як різні види транспорту та час відбуття впливають на час у дорозі.*

**Етапи 1–2 (Підготовка):**

- **Точка старту:** Ваша школа.
- **Точка фінішу:** Майдан Незалежності, Київ.
- **Змінні (те, що будемо міняти):** Вид транспорту, Час відбуття.
- **Що шукаємо:** Час у дорозі.

</div>

---

## 🚀 Хід експерименту (Етапи 3–4)

<div class="grid-container">

<div class="text-small grid-item">

1. Відкрийте **[Google Карти](https://www.google.com/maps)** (maps.google.com).
2. У пошуку введіть "Майдан Незалежності".
3. Натисніть **"Маршрути"**. Введіть точку відправлення "Школа 30, Львів".
4. Створіть у зошиті таблицю результатів:

| Транспорт | Час (зараз) | Час (завтра, 8:00) | Час (завтра, 23:00) |
|---|---|---|---|
| Автомобіль |  |  |  |
| Громадський |  |  |  |

5. **Експериментуйте!** Змінюйте вид транспорту та час відправлення ("Відправлення в..."). Записуйте результати.
6. Дайте відповіді на запитання на наступному слайді.

</div>
<div class="grid-item image-center text-small">

1. Змініть час відправлення

  ![h:200px](./assets/59/experiment_step_1.png)

2. Оберіть дату і час відправлення

  ![h:200px](./assets/59/experiment_step_2.png)

</div>
</div>

---

## 🔍 Аналіз результатів (Етап 5)

<div class="card text-medium-small">

Подивіться на свою заповнену таблицю і дайте відповіді:

1. Який вид транспорту є найшвидшим *зараз*?
2. Як змінюється час у дорозі на автомобілі вранці (о 8:00) та вночі (о 23:00)? **Чому так відбувається?**
3. Чи вдалося нам за допомогою комп'ютерної моделі (Google Карт) виконати поставлену задачу та знайти найшвидший шлях?

</div>
