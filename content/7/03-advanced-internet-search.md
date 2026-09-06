---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
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

# 🔎🌐 Пошук інформації в інтернеті

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

- 🔍 Які бувають види пошуку в інтернеті
- 🧩 Чинні оператори мови запитів Google
- 🛠️ Стратегію ефективного розширеного пошуку
- ✏️ Як застосувати оператори пошуку на практиці

---

## 🗣️ Актуалізація знань

<div class="card">

Опитування та перевірка домашнього завдання.

</div>

---

## 💡 «Хто володіє інформацією, той володіє світом»

<div class="text-medium text-left">

В інтернеті — мільярди сторінок.

❓ Як серед них швидко знайти саме те, що потрібно?

</div>

---

## 🗂️ Які бувають види пошуку?

- 📝 **Простий** — за одним чи кількома ключовими словами
- 🧠 **Контекстний** — за точним висловом (у лапках)
- ⚙️ **Розширений** — комбінація ключових слів з операторами

---

## 📝 Простий пошук

<div class="grid-container">
  <div class="text-left text-medium">

Простий пошук знаходить сторінки, що містять будь-яке слово з пошукового запиту. Використовують для нескладних, однозначних питань.

  </div>

  <div class="image-center">

![w:500px](./assets/03/simple-search-example.png)

  </div>
</div>

---

## 🧠 Контекстний пошук

<div class="grid-container">
  <div class="text-left text-medium">

Контекстний пошук знаходить сторінки, що **точно** відповідають пошуковому запиту.<br>
Для контекстного пошуку фразу беруть у лапки `" "`.

  </div>

  <div class="image-center">

![w:500px](./assets/03/context-search-example-1.png)

  </div>
</div>

---

## ⚙️ Розширений пошук

<div class="grid-container">
  <div class="text-left text-medium">

[Розширений пошук Google](https://www.google.com/advanced_search) дозволяє точно налаштувати параметри пошукового запиту.

Скористатися ним можна двома способами: перейти на сторінку google.com/advanced_search або використовувати оператори мови запитів прямо в рядку пошуку.

  </div>

  <div class="image-center">

![w:500px](./assets/03/advanced-search-example.png)

  </div>
</div>

---

## 🧩 Чинні оператори мови запитів Google

<section class="text-small">

| Оператор | Призначення | Приклад |
| -------- | ----------- | ------- |
| " "      | 🔎 Точний вислів (контекстний пошук) | "інформатика 7 клас" |
| -        | ➖ Сторінка не має містити слово (без пробілу перед словом) | ігри -онлайн |
| site:    | 🌍 Пошук на конкретному сайті | site:wikipedia.org "озеро Світязь" |
| filetype: | 📄 Пошук файлів певного типу | "інформатика" filetype:pdf |
| OR або \| | 🔀 Хоча б одне зі слів | ноутбук OR планшет |
| *        | ✨ Будь-яке слово замість зірочки (у фразі) | "інформатика \* клас" |

</section>

<div class="card text-tiny">

💡 Слова через пробіл (наприклад, <code>інформатика алгоритми</code>) пошукова система і без операторів шукає разом — окремий оператор «AND» не потрібен.

</div>

---

## 🛠️ Стратегія ефективного розширеного пошуку

<section class="text-medium-small">

1. 🎯 **Визначити мету пошуку** — що саме потрібно знайти
2. 🔎 **Обрати пошукову систему**
3. ⌨️ **Сформувати запит** з ключовими словами й операторами
4. ▶️ **Здійснити пошук** і оцінити релевантність результатів
5. 🔬 **За потреби деталізувати запит** — додати уточнювальні слова

</section>

---

## 📝✨ Практичне завдання (5-7 хв)

<section class="text-medium">

1. 🌐 Знайдіть у Google інформацію про "найбільше озеро України" так, щоб у результатах були тільки сторінки з сайту wikipedia.org.
   - Використайте оператор: `site:wikipedia.org "найбільше озеро України"`
2. 🍕 Знайдіть у Google рецепти піци, але виключіть сторінки, де згадується слово "гриби".
   - Використайте оператор: `рецепт піци -гриби`
3. 📊 Знайдіть у Google файли презентацій про інформатику у форматі PowerPoint.
   - Використайте оператор: `презентація інформатика filetype:pptx`

</section>

---

## 🔀🐱 Практичне завдання: OR та розширений пошук

<section class="task text-medium">

1. Складіть запит з оператором `OR` (наприклад, `ноутбук OR планшет`) і порівняйте результати із запитом без нього.
2. Спробуйте розширений пошук Google, щоб знайти зображення кота, які можна використовувати безкоштовно (з ліцензією для повторного використання).

</section>

---

## 🤔 Рефлексія

- Який оператор пошуку виявився для вас найкориснішим і чому?
- Чи змінилося ваше уявлення про те, скільки часу можна заощадити, правильно сформулювавши запит?

---

## 🏠📚 Домашнє завдання

У зошиті напиши пошукові запити для таких пошуків:

1. 🏔️ Знайдіть у Google інформацію про "найвища гора України" лише на сайті wikipedia.org.
2. 🚀 Знайдіть у Google цікаві факти про космос, але виключіть сторінки, де згадується слово "NASA".
3. 📄 Знайдіть у Google презентації про інформатику у форматі PowerPoint (файли з PowerPoint зазвичай мають розширення pptx).
