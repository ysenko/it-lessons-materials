---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 9 клас
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

# Порівняння ШІ-асистентів

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

## 🎯 Сьогодні ми

- 🤖 Порівняємо популярні **ШІ-асистенти**.
- 🎮 З'ясуємо, чи може ШІ створити **AAA-гру на 100 годин**.
- 🕵️ Дізнаємося, що **приховує** від нас ШІ.
- 🧐 Розберемося, як ШІ відрізняє **правду від вигадки**.
- ⚔️ Влаштуємо **ШІ-арену**: хто з асистентів потрапить у пастку?

---

## 🤖 Популярні ШІ-асистенти

<div class="text-small">

| Асистент | Розробник | 💪 Чим сильний | ⚠️ Що врахувати |
|---|---|---|---|
| <a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">**ChatGPT**</a> | OpenAI 🇺🇸 | Універсальний: пояснення, тексти, код | Без входу — гостьовий режим з обмеженнями |
| <a href="https://gemini.google.com" target="_blank" rel="noopener noreferrer">**Gemini**</a> | Google 🇺🇸 | Пошук Google, YouTube, Документи | Повний доступ — з Google-акаунтом |
| <a href="https://copilot.microsoft.com" target="_blank" rel="noopener noreferrer">**Copilot**</a> | Microsoft 🇺🇸 | Windows, Edge, Word; посилання на джерела | Може вимагати вхід |
| <a href="https://www.perplexity.ai" target="_blank" rel="noopener noreferrer">**Perplexity**</a> | Perplexity AI 🇺🇸 | «ШІ-пошуковик»: відповідь + джерела | Краще для фактів, ніж для творчості |
| <a href="https://claude.ai" target="_blank" rel="noopener noreferrer">**Claude**</a> | Anthropic 🇺🇸 | Довгі тексти, акуратні пояснення, код | Потрібен акаунт |
| <a href="https://chat.deepseek.com" target="_blank" rel="noopener noreferrer">**DeepSeek**</a> | DeepSeek 🇨🇳 | Безкоштовний, математика й код | Цензура; дані на серверах у Китаї |

</div>

<div class="important-to-remember text-small text-left">

🦆 <a href="https://duck.ai" target="_blank" rel="noopener noreferrer">**Duck.ai**</a> — кілька моделей (GPT, Claude, Llama, Mistral) в одному вікні, **без реєстрації**. 💡 Немає найкращого ШІ — є **кращий для конкретного завдання**.
</div>

---

## 🎮 Чи може ШІ створити AAA-гру на 100 годин?

<div class="text-small">

🏗️ **AAA-гра** — це сотні розробників, 3–5+ років роботи і бюджет у **сотні мільйонів** доларів.

</div>

<div class="grid-container">
<div class="card text-small text-left">

✅ **Що ШІ вже вміє:**
- 🎨 концепт-арти, текстури, звуки;
- 💬 діалоги персонажів, шматки коду;
- 🌍 **Genie 3** (Google DeepMind) створює 3D-світ за описом — лише **на кілька хвилин**.

</div>
<div class="card text-small text-left">

❌ **Чого ШІ поки не вміє:**
- 📖 тримати цілісний сюжет **100 годин**;
- ⚖️ збалансувати тисячі механік;
- 🧪 відчути, чи гра **цікава**.

</div>
</div>

<div class="important-to-remember text-small text-left">

🎯 **Висновок:** зараз — **ні**. ШІ — потужний інструмент команди, який пришвидшує роботу, але не замінює її.

</div>

---

## 🕵️ Що приховує від нас ШІ?

<div class="grid-container">
<div class="card text-small text-left">

📜 **Приховані інструкції** — розробник дає ШІ правила (системний промпт), яких ви не бачите.

📅 **Межі знань** — ШІ навчений на даних до певної дати й не завжди каже, що інформація застаріла.

😎 **Невпевненість** — правду і вигадку ШІ говорить **однаково впевнено**.

</div>
<div class="card text-small text-left">

🚧 **Фільтри та цензура** — відмова від небезпечних тем захищає нас; але деякі моделі мовчать і з **політичних причин** (DeepSeek уникає подій 1989 р. на площі Тяньаньмень).

