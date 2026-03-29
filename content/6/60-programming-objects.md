---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 6 клас
header: 🏫 Урок 60
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

# 🤖 Поняття про об’єкт у програмуванні

## 🏫 Урок **60**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке **програмний об’єкт**.
- 🔧 Які **властивості** має об’єкт у Scratch.
- ✏️ Як створювати та змінювати об’єкти за допомогою коду.

---

## 🤔 Що таке об’єкт?

У реальному житті нас оточують об’єкти: стіл, книга, кіт, автомобіль.
Кожен об’єкт має:
1. **Назву** (хто це або що це?)
2. **Властивості** (який він?)
3. **Дії** (що він робить?)

---

## 💻 Програмний об’єкт

У програмуванні **об’єкт** — це частина програми, яка має своє ім’я, властивості та дії, які він може виконувати.

У середовищі Scratch програмні об’єкти називають **спрайтами**.

---

## 📊 Властивості спрайта у Scratch

<section class="text-medium-small">

| Властивість | Що описує |
| :--- | :--- |
| **Положення (X, Y)** | Місце на сцені |
| **Напрямок** | Кут повороту |
| **Розмір** | Масштаб (у %) |
| **Образ** | Зовнішній вигляд |
| **Видимість** | Показати/Сховати |

</section>

---

## 🛠️ Як змінити властивості програмно?

<section class="grid-container">
<div class="card text-small">

**Рух:**
`перемістити в x: ... y: ...`
`повернути в напрямку ...`

</div>
<div class="card text-small">

**Вигляд:**
`змінити розмір на ...`
`наступний образ`
`змінити ефект колір на ...`

</div>
</section>

---

## 🖱️ Практичне завдання "Чарівний Спрайт"

<section class="task text-medium-small">

1. Додайте новий спрайт з бібліотеки.
2. Змініть його назву та початковий розмір (на 80) вручну.
3. Складіть скрипт:
   - Коли натиснуто 🟢
   - Завжди:
     - `змінити розмір на 10`
     - `чекати 0.5 сек`
     - `змінити розмір на -10`
     - `змінити ефект колір на 25`
     - `чекати 0.5 сек`

</section>

---

## 🗣️ Рефлексія

- Що таке програмний об'єкт?
- Як називаються об'єкти у Scratch?
- Які властивості ми сьогодні навчилися змінювати кодом?

---

## 🏠 Домашнє завдання

- Опрацювати матеріал підручника c. 203-208.
