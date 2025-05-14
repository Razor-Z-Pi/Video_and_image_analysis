import numpy as np
import matplotlib.pyplot as plt

# Набор данных с символами
symbols = {
    "L": np.array([[1, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1]]),
    "T": np.array([[1, 1, 1],
                   [0, 1, 0],
                   [0, 1, 0]]),
    "X": np.array([[1, 0, 1],
                   [0, 1, 0],
                   [1, 0, 1]]),
    "N": np.array([[1, 0, 1],
                   [1, 1, 1],
                   [1, 0, 1]]),
    "K": np.array([[1, 0, 1],
                   [1, 1, 0],
                   [1, 0, 1]]),
    "O": np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]),
    "H": np.array([[1, 0, 1],
                   [1, 1, 1],
                   [1, 0, 1]]),
    "Y": np.array([[1, 0, 1],
                   [0, 1, 0],
                   [0, 1, 0]]),
}

# Параметры сети
eps = 0.1  # Коэффициент торможения
threshold = 4.5  # Порог активации (примерно половина размера вектора)

# Преобразуем символы в векторы для сети Хэмминга
def flatten_symbol(symbol):
    return symbol.flatten()

# Создаем весовую матрицу (нижний слой)
def create_weights(symbols_dict):
    patterns = [flatten_symbol(s) for s in symbols_dict.values()]
    weights = np.array(patterns) / 2
    return weights

weights = create_weights(symbols)
symbol_names = list(symbols.keys())

# Первый слой сети Хэмминга
def first_layer(input_vector, weights):
    return np.dot(weights, input_vector) + threshold

# Второй (рекуррентный) слой сети Хэмминга, для конкуренции 
def second_layer(initial_output, max_iter=20):
    output = initial_output.copy()
    for _ in range(max_iter):
        new_output = output.copy()
        for i in range(len(output)):
            sum_others = np.sum(output) - output[i]
            new_output[i] = max(0, output[i] - eps * sum_others)
        
        # Проверка на сходимость
        if np.allclose(new_output, output, atol=1e-4):
            break
        output = new_output
    return output

# Полный процесс распознавания
def recognize_symbol(input_symbol):
    # Преобразуем вход в бинарный вектор
    input_vector = flatten_symbol(input_symbol)
    input_vector = np.where(input_vector > 0, 1, 0)
    
    # Первый слой
    first_out = first_layer(input_vector, weights)
    
    # Второй слой
    second_out = second_layer(first_out)
    
    # Находим самого победителя
    winner_idx = np.argmax(second_out)
    confidence = second_out[winner_idx] / np.sum(second_out)
    
    return symbol_names[winner_idx], confidence

# Функция для добавления шума к символу
def add_area(symbol, noise_level=0.2):
    noisy = symbol.copy()
    mask = np.random.random(noisy.shape) < noise_level
    noisy[mask] = 1 - noisy[mask]  # Инвертируем выбранные пиксели
    return noisy

# Тестирование на оригинальных символах
print("Тестирование на оригинальных символах:")
for name, symbol in symbols.items():
    recognized, confidence = recognize_symbol(symbol)
    print(f"Символ {name} распознан как {recognized} (уверенность: {confidence:.2f})")
    
# Тестирование на зашумленных символах
print("\nТестирование на зашумленных символах:")
test_symbol = symbols["L"]
noisy_L = add_area(test_symbol, 0.3)
recognized, confidence = recognize_symbol(noisy_L)
print(f"Зашумленный L распознан как {recognized} (уверенность: {confidence:.2f})")
    
test_symbol = symbols["X"]
noisy_X = add_area(test_symbol, 0.3)
recognized, confidence = recognize_symbol(noisy_X)
print(f"Зашумленный X распознан как {recognized} (уверенность: {confidence:.2f})")

test_symbol = symbols["Y"]
noisy_Y = add_area(test_symbol, 0.3)
recognized, confidence = recognize_symbol(noisy_Y)
print(f"Зашумленный Y распознан как {recognized} (уверенность: {confidence:.2f})")

test_symbol = symbols["K"]
noisy_K = add_area(test_symbol, 0.3)
recognized, confidence = recognize_symbol(noisy_K)
print(f"Зашумленный Z распознан как {recognized} (уверенность: {confidence:.2f})")

test_symbol = symbols["H"]
noisy_H = add_area(test_symbol, 0.3)
recognized, confidence = recognize_symbol(noisy_H)
print(f"Зашумленный M распознан как {recognized} (уверенность: {confidence:.2f})")
    
# Визуализация
def plot_symbol(symbol, title):
    fix, ax = plt.subplots() # Создаем фигуру и оси для графика
    ax.imshow(symbol, cmap="binary", vmin=0, vmax=1)
    ax.set_title(title)
    ax.axis('off')
    plt.show()
    
plot_symbol(symbols["L"], "Эталонный символ L")
plot_symbol(noisy_L, "Зашумленный символ L")
plot_symbol(symbols["X"], "Эталонный символ X")
plot_symbol(noisy_X, "Зашумленный символ X")
plot_symbol(symbols["Y"], "Эталонный символ Y")
plot_symbol(noisy_Y, "Зашумленный символ Y")
plot_symbol(symbols["K"], "Эталонный символ K")
plot_symbol(noisy_K, "Зашумленный символ K")
plot_symbol(symbols["H"], "Эталонный символ H")
plot_symbol(noisy_H, "Зашумленный символ H")