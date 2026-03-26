---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 8 клас
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

# 🖼️ Растрова графіка. Обробка растрових зображень

## 🏫 Урок *60*

---

## 🎯 Сьогодні ми дізнаємося

- 🖼️ Що таке растрова графіка та її особливості.
- 💻 Як працювати в онлайн-редакторі Photopea.
- ✂️ Як кадрувати, переміщувати та ретушувати фото.
- 🏁 Як створювати зображення з прозорим фоном (PNG).

---

## 🖼️ Растрова графіка

<div class="card important-to-remember">

**Растрове зображення** — це зображення створене з кольорових точок (пікселів).

</div>

- При збільшенні виникає ефект "пікселізації" (втрата якості).
- Для збереження зображення з прозорим фоном використовується формат **PNG**.
- Дозволяє працювати з фото та створювати фотореалістичні зображення.

---

## 💻 Онлайн-редактор Photopea

Це безкоштовний графічний редактор, який працює прямо в браузері.
🌐 **[www.photopea.com](https://www.photopea.com/)**

---

## 🛠️ Інструменти Photopea

<section class="text-medium-small">

- ![h:40px](./assets/60/move.png) **Переміщення (V):** дозволяє рухати об'єкти на полотні.
- ![h:40px](./assets/60/crop.png) **Кадрування (C):** обрізання зайвих країв зображення для покращення композиції.
- ![h:40px](./assets/60/blure.png) **Розмиття (Blur Tool):** дозволяє розмити задній план, щоб виділити головний об'єкт.
- ![h:40px](./assets/60/red-eye-removal.png) **Усунення червоних очей (Red Eye Tool):** швидко виправляє дефекти від спалаху камери.
- ![h:40px](./assets/60/patch.png) **Латка (Patch Tool):** допомагає прибрати дрібні дефекти або випадкові об'єкти на фоні.
-  ![h:40px](./assets/60/dodge.png) **Освітлювач (Dodge Tool):** обережно висвітлює потрібні ділянки (наприклад, обличчя в тіні).

</section>

---

## 📝 Довідник: Кадрування та Червоні очі

<div class="grid-container">
<div class="grid-item text-medium-small">

![h:50px](./assets/60/crop.png) **Кадрування (Crop - C)**

1. Виберіть інструмент кадрування на панелі ліворуч.
2. Потягніть за маркери на кутах рамки, щоб виділити головне, відрізавши зайве.
3. Натисніть **Enter** або галочку на верхній панелі для підтвердження.

</div>
<div class="grid-item text-medium-small">

![h:50px](./assets/60/red-eye-removal.png) **Червоні очі (Red Eye Tool)**

1. Натисніть праву кнопку миші на інструменті "Точковий пензель відновлення" (значок пластиру).
2. Виберіть **Red Eye Tool**.
3. Просто клікніть лівою кнопкою миші по червоних зіницях на фото.

</div>
</div>

---

## 📝 Довідник: Розмиття та Латка

<div class="grid-container">
<div class="grid-item text-medium-small">

![h:50px](./assets/60/blure.png) **Розмиття (Blur Tool)**

1. Знайдіть значок краплі на панелі.
2. Зверху налаштуйте: Жорсткість (Hardness) **0%**, Інтенсивність (Strength) **50-70%**.
3. Затисніть мишу та акуратно "замалюйте" фон, не торкаючись головного об'єкта.

</div>
<div class="grid-item text-medium-small">

![h:50px](./assets/60/patch.png) **Латка (Patch Tool)**

1. Знаходиться в групі інструментів "Пластиру".
2. Обведіть зайвий об'єкт на фоні (замкніть лінію виділення).
3. Наведіть курсор всередину виділеного і перетягніть на чисту сусідню ділянку фону.

</div>
</div>

---

## 📝 Довідник: Освітлювач та Прозорий фон

<div class="grid-container">
<div class="grid-item text-medium-small">

![h:50px](./assets/60/dodge.png) **Освітлювач (Dodge Tool)**

1. Знайдіть значок шпильки 📍 (в групі з "рукою").
2. Налаштування зверху: Жорсткість **0%**, Діапазон **Середні тони**, Експозиція **20%**.
3. Плавно проведіть по темних ділянках (тінях) на обличчі для їх висвітлення.

</div>
<div class="grid-item text-medium-small">

**🏁 Прозорий фон (PNG)**

1. Виділіть фон (наприклад, інструментом *Чарівна паличка - W*).
2. Натисніть клавішу **Delete** (замість фону має з'явитися шахівниця).
3. Збережіть: *Файл -> Експортувати як -> **PNG***.

</div>
</div>

---

## 💻 Практична робота

<div class="task">

**⭐️ Достатній рівень (до 6 балів)**

1. Відкрийте **[www.photopea.com](https://www.photopea.com/)** та завантажте [фото](https://drive.google.com/file/d/1Vt_jbYLnMF3g7DIx03-sj73bOXVfYdKf/view?usp=sharing)
2. Використовуйте інструмент **Кадрування (Crop)**, щоб покращити композицію (прибрати зайве з боків).
3. Збережіть результат як JPG (*Файл -> Експортувати як -> JPG*).

</div>

---

## 💻 Практична робота

<div class="task">

**⭐️⭐️ Середній рівень (до 9 балів)**

1. Виконайте завдання достатнього рівня.
2. Використовуйте інструмент **Розмиття (Blur tool)**, щоб розмити фон за основним об'єктом.
3. Також, на фото є ефект червоних очей — виправте його інструментом **Red Eye Tool**.
4. Збережіть проект (*Файл -> Зберегти як PSD*)

</div>

---

## 💻 Практична робота

<div class="task">

**⭐️⭐️⭐️ Високий рівень (до 12 балів)**

1. Виконайте завдання середнього рівня.
2. Використовуйте інструмент **Латка (Patch Tool)**, щоб прибрати дрібні дефекти на фоні.
3. Використовуйте інструмент **Освітлювач (Dodge Tool)**, щоб висвітлити обличчя.
4. Спробуйте видалити фон навколо основного об'єкта та збережіть результат у форматі **PNG** (для прозорості).

</div>
