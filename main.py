import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * np.sin(np.pi * x)

logistic_map_vec = np.vectorize(logistic_map) # Векторизируем функцию, чтобы работать с массивами
r_values = np.linspace(-2, 5, 5000) # 1000 - число точек между 2 и 4

iterations = 500 # Количество итераций для построения
last = 1000 # Сколько последних итераций отображать

x = 1e-5 * np.ones(len(r_values)) # Начальное значение 1000 иксов

fig, ax = plt.subplots(figsize=(10, 7))

for i in range(iterations): # Основной цикл для вычисления и отображения бифуркации
    x = logistic_map_vec(r_values, x)
    if i >= (iterations - last):
        ax.plot(r_values, x, ',k', alpha=.25)
        if i < last:
            ax.plot(r_values, -x, ',k', alpha=.25)

ax.set_xlim(2, 4)
ax.set_title("Бифуркационная диаграмма для логистического отображения")
ax.set_xlabel("r")
ax.set_ylabel("x")
plt.show()

#############################################################################

# Задаем несколько значений r
r_values = [2.5, 3.0, 3.5, 3.8, 4.0]
iterations = 1000
x_initial = 0.5  # Начальное значение

# Создаем фигуру с несколькими подграфиками
fig, axs = plt.subplots(len(r_values), 1, figsize=(10, 10))

for i, r in enumerate(r_values):
    x = x_initial
    x_values = []

    for j in range(iterations):
        x = logistic_map(r, x)
        x_values.append(x)

    axs[i].plot(x_values, 'k-', lw=0.5)
    axs[i].set_title(f"Временная эволюция для r = {r}")
    axs[i].set_xlabel("Итерация")
    axs[i].set_ylabel("x")

plt.tight_layout()
plt.show()