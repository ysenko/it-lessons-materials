---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 9 клас
header: 🏫 Урок 05
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

# Фільтрування та аналіз даних засобами Таблиці Google

## 🏫 Урок **05**

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

- 🔍 Чим фільтрування відрізняється від сортування.
- ⚙️ Як створити фільтр у Таблицях Google.
- 🎛️ Як фільтрувати дані за значеннями та за умовою.
- 🔗 Як застосувати кілька умов фільтрування одночасно.

---

## 🔁 Пригадаймо попередні уроки

- Що таке гіпотеза і як її сформулювати за схемою «Я думаю, що… бо…»?
- За якими критеріями оцінюють якість відкритих даних?
- Як імпортувати xlsx-файл у Таблиці Google?
- Чим відрізняється сортування «Від А до Я» від «Від Я до А»?

---

## 🤔 Навіщо аналітику вміти фільтрувати дані?

<div class="card text-medium">

Уявіть: не 27 рядків у таблиці, а 27 000 рядків даних. І далеко не всі вони однаково важливі — частина з них лише «шум», який заважає побачити головне.

</div>

<div class="important-to-remember text-medium-small text-left">

Фільтрування дає змогу миттєво відібрати лише ті рядки, які потрібні для перевірки конкретної гіпотези, — без ручного перегляду тисяч зайвих даних.

</div>

---

## 🆚 Сортування чи фільтрування?

<div class="grid-container">
<div class="card text-left text-small">

**Сортування**

Переставляє рядки місцями за обраним стовпцем. Усі рядки залишаються на екрані — просто в іншому порядку.

</div>
<div class="card text-left text-small">

**Фільтрування**

Приховує рядки, які не відповідають умові. Порядок рядків, що залишилися, не змінюється. Дані нікуди не зникають — фільтр лише тимчасово ховає зайве.

</div>
</div>

---

## ⚙️ Як створити фільтр у Таблицях Google

<div class="card text-left text-small">

1. Виділіть таблицю з даними.
2. Оберіть `Дані → Створити фільтр`.
3. Біля кожного заголовка стовпця з'явиться значок фільтра 🔽.
4. Натисніть на значок і оберіть спосіб фільтрування.
5. Щоб зняти фільтр — `Дані → Видалити фільтр`.

</div>

---

## 🎛️ Два способи фільтрування

<div class="grid-container">
<div class="card text-left text-small">

**За значеннями**

Прапорці біля кожного унікального значення стовпця — знімаєте прапорець, і рядки з цим значенням зникають.

</div>
<div class="card text-left text-small">

**За умовою**

Умови на кшталт «Більше ніж», «Менше ніж», «Текст містить» — показуються лише рядки, що відповідають умові.

</div>
</div>

<div class="important-to-remember text-medium-small text-left">

🔗 Фільтри можна застосувати одночасно до кількох стовпців — тоді рядок залишиться видимим, лише якщо відповідає **всім** умовам одразу.

</div>

---

## ▶️ Відео: фільтри в Таблицях Google

<div class="task text-medium-small">

[Переглянути відео-інструкцію: використання фільтрів у Таблицях Google](https://www.youtube.com/watch?v=PszzC5UihlI)

</div>

---

## 📊 Набір даних: штрафи Укртрансбезпеки

<div class="grid-container">
<div class="card text-left text-small">

**Видавець:** Держслужба України з безпеки на транспорті (Укртрансбезпека)

**Джерело:** [набір даних на data.gov.ua](https://data.gov.ua/dataset/dfab13fa-8911-4098-ac1e-85f210ab9b24/resource/03e97f15-b365-4f8c-9bff-57a6dc1e2070)

</div>
<div class="card text-left text-small">

Аркуш «January-March 2026» — суми штрафів по областях за I квартал 2026 року. Той самий файл, що й на уроці 04.

</div>
</div>

---

## 🖱️ Завдання. Перевірте гіпотези фільтруванням

<div class="grid-container">
<div class="card text-left text-small">

**Гіпотеза 1**
Західні області (Львівська, Івано-Франківська, Тернопільська) сплатили менше мільйона гривень штрафів з пасажирського транспорту.
Фільтр за значеннями (області) + умова «Менше ніж» `1000000` на `finesPassengerTransport`.

</div>
<div class="card text-left text-small">

**Гіпотеза 2**
Київська область сплатила більше 10 мільйонів гривень штрафів з пасажирського транспорту.
Фільтр за значеннями (Київська обл.) + умова «Більше ніж» `10000000` на `finesPassengerTransport`.

</div>
<div class="card text-left text-small">

**Гіпотеза 3**
В Україні немає області, де одночасно сплатили 5+ млн грн штрафів і за пасажирський, і за вантажний транспорт.
Умова «Більше або дорівнює» `5000000` одночасно на `finesTruckTransport` і `finesPassengerTransport`.

</div>
</div>

<div class="important-to-remember text-medium-small text-left">

⏱️ Час на практичну роботу — 18 хв. Після кожної перевірки записуйте у зошит, чи підтвердилася гіпотеза.

</div>

---

## 👀 Пауза для очей

<div class="card text-medium">

Відведіть погляд від екрана. Подивіться на найдальший предмет у кабінеті, потім — на найближчий. Повторіть кілька разів.

</div>

---

## ✅ Перевіряємо результати

<div class="grid-container">
<div class="card text-left text-small">

**Гіпотеза 1** — не підтвердилася повністю: Івано-Франківська (432 480 грн) та Тернопільська (694 960 грн) — менше мільйона, а Львівська — ні (1 471 520 грн).

</div>
<div class="card text-left text-small">

**Гіпотеза 2** — не підтвердилася: у Київської області та м. Києва — лише 4 929 490 грн.

</div>
<div class="card text-left text-small">

**Гіпотеза 3** — не підтвердилася: Одеська область має і вантажний (7 102 260 грн), і пасажирський (5 083 510 грн) показники ≥ 5 млн одночасно.

</div>
</div>

---

## 🗣️ Рефлексія

- Чим фільтрування відрізняється від сортування?
- Що відбувається з рядками, які не відповідають умові фільтра — вони видаляються чи лише приховуються?
- Коли на практиці варто скористатися фільтром, а коли — сортуванням?

---

## 🏠 Домашнє завдання

<div class="task text-medium-small">

1. Опрацювати текст підручника, с. 21-23 (Проєкт 2, Етап 3).
2. Переглянути відео-інструкцію «Використання фільтрів у Таблицях Google» та цю презентацію.

</div>
