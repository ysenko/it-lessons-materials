---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 9 клас
header: 🏫 Урок 22
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

# Особливості пошуку інформації з використанням ШІ

## 🏫 Урок **22**

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

## 🎯 Сьогодні ми

- 🧪 Самі з'ясуємо, чим **ШІ-пошук** відрізняється від **звичайного пошуку**.
- ⚙️ Розберемо **модель роботи ШІ-пошукача**.
- ⚠️ Дізнаємося, де ШІ може показати **рекламу**, дати **неповну відповідь** чи **помилитися**.
- 🤝 Порівняємо: що краще вміє **людина**, а що — **ШІ**.
- 🔬 Проведемо **власне дослідження** і побудуємо діаграму.

---

## 🧪 Міні-експеримент: Google чи ШІ?

<div class="card text-medium-small text-left">

🔎 Введіть **той самий запит** спочатку в <a href="https://www.google.com" target="_blank" rel="noopener noreferrer">Google</a>, потім у <a href="https://www.perplexity.ai" target="_blank" rel="noopener noreferrer">Perplexity</a>:

**«Найкращий смартфон для школяра до 10000 грн»**

</div>

<div class="important-to-remember text-medium-small text-left">

🤔 Знайдіть відповіді:

1. 📋 Де ви одразу отримали **готову відповідь**, а де — **список посилань**?
2. 🛒 Чи є **реклама** або назви конкретних **магазинів і брендів**?
3. ⚖️ Чи **збігаються** відповіді?

</div>

---

## 🔍 Класичний пошук і ШІ-пошук

<div class="text-small">

| | 🔎 Класичний пошук (Google, Bing) | 🤖 ШІ-пошук (Perplexity, ChatGPT, Copilot) |
|---|---|---|
| **Результат** | Список посилань | Готова відповідь своїми словами |
| **Хто обирає джерела** | 🙋 Людина | 🤖 ШІ |
| **Джерела** | Видно одразу | Не завжди або лише кілька |
| **Запит** | Ключові слова | Звичайне запитання, можна уточнювати в діалозі |
| **Ризик** | Реклама, багато зайвого | Реклама, неповна відповідь, галюцинації |

</div>

<div class="important-to-remember text-medium-small text-left">

💡 ШІ-пошук **зручний**, але тепер **ШІ вирішує за нас**, які джерела важливі.

</div>

---

## 🧩 Як «думає» ШІ-пошукач?

<div class="card text-medium-small text-left">

🔀 Розставте кроки роботи ШІ-пошукача **у правильному порядку**:

</div>

<div class="grid-container text-medium-small">
<div class="grid-item">🖥️ Виведення</div>
<div class="grid-item">🌐 Вибір джерел</div>
<div class="grid-item">❓ Запит</div>
<div class="grid-item">✍️ Формування відповіді</div>
<div class="grid-item">🔬 Аналіз</div>
</div>

---

## ⚙️ Модель роботи ШІ-пошукача

<div class="important-to-remember text-medium-small">

**❓ Запит → 🔬 Аналіз → 🌐 Вибір джерел → ✍️ Формування відповіді → 🖥️ Виведення**

</div>

<div class="card text-small text-left">

- ❓ **Запит** — користувач ставить запитання.
- 🔬 **Аналіз** — ШІ визначає ключові слова, тон і **намір** запиту.
- 🌐 **Вибір джерел** — ШІ шукає та обирає сторінки в інтернеті.
- ✍️ **Формування відповіді** — мовна модель складає текст на основі обраних джерел.
- 🖥️ **Виведення** — ми бачимо відповідь (іноді з посиланнями).

</div>

---

## ⚠️ Де виникає упередженість ШІ?

<div class="card text-medium-small text-left">

🤔 **На якому кроці ШІ може нас підвести?**

</div>

<div class="grid-container">
<div class="card text-small text-left">

🔬 **Аналіз**

🛒 Може показати **рекламу**: комерційний запит → комерційні джерела.

</div>
<div class="card text-small text-left">

🌐 **Вибір джерел**

🧩 Може дати **неповну відповідь**: обирає **популярне**, а не перевірене; бере лише кілька джерел.

</div>
<div class="card text-small text-left">

✍️ **Формування відповіді**

🌀 Може **помилитися** або **вигадати** (галюцинація), неточно переказати джерело.

</div>
</div>

---

## 🤝 Людина і ШІ: хто сильніший?

<div class="text-small">

