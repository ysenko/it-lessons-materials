---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 20
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
  .centered {
    text-align: center;
  }
---

# 📊 Опрацювання табличних даних

## 🏫 Урок **20**

---

## 🧠 Актуалізація знань

**Дайте відповіді на запитання:**

1. З якого знака починається запис будь-якої формули в Excel?
2. Чим функція відрізняється від звичайної формули (наприклад, `A1+A2+...`)?
3. Які типи даних можуть зберігатися в клітинках таблиці?

---

## 📘 Що таке функція?

<div class="important-to-remember text-medium">

**Функція** — це заздалегідь визначена формула, яка виконує обчислення за заданими величинами (аргументами) у певному порядку.

</div>

<div class="card text-medium-small">

**Синтаксис:**
`=НАЗВА_ФУНКЦІЇ(аргумент1; аргумент2; ...)`

<small>Примітка: у Excel/Google Sheets для української локалі аргументи розділяються крапкою з комою (;).</small>

</div>

---

## 🛠 Як вставити функцію?

1. **Вручну** ✍️
   Введіть назву функції після знака `=` у клітинці.
2. **Через меню**
   Виберіть: **Вставити → Функція**.

---

## 🖼️ Приклад вставки функції через меню

<div class="image-center">

![h:450px](./assets/20/add-formula-via-the-menu.png)

</div>

---

## 🔢 Математичні функції

<div class="card text-medium-small">

- **`SUM`** — сума чисел у діапазоні
  _Приклад:_ `=SUM(A1:A10)`
- **`PRODUCT`** — добуток чисел
  _Приклад:_ `=PRODUCT(A1:A10)`
- **`ROUND`** — округлення числа
  _Приклад:_ `=ROUND(B2; 2)` (до 2 знаків після коми)

</div>

---

## 📊 Статистичні функції (1/2)

<div class="card text-medium-small">

- **`AVERAGE`** — середнє арифметичне
- **`MIN`** — мінімальне значення
- **`MAX`** — максимальне значення

</div>

---

## 📊 Статистичні функції (2/2)

<div class="important-to-remember text-medium-small">

**`COUNTIF`** — підраховує кількість клітинок, які відповідають певній умові.

</div>

<div class="card text-medium-small">

_Приклад:_ Порахувати, скільки товарів коштують більше 1000 грн:
`=COUNTIF(C2:C20; ">1000")`

<small>Примітка: у Google Sheets/Excel англійською локаллю — кома, українською — крапка з комою.</small>

</div>
