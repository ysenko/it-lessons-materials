---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: Інформатика | 7 клас
header: Урок 59
---

# **Алгоритми з вкладеними розгалуженнями**

## Урок **59**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Які блоки надає Scratch для реалізації алгоритмів з розгалуженнями
- ✏️ Як реалізувати алгоритми розгалуженнями в Scratch
- 🔧 Як реалізувати алгоритми з вкладеними розгалуженнями в Scratch

---

## Блоки Scratch для реалізації розгалужень

Для реалізацї алгоритмів з розгалуженням Scratch надає наступні блоки з розділу `Керування`

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.grid-panel {
  font-size: 14px; /* Adjust text size */
  padding: 10px;
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  margin-top: 20px;
}
</style>

<div class="grid-container">
<div class="grid-panel">

Блок `Якщо...то` дозволяє задати умову. Якщо умова виконується, то виконається код всередині блоку, якщо умова не виконується, то код всередині блоку буде пропущено.

![w:200px](./assets/59/if-block.png)

</div>
<div class="grid-panel">

Блок `Якщо...то..інакше` теж дозволяє задати умову. Якщо умова виконується, то виконається код всередині `то`, якщо умова не виконується, то виконається код всередині `інакше`.

![w:200px](./assets/59/if-else-block.png)

</div>
</div>

---

## Приклад використання блоків `Якщо`

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.grid-panel {
  font-size: 14px; /* Adjust text size */
  padding: 10px;
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  margin-top: 20px;
}
</style>

<div class="grid-container">
<div class="grid-panel">

![w:250px](./assets/59/if-example.png)

Якщо спрайт торкається межі, то він скаже "Привіт", якщо не торкається, то нічого не скаже.

</div>
<div class="grid-panel">

![w:250px](./assets/59/if-else-example.png)

Якщо спрайт торкається межі, то він скаже "Привіт", якщо не торкається, то скаже "Бувай!".

</div>
</div>

---

## ❓ Який алгоритм поданий на екрані?

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.grid-panel {
  font-size: 14px; /* Adjust text size */
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  margin-top: 20px;
}
</style>

<div class="grid-container">
<div class="grid-panel">

![h:480px](./assets/59/conditional-example-1.png)

</div>
<div class="grid-panel">

</div>
</div>

---

## 💡 Пояснення

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.grid-panel {
  font-size: 24px; /* Adjust text size */
  padding: 10px;
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  margin-top: 20px;
}
p {
  font-size: 24px;
}
</style>

Це аглгоритм, з розгалуженнями, що дозволяє спрайту "ходити" по екрану, коли натиснута відповідна стрілка на клавіатурі.

<div class="grid-container">
<div class="grid-panel">

![h:400px](./assets/59/conditional-example-1.png)

</div>
<div class="grid-panel">

![h:400px](./assets/59/conditional-example-1-scratch.png)

</div>
</div>

---

## Алгоритм з вкладеними розгалуженнями

<style>
.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: left;
}
.grid-panel {
  font-size: 24px; /* Adjust text size */
  padding: 10px;
  max-width: 100%; /* Ensures the image scales within its space */
  height: auto;
  margin-top: 20px;
}
p {
  font-size: 24px;
}
</style>

Це варіант попереднього алгоритму, що використовує вкладені блоки `Якщо...то...інакше`

<div class="grid-container">
<div class="grid-panel">

![h:350px](./assets/59/conditional-example-2.png)

</div>
<div class="grid-panel">

![h:350px](./assets/59/conditional-example-2-scratch.png)

</div>
</div>

---

## 📚 Домашнє завдання!

1. Прочитати Відкриття 42: с.218-224
2. Виконати вправу 1 на с. 222. Зняти відео роботи програми на телефон та показати в класі.
