import matplotlib.pyplot as plt
import os

# Створюємо папку, якщо її немає
os.makedirs('content/6/assets/51', exist_ok=True)

plt.figure(figsize=(10, 8))

# Малюємо осі
plt.axhline(0, color='blue', linewidth=3)
plt.axvline(0, color='green', linewidth=3)

# Координати сцени Scratch
plt.xlim(-240, 240)
plt.ylim(-180, 180)

# Додаємо сітку
plt.grid(True, linestyle='--', alpha=0.5)

# Підписи точок (Центр та краї)
plt.text(0, 5, '(0, 0)\nЦентр', fontsize=14, ha='center', va='bottom', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
plt.text(180, 10, 'X: 240\nВправо', fontsize=12, color='blue', fontweight='bold')
plt.text(-220, 10, 'X: -240\nВліво', fontsize=12, color='blue', fontweight='bold')
plt.text(10, 150, 'Y: 180\nВгору', fontsize=12, color='green', fontweight='bold')
plt.text(10, -170, 'Y: -180\nВниз', fontsize=12, color='green', fontweight='bold')

# Назва та підписи
plt.title('Де знаходиться наш Спрайт? (Координати)', fontsize=20, pad=30)
plt.xlabel('Вісь X (Вправо-Вліво)', fontsize=14, color='blue')
plt.ylabel('Вісь Y (Вгору-Вниз)', fontsize=14, color='green')

# Стрілки
plt.annotate('', xy=(240, 0), xytext=(220, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
plt.annotate('', xy=(-240, 0), xytext=(-220, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
plt.annotate('', xy=(0, 180), xytext=(0, 160), arrowprops=dict(arrowstyle='->', color='green', lw=2))
plt.annotate('', xy=(0, -180), xytext=(0, -160), arrowprops=dict(arrowstyle='->', color='green', lw=2))

plt.tight_layout()
plt.savefig('content/6/assets/51/scratch-coordinates.png', dpi=150)
