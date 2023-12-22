import cv2
import mediapipe as mp
import numpy as np
import math

# Проверка, показываем ли мы жест "Кольцо" первым и вторым пальцем
def jest(results):
    ax1 = results.multi_hand_landmarks[0].landmark[4].x
    ay1 = results.multi_hand_landmarks[0].landmark[4].y
    ax2 = results.multi_hand_landmarks[0].landmark[20].x
    ay2 = results.multi_hand_landmarks[0].landmark[20].y
    if math.hypot(ax1 - ax2, ay1 - ay2) < 0.05:
        return True

# Проверка выпрямлен ли второй палец
def finger_2(results):
    ax = results.multi_hand_landmarks[0].landmark[5].x
    ay = results.multi_hand_landmarks[0].landmark[5].y
    axx = results.multi_hand_landmarks[0].landmark[6].x
    ayy = results.multi_hand_landmarks[0].landmark[6].y
    axxx = results.multi_hand_landmarks[0].landmark[7].x
    ayyy = results.multi_hand_landmarks[0].landmark[7].y
    axxxx = results.multi_hand_landmarks[0].landmark[8].x
    ayyyy = results.multi_hand_landmarks[0].landmark[8].y
    x = results.multi_hand_landmarks[0].landmark[0].x
    y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(ax - x, ay - y) < math.hypot(axx - x, ayy - y) < math.hypot(axxx - x,
                                                                                        ayyy - y) < math.hypot(
        axxxx - x, ayyyy - y):
        return True
    return False

# Проверка выпрямлен ли третий палец
def finger_3(results):
    ax = results.multi_hand_landmarks[0].landmark[9].x
    ay = results.multi_hand_landmarks[0].landmark[9].y
    axx = results.multi_hand_landmarks[0].landmark[10].x
    ayy = results.multi_hand_landmarks[0].landmark[10].y
    axxx = results.multi_hand_landmarks[0].landmark[11].x
    ayyy = results.multi_hand_landmarks[0].landmark[11].y
    axxxx = results.multi_hand_landmarks[0].landmark[12].x
    ayyyy = results.multi_hand_landmarks[0].landmark[12].y
    x = results.multi_hand_landmarks[0].landmark[0].x
    y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(ax - x, ay - y) < math.hypot(axx - x, ayy - y) < math.hypot(axxx - x,
                                                                              ayyy - y) < math.hypot(
        axxxx - x, ayyyy - y):
        return True
    return False

# Проверка выпрямлен ли четвертый палец
def finger_4(results):
    ax = results.multi_hand_landmarks[0].landmark[13].x
    ay = results.multi_hand_landmarks[0].landmark[13].y
    axx = results.multi_hand_landmarks[0].landmark[14].x
    ayy = results.multi_hand_landmarks[0].landmark[14].y
    axxx = results.multi_hand_landmarks[0].landmark[15].x
    ayyy = results.multi_hand_landmarks[0].landmark[15].y
    axxxx = results.multi_hand_landmarks[0].landmark[16].x
    ayyyy = results.multi_hand_landmarks[0].landmark[16].y
    x = results.multi_hand_landmarks[0].landmark[0].x
    y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(ax - x, ay - y) < math.hypot(axx - x, ayy - y) < math.hypot(axxx - x,
                                                                              ayyy - y) < math.hypot(
        axxxx - x, ayyyy - y):
        return True
    return False

# Проверка выпрямлен ли пятый палец
def finger_5(results):
    ax = results.multi_hand_landmarks[0].landmark[17].x
    ay = results.multi_hand_landmarks[0].landmark[17].y
    axx = results.multi_hand_landmarks[0].landmark[18].x
    ayy = results.multi_hand_landmarks[0].landmark[18].y
    axxx = results.multi_hand_landmarks[0].landmark[19].x
    ayyy = results.multi_hand_landmarks[0].landmark[19].y
    axxxx = results.multi_hand_landmarks[0].landmark[20].x
    ayyyy = results.multi_hand_landmarks[0].landmark[20].y
    x = results.multi_hand_landmarks[0].landmark[0].x
    y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(ax - x, ay - y) < math.hypot(axx - x, ayy - y) < math.hypot(axxx - x,
                                                                              ayyy - y) < math.hypot(
        axxxx - x, ayyyy - y):
        return True
    return False


# Принимание на вход изображение, с которым будем работать
img = cv2.imread('input.jpg')

#создаем детектор
handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    # переводим его в формат RGB для распознавания
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    # Распознаем
    results = handsDetector.process(flippedRGB)
    # Рисуем распознанное, если распозналось
    if results.multi_hand_landmarks is not None:
        # Проверяем, что показали кольцо первым и пятым пальцем
        if jest(results):
            # Если да, то записываем в img синие изображение
            img[:, :, 1:] = 0
            break
        # Проверяем, что показываем второй и третий палец
        elif finger_2(results) and finger_3(results) and finger_5(results)!=True and finger_4(results)!=True:
            # Если да, то записываем в img красное изображение
            img[:, :, :2] = 0
            break
        # Проверяем, что показываем первый палец:
        elif finger_2(results) and finger_5(results)!=True and finger_4(results)!=True and finger_3(results)!=True:
            # Если да, то записываем в img зеленое изображение
            img[:, :, 2:] = 0
            img[:, :, :1] = 0
            break
        # Функция вывода точек на руке и их соединение
        mp.solutions.drawing_utils.draw_landmarks(flippedRGB,
                                                      results.multi_hand_landmarks[0],
                                                      mp.solutions.hands.HAND_CONNECTIONS)
    # переводим в BGR и показываем результат
    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hands", res_image)
# освобождаем ресурсы
handsDetector.close()
# Выводи наше изображение одного цвета
cv2.imshow('output.jpg', img)
cv2.waitKey()