---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: Інформатика | 7 клас
header: Урок 58
---

# **Малюємо Тризуб**

## Використовуючи Python модуль turtle

## Урок **58**

---

## Завдання

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.text {
  font-size: 14px; /* Adjust text size */
  padding: 10px;
}
.image {
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  text-align: right;
  margin-top: 50px;
}
</style>

<div class="grid-container">
  <div class="text">

1. Відкрий [turtle sandbox](https://pythonsandbox.com/turtle)
2. Використай команди модуля `turtle`, щоб намалювати Тризуб *синім кольором*.
3. Дививсь координати основних точок на та приклад тризубу праворуч.
4. Основні команди, що можуть тобі знадобитися

   | Команда            | Що робить                                  |
   |--------------------|--------------------------------------------|
   | `forward(довжина)` | Рухається вперед на вказану відстань       |
   | `back(довжина)`    | Рухається назад                            |
   | `left(кут)`        | Повертає вліво на вказаний кут (градуси)   |
   | `right(кут)`       | Повертає вправо                            |
   | `penup()`          | Піднімає "олівець", не малює               |
   | `pendown()`        | Опускає "олівець", малює знову             |
   | `goto(x, y)`       | Рухається до вказаної точки                |
   | `color("blue")`    | Задає колір лінії                          |
   | `pensize(5)`       | Встановлює товщину лінії                   |

  </div>

  <div class="imаge">

![h:540px](./assets/58/trident.png)

  </div>
</div>