| Критерій | 🙋 Людина | 🤖 ШІ |
|---|---|---|
| **Розуміння запиту** | Враховує контекст і приховані наміри | Аналізує ключові слова й шаблони |
| **Вибір джерел** | Обирає перевірені джерела | Широкий спектр, іноді комерційні |
| **Перевірка** | Сумнівається, порівнює, уточнює | Не завжди перевіряє, може «галюцинувати» |
| **Швидкість** | 🐢 Повільніше | ⚡ Майже миттєво |

</div>

<div class="important-to-remember text-medium-small text-left">

🏆 Найкращий результат — **людина + ШІ разом**: ШІ швидко знаходить, людина **оцінює й перевіряє**.

</div>

---

<section class="task">

## 🎲 Завдання 1: Як шукає ШІ?

<div class="text-medium text-left">

1. 🌐 Відкрийте <a href="https://kahoot.it/" target="_blank" rel="noopener noreferrer">kahoot.it</a>.
2. 🔢 Введіть **PIN гри**, який назве вчитель.
3. 🙋 Нікнейм — **ім'я та перша літера прізвища**.
4. ✅ Оберіть правильну відповідь на кожне питання.

</div>

<div class="card text-medium-small text-left">

⚡ Що швидше й точніше відповідаєте — то більше балів!

</div>

</section>

---

<section class="task">

## 🔬 Завдання 2: Чи завжди ШІ-пошук дає точну інформацію?

<div class="text-tiny text-left">

👥 **В парах**: номер пари = номер запиту. Поставте запит **без змін** у <a href="https://www.perplexity.ai" target="_blank" rel="noopener noreferrer">Perplexity</a>, <a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">ChatGPT</a> і <a href="https://copilot.microsoft.com" target="_blank" rel="noopener noreferrer">Copilot</a>. 🔐 Не входьте в акаунти (і не тисніть «Продовжити з Google») — якщо система вимагає вхід, пропустіть її.

| № | Запит | ✔️ Як перевірити |
|---|---|---|
| 1 | Яка найвища гора України та яка її висота? | Говерла, 2061 м |
| 2 | Яка столиця Австралії? | Канберра (не Сідней) |
| 3 | Чи правда, що людина використовує лише 10 % мозку? | Ні, це міф |
| 4 | Хто автор повісті «Тіні забутих предків» і коли її написано? | Михайло Коцюбинський, 1911 р. |
| 5 | Скільки областей в Україні? | 24 + АР Крим, Київ, Севастополь |
| 6 | Яка найдовша річка України? | Дніпро, 2201 км (в Україні ≈ 980 км) |
| 7 | Хто зараз є президентом США? | Дональд Трамп (з 2025 р.) |
| 8 | Хто винайшов електричну лампочку? | Не одна людина: Едісон, Свон та інші |

</div>

</section>

---

<section class="task">

## 📊 Завдання 2: рівні

<div class="grid-container">
<div class="card text-tiny text-left">

🟡 **Середній.** Створіть таблицю за посиланням <a href="https://sheets.new" target="_blank" rel="noopener noreferrer">sheets.new</a> (одна на пару), назва — **«Урок 22. ШІ-пошук»**. Таблиця — з клітинки **A1**:

| Система | Кількість джерел у відповіді | Якість результату (1–3) |
|---|---|---|
| Perplexity | | |
| ChatGPT | | |
| Copilot | | |

🔗 **Джерела** — сайти, які ШІ показав **у своїй відповіді** (виноски, кнопка «Джерела» / «Sources»). Немає — **0**.

⭐ **Якість:** **3** — правильно і повно · **2** — правильно, але неповно · **1** — помилка, вигадка або немає відповіді.

</div>
<div class="card text-tiny text-left">

🟢 **Достатній.**

1. 🖱️ Виділіть таблицю **A1:C4** → **Вставка → Діаграма** → тип **«Стовпчаста діаграма»**.
2. 🏷️ Назва діаграми — **номер і текст запиту**.
3. ✍️ Під таблицею запишіть **висновок** (1–2 речення):
   - яка система дала **найкращий результат**;
   - чи траплялися **помилки**;
   - чи пов'язана **якість** відповіді з **кількістю джерел**.

</div>
</div>

</section>

---

## 🏠 Домашнє завдання

<div class="card text-medium-small text-left">

1. 📝 Опрацювати конспект уроку.
2. 📖 Опрацювати матеріали підручника **с. 72–75**.
3. 🎨 Уявіть, що ви — **ШІ**. Оберіть просте запитання (наприклад, «Що таке фейк?») і намалюйте в будь-якому графічному редакторі **власну мінімодель** відповіді на нього: які **джерела** перевіряєте, як вирішуєте, що **включити у відповідь**, як перевіряєте **достовірність**.

</div>
