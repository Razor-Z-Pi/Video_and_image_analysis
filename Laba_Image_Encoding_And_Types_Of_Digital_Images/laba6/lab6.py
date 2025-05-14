import numpy as np
import matplotlib.pyplot as plt

# Набор данных с символами

symbols = {  
            "L": np.array([ [1, 0, 0],
                            [1, 0, 0],
                            [1, 1, 1]]),
            "T": np.array([ [1, 1, 1],
                            [0, 1, 0],
                            [0, 1, 0]]),
            "X": np.array([ [1, 0, 1],
                            [0, 1, 0],
                            [1, 0, 1]]),
}

# Функция для вычесления Хеммингового расстояния
def hamming_distance(a, b):
    return np.sum(a != b) # Считаем количество различий между массивами a and b

# Функция для распознования символа
def recognize_symbol(input_symbol):
    distances = {}
    for symbol, template in symbols.items():
        distances[symbol] = hamming_distance(input_symbol, template)

    recognize_symbol = min(distances, key=distances.get)
    return recognize_symbol

# Пример использования
input_symbol = np.array([[0, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0]])

recognized = recognize_symbol(input_symbol)
print(f"Распознанный символ: {recognized}")

# Визуализация
fix, ax = plt.subplots() # Создаем фигуру и оси для графика
ax.imshow(input_symbol, cmap = "gray", vmin = 0, vmax = 1) # Отображаем входной символ с цветовой картой
ax.set_title("Входной символ") # Заголовок для графика
plt.show()