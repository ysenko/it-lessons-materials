---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 06
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

# Поштові служби інтернету. Обліковий запис онлайн-сервісу та його налаштування

## 🏫 Урок **06**

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

- 🌐 Що таке поштовий сервер електронної пошти
- ✉️ Із яких частин складається електронна адреса
- 🔑 Що таке обліковий запис (акаунт) і логін
- 🔐 Які вимоги до надійного пароля
- ✍️ Зареєструємо власну поштову скриньку та налаштуємо обліковий запис

---

## 📬 Поштовий сервер

<div class="card text-medium">

**Поштовий сервер** — комп'ютер і програмне забезпечення, за допомогою якого підтримується робота електронної пошти.

</div>

📌 Наприклад: `gmail.com`, `mail.ukr.net`, `proton.me`

Лист надсилається на поштовий сервер, що забезпечує його доставку за адресою, і приймається на тому сервері, де адресат/адресатка має обліковий запис.

---

## ✉️ Адреса електронної пошти

**Приклад:** `s.petrenko@proton.me`

<div class="grid-container">
<div class="card text-medium">

👤 `s.petrenko`
Логін — ім'я поштової скриньки користувача

</div>
<div class="card text-medium">

🌐 `proton.me`
Ім'я поштового сервера, на якому розміщена скринька

</div>
</div>

📧 Символ `@` (читається «ет» або «собака») розділяє логін і сервер

---

## ✅ Правила для логіна

<div class="text-medium-small">

- 🔒 Логін має бути **унікальним** у межах обраного сервера
- 🚫 Не можна використовувати пропуски, символи кирилиці
- ➖ Можна відокремити прізвище від імені символом `_` або `.`
- 💡 Обирайте логін, який важко сплутати з чужим (ініціали + прізвище)

</div>
<div class="task text-small">

**Вправа.** Обговоріть у парі, що з переліченого може бути адресою електронної пошти:

<div class="grid-container" style="grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 8px;">

<div class="card" style="padding: 8px; margin: 0;">

1. `olena2020@ gmail.com`

</div>

<div class="card" style="padding: 8px; margin: 0;">

2. `олена2020@ gmail.com`

</div>

<div class="card" style="padding: 8px; margin: 0;">

3. `olena2020@Д.ua`

</div>

<div class="card" style="padding: 8px; margin: 0;">

4. `olena2020@ukr.net`

</div>

<div class="card" style="padding: 8px; margin: 0;">

5. `olena:/&@ gmail.com`

</div>

<div class="card" style="padding: 8px; margin: 0;">

6. `OlEnA2020@ukr.net`

</div>

<div class="card" style="padding: 8px; margin: 0;">

7. `olena 2020@mail.ukr.net`

</div>

</div>

</div>

---

## 🔑 Обліковий запис (акаунт)

<div class="card text-medium important-to-remember">

**Обліковий запис (акаунт)** — сукупність логіна й пароля, за якими сервер розпізнає користувача під час звернення до своїх ресурсів.

</div>

- 🗝️ Логін + пароль = обліковий запис
- 🖊️ Заповнюється один раз під час реєстрації
- ⭐ Обов'язкові поля анкети зазвичай позначені зірочкою

---

## 🔐 Як обрати надійний пароль

<div class="important-to-remember text-medium-small text-left">

- 📏 Не менше 10–14 символів
- 🔤 Великі й малі літери, цифри, спеціальні символи
- 🚫 Без імен, дат народження, простих слів («123456», «password», «qwerty»)
- 🔁 Не використовувати один пароль для кількох сервісів
- 🔒 Символи пароля на екрані заховані (замінені зірочками або кружечками)

</div>

---

## 🔐 Вправа: обери надійний і зручний пароль

<div class="task text-medium-small">

На поштовому сервері діють правила: не менше 8 символів, обов'язково великі й малі літери, цифри та спецзнаки. Оберіть паролі, що відповідають правилам і будуть надійними та зручними для введення:

1. `17071967`
2. `Data17071967$`
3. `Antkiv17071967`
4. `1767Fynrsd!`
5. `lfgrfygjdfhf1!`

</div>

💬 Обговорення: чому решта варіантів не підходять?

---

## ⚖️ Переваги та недоліки електронної пошти

<div class="grid-container">
<div class="card text-medium-small">

**➕ Переваги**
- Висока швидкість доставки (секунди)
- Невисока вартість послуг
- Обмін повідомленнями у зручний час

</div>
<div class="card text-medium-small">

**➖ Недоліки**
- Не можна надіслати оригінал документа з підписом і печаткою
- Лист може перехопити стороння особа
- Ризик отримати шкідливу програму разом з листом

</div>
</div>

---

## 💻 Практична робота

<div class="task text-medium-small">

1. 🌐 Перейти на [https://account.proton.me/mail](https://account.proton.me/mail)
2. 🆕 Обрати безкоштовний план, вигадати унікальний логін і перевірити його доступність
3. 🔐 Створити надійний пароль за правилами з інструктажу
4. ✅ Пройти перевірку — CAPTCHA або код на резервну електронну адресу (**номер телефону вводити не потрібно**)
5. 📥 Увійти до своєї поштової скриньки
6. 💾 Зберегти логін і пароль у менеджері паролів або записати в надійному місці
7. 📝 Додати адресу своєї скриньки до [спільного списку класу](https://forms.gle/St5e61HwCCpa7W4VA)

</div>

---

## 🤔 Обговорення

- 🔓 Чому небезпечно використовувати один і той самий пароль для кількох сервісів?
- 🧐 Чому логін варто обирати обдумано?
- 📬 Яку адресу ви собі створили і чому обрали саме такий логін?

---

## 📌 Висновки

- 📬 Поштовий сервер підтримує роботу електронної пошти
- ✉️ Адреса складається з логіна, символу `@` та імені сервера
- 🔑 Обліковий запис — це логін і пароль разом
- 🔒 Надійний пароль — основа безпеки поштової скриньки
- 🚨 Будьте уважні: не вводьте зайві особисті дані під час реєстрації

---

## 🏠 Домашнє завдання

1. 📖 Опрацювати матеріал підручника, с. 30–33
2. 🔑 Запам'ятати логін і пароль від власної поштової скриньки — знадобляться на наступному уроці
3. ⭐ *(Додатково)*: дізнатися в дорослих, якою поштовою скринькою користуються вони і чому саме нею
