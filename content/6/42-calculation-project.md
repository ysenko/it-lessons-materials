---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 42
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

# Обчислення з числовими даними електронної таблиці

## 🏫 Урок **42**

---

## 🎯 Сьогодні ми дізнаємося

- 🧮 Як створювати формули з використанням арифметичних операцій.
- 🔗 Чому важливо використовувати посилання на клітинки замість звичайних чисел.
- 🎨 Як форматувати таблиці та працювати над проєктом "Мій шкільний ярмарок".

---

## 🧠 Згадаємо минулий урок

<div class="grid-container text-medium-small">
  <div class="grid-item">

**1.** Які формати даних ми вивчали? (Текст, Число, Грошовий, Відсотки...)

  </div>
  <div class="grid-item">

**2.** Як змінити колір клітинки або додати межі таблиці?

  </div>
  <div class="grid-item">

**3.** Що таке "адреса клітинки" і як вона виглядає?

  </div>
</div>

---

## ✍️ Занотуйте в зошит

**Головні правила обчислень:**

<div class="important-to-remember text-medium-small">

1. Будь-яка формула **ЗАВЖДИ** починається зі знака **`=`** (дорівнює).
2. Використовуйте **адреси клітинок** (наприклад, `=A1+B1`), а не просто числа. Тоді при зміні числа в клітинці результат перерахується автоматично!
3. Основні арифметичні дії:
   - **`+`** (додавання)
   - **`-`** (віднімання)
   - **`*`** (множення)
   - **`/`** (ділення)

</div>

---

## 💻 Практична робота: Проєкт

<div class="grid-container borderless">
  <div class="grid-item">
    <span class="emoji-large">🎪</span>

### "Мій шкільний ярмарок"

Сьогодні ми створимо електронну таблицю для розрахунку прибутку від продажу товарів на уявному шкільному ярмарку. Уважно читайте завдання та переходьте від простішого до складнішого.

  </div>
</div>

---

## 🛠️ Практичне завдання (Етап 1)

<div class="grid-container">
<div class="task text-small grid-item">

### ⭐️ Рівень "Достатній" (до 6 балів)

1. Відкрийте програму для роботи з електронними таблицями.
2. Створіть таблицю на 3 стовпці з заголовками: **Товар**, **Ціна**, **Кількість**.
3. Заповніть 4 рядки будь-якими товарами (наприклад: Торт, Кекс, Браслет, Сік).
4. Додайте межі до таблиці та зробіть заголовок жирним шрифтом.
5. Введіть довільні числа в стовпці "Ціна" та "Кількість".

</div>
<div class="grid-item">

### Зразок

<div class="image-center">

![w:500px](./assets/42/lvl-1.png)

</div>
</div>
</div>

---

## 🛠️ Практичне завдання (Етап 2)

<div class="grid-container">
<div class="task text-small grid-item">

### ⭐️⭐️ Середній рівень (до 9 балів)

1. **Виконайте завдання початкового рівня.**
2. Додайте 4-й стовпець і назвіть його **"Разом"**.
3. У стовпці "Разом" напишіть формулу множення **Ціни** на **Кількість**.
4. Використайте **автозаповнення** (потягніть за маркер у правому нижньому кутку клітинки), щоб швидко скопіювати формулу для всіх товарів.
5. Встановіть для стовпців "Ціна" та "Разом" **Грошовий формат** (грн).
6. Відформатуйте межі та кольори відповідно до зразка.

</div>
<div class="grid-item">

### Зразок

<div class="image-center">

![w:500px](./assets/42/lvl-2.png)

</div>
</div>
</div>

---

## 🛠️ Практичне завдання (Етап 3)

<div class="grid-container">
<div class="task text-small grid-item">

### ⭐️⭐️⭐️ Високий рівень (до 12 балів)

1. **Виконайте попередні завдання.**
2. Додайте 5-й стовпець **"Знижка 10%"**. Обчисліть суму знижки за формулою (наприклад: `=D2 * 10%`).
3. Додайте 6-й стовпець **"До сплати"**, де відніміть знижку від загальної суми.
4. Внизу таблиці зробіть підпис **"Загальна сума виручки"** та порахуйте суму всіх товарів (можна використати функцію `SUM`).
5. Відформатуйте таблицю відповідно до зразка.

</div>
<div class="grid-item">

### Зразок

<div class="image-center">

![w:500px](./assets/42/lvl-3.png)

</div>
</div>
</div>
