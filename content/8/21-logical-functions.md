---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
header: 🏫 Урок 21
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

# Опрацювання табличних даних з використанням логічних функцій

## 🏫 Урок **21**

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

- 🔁 Пригадаємо вбудовані функції та підсумуємо проєкт «Благодійний ярмарок».
- ℹ️ Що таке логічний вираз і яких значень він набуває.
- 🔀 Як функція `IF` обирає результат залежно від умови.
- 🔗 Як описати складену умову функціями `AND`, `OR`, `NOT`.
- ⌨️ Як застосовувати логічні функції в Google Таблицях.

---

## 🔁 Пригадуємо функції

<div class="grid-container text-small">
<div class="task">

### 🧩 Розминка
Яку функцію — `SUM`, `MAX`, `MIN` чи `AVERAGE` — потрібно використати для кожного обчислення?

🔗 <a href="https://learningapps.org/view2093638" target="_blank" rel="noopener noreferrer">Відкрити вправу</a>

</div>
<div class="card">

### 🛍️ Проєкт «Благодійний ярмарок»: типові помилки
- Діапазон у `RANK` без `$` → місця неправильні.
  ✅ `=RANK(D2; $D$2:$D$9; 0)`
- `D10` без `$` у частці виручки → хибні числа або `#DIV/0!`.
  ✅ `=ROUND(D2/$D$10*100; 1)`
- Числа введено вручну замість функції ❌

</div>
</div>

---

## ℹ️ Логічний вираз

<div class="card text-medium-small">

**Логічний вираз** містить знак порівняння `=` `<>` `>` `<` `>=` `<=` і набуває одного з двох значень: **TRUE** (істина) або **FALSE** (хибність).

</div>

<div class="text-small">

| Логічний вираз | Коли він набуває значення TRUE |
|---|---|
| `A1>1` | число в `A1` більше за 1 |
| `B13="Петрик"` | у клітинці `B13` записано текст «Петрик» |
| `B3-C3>=12` | різниця значень `B3` і `C3` більша або дорівнює 12 |
| `F2*A4=SUM(B2:B13)` | добуток `F2` і `A4` дорівнює сумі діапазону `B2:B13` |

</div>

---

## 🔀 Функція IF — розгалуження в таблиці

<div class="card text-medium-small">

`IF(логічний_вираз; значення_якщо_істина; значення_якщо_хибність)`

</div>

<div class="grid-container text-small">
<div>

- Вираз **істинний** → у клітинці друге значення ✅
- Вираз **хибний** → у клітинці третє значення ❌
- Значення — число, **текст у лапках**, вираз або інша функція.
- `""` — порожня клітинка.

</div>
<div>

| Формула | Значення | Результат |
|---|---|---|
| `=IF(B2>C2; "Перевищення бюджету"; "OK")` | `B2`=450, `C2`=500 | OK |
| `=IF(A1>A2; 100; 0)` | `A1`=20, `A2`=15 | 100 |
| `=IF(A1>=0; A1; -A1)` | `A1`=−7 | 7 |

</div>
</div>

---

## 🤔 Перевір себе

<div class="card text-medium-small">

У клітинці `B2` — число **20**, у клітинці `C2` — число **10**. Що відобразиться в клітинці `D2`?

1. `=IF(B2<0; -B2; B2)`
2. `=IF(B2>C2; "більше"; "")`
3. `=IF(C2>0; B2+C2; B2-C2)`

</div>

---

## 🔗 Складені умови: AND, OR, NOT

<div class="grid-container text-small">
<div class="card">

### `AND(умова1; умова2; …)`
**TRUE**, якщо виконуються **всі** умови.
Чи двоцифрове число в `A1`?
`=AND(A1>9; A1<100)`

</div>
<div class="card">

### `OR(умова1; умова2; …)`
**TRUE**, якщо виконується **хоча б одна** умова.
`=OR(A1<0; B1<0)`

</div>
<div class="card">

### `NOT(умова)`
**TRUE**, якщо умова **не** виконується.
`=NOT(A1=0)`

</div>
</div>

<div class="important-to-remember text-small">

🪆 **Вкладені IF** — для вибору з трьох і більше варіантів (рівняння ax = b, a — в `A4`, b — в `B4`):
`=IF(AND(A4=0; B4=0); "Безліч розв'язків"; IF(AND(A4=0; B4<>0); "Жодного розв'язку"; B4/A4))`

</div>

---

<section class="task">

## 🧩 Завдання 1: Логічні функції

<div class="grid-container">
<div class="text-left text-medium-small">

У клітинці `A1` — число **100**, у клітинці `B1` — число **10**. Оберіть правильну відповідь на кожне запитання вправи.

🔗 <a href="https://learningapps.org/display?v=pyuko1uxa26" target="_blank" rel="noopener noreferrer">Відкрити вправу</a>

</div>
<div class="image-center">

![w:260px](./assets/21/qrcode.png)

</div>
</div>

</section>

---

<section class="task">

## ⌨️ Завдання 2: Логічні функції в Google Таблицях

<div class="text-small">

🔗 <a href="https://docs.google.com/spreadsheets/d/1qhTrqkVm2bq1HiJ5BgdiKQOE4DH5ek9EpR5FE6ikptY/copy" target="_blank" rel="noopener noreferrer">Відкрити таблицю</a> → **Створити копію** → перейменуйте на `Урок21_Прізвище`. Заповнюйте **жовті** клітинки формулами.

### 🟢 Середній
1. У `C2` за допомогою функції `IF` визнач колір маркування парти: зріст **понад 160 см** — «Синє», інакше — «Зелене». Скопіюй формулу автозаповненням до `C9`.

### 🟡 Достатній
2. У `E2` за допомогою функцій `IF` і `AND` виведи «Так», якщо зріст **не менше 155 см і** оцінка з фізкультури **не нижче 9**, інакше — «Ні». Скопіюй до `E9`.
3. У `E10` обчисли, скільки учнів потрапили до збірної.

</div>

</section>

---

<section class="task">

## ⌨️ Завдання 2 (продовження)

<div class="text-small">

### 🔴 Високий
4. У `F2` за допомогою функцій `IF` і `OR` виведи «Так», якщо зріст **менше 150 см або** оцінка з фізкультури **нижче 9**; інакше клітинка має залишитися **порожньою**. Скопіюй до `F9`.
5. У `F10` обчисли, скільки учнів потребують додаткового тренування.

</div>

<div class="important-to-remember text-small">

⚠️ Текст у формулі пишемо в лапках: `"Так"`. Формула з `;` видає помилку? *Файл* → *Налаштування* → *Мовний стандарт* → **Україна**.

</div>

</section>

---

## 🏠 Домашнє завдання

<div class="text-medium-small">

1. 📖 Опрацювати конспект уроку.
2. 📚 Опрацювати матеріали підручника **с. 82–86**.
3. 🔺 Завдання 11 (с. 86): у Google Таблицях створити таблицю, у якій після введення довжин сторін трикутника автоматично визначається, чи є він **рівнобедреним** (хоча б дві сторони рівні) — функції `IF` і `OR`.

</div>