💾 **Ваші дані** — розмови можуть зберігатися й використовуватися для навчання моделі.

⬛ **«Чорна скринька»** — навіть розробники не до кінця розуміють, як модель дійшла до відповіді.

</div>
</div>

---

## 🧐 Як ШІ відрізняє правду від вигадки?

<div class="card text-small text-left">

🎲 Мовна модель **не знає**, що правда, — вона передбачає **найімовірніше наступне слово** на основі мільярдів прочитаних текстів.

</div>

<div class="grid-container">
<div class="card text-small text-left">

✅ **Часто трапляється в даних** — ШІ відповідає правильно.
*Столиця України — Київ.*

</div>
<div class="card text-small text-left">

🌀 **Рідкісне, нове, локальне** (ваша школа, місто) — ризик **галюцинації**: вигадки, що виглядає правдоподібно.

</div>
</div>

<div class="card text-small text-left">

🔗 **Що допомагає:** пошук в інтернеті з джерелами (Perplexity, Copilot, режим пошуку ChatGPT). Але посилання треба **відкривати** — ШІ може неправильно переказати джерело.

</div>

<div class="important-to-remember text-small text-left">

🛡️ Відрізняти правду від вигадки — **наша робота**. Пригадуємо **SIFT**: зупинись → досліди джерело → знайди краще висвітлення → простеж до оригіналу.

</div>

---

<section class="task">

## 🎲 Завдання 1: ШІ — правда чи міф?

<div class="text-medium text-left">

1. 🌐 Відкрийте <a href="https://kahoot.it/" target="_blank" rel="noopener noreferrer">kahoot.it</a>.
2. 🔢 Введіть **PIN гри**, який назве вчитель.
3. 🙋 Нікнейм — **ім'я та перша літера прізвища**.
4. ✅❌ Для кожного твердження оберіть: **Правда** чи **Міф**.

</div>

<div class="card text-medium-small text-left">

⚡ Що швидше й точніше відповідаєте — то більше балів!

</div>

</section>

---

<section class="task">

## ⚔️ Завдання 2: ШІ-арена (у групах)

<div class="text-small text-left">

📌 <a href="https://padlet.com/yurasenko/21-s0259rvj9y91wsm41dns" target="_blank" rel="noopener noreferrer">Дошка «Урок 21. ШІ-арена»</a> · 🤖 <a href="https://chatgpt.com" target="_blank" rel="noopener noreferrer">ChatGPT</a> · <a href="https://gemini.google.com" target="_blank" rel="noopener noreferrer">Gemini</a> · <a href="https://claude.ai" target="_blank" rel="noopener noreferrer">Claude</a> · <a href="https://www.perplexity.ai" target="_blank" rel="noopener noreferrer">Perplexity</a>

</div>

<div class="card text-small text-left">

1. 👥 Ваша група отримує **одне запитання** з дошки (стовпець **📋 Запитання**).
2. 🔁 Поставте **те саме запитання** кожному з **4 ШІ-асистентів** (кожен — у своїй вкладці).
3. ⚖️ Порівняйте відповіді з підказкою на картці: хто **правильний**, **чесний**, **зрозумілий**?
4. 🖱️ **Перетягніть** картку із запитанням у стовпець асистента, який відповів **найкраще**.
5. 💬 Додайте **коментар** до картки: *«Група N: переміг …, бо …»* (1–2 речення).

</div>

<div class="important-to-remember text-small text-left">

🔐 Не входьте в акаунти. Якщо асистент вимагає вхід — пропустіть його й напишіть про це в коментарі.

</div>

</section>

---

## 🏠 Домашнє завдання

<div class="card text-medium-small text-left">

1. 📝 Опрацювати конспект уроку.
2. 📖 Опрацювати матеріали підручника **с. 66–72**.
3. 🏫 Поставте улюбленому ШІ-асистенту запитання про **рідкісний факт**, який ви точно знаєте (історія вашої школи, вулиці, села чи міста). Перевірте, чи не вигадав ШІ відповідь, і запишіть у зошит: **запитання**, **що відповів ШІ**, **що правильно**, а **що — вигадка**.

</div>
