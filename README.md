# Project_Mediapipe
Распознавание изображения и вывод картинки в различных цветах
В моем проекте используются три жеста, который предсталвены ниже:


1 - ый жест:


![Alt-текст](https://w7.pngwing.com/pngs/468/569/png-transparent-v-sign-peace-symbols-drawing-points-of-interest-miscellaneous-white-text.png)

2- ой жест:


![Alt-текст](https://cdn4.iconfinder.com/data/icons/rcons-hands-gesture-line/30/index_finger_attention_hand_specify_gesture-1024.png)

3 - ий жест:


![Alt-текст](https://nastroy.net/pic/images/201906/699868-1561286480.jpg)



В соответсвие с показанными жестами будет выводиться изображение в красном, зеленом или синим цветах.

Для выполениния данного проекта я использовала библиотеку "mediapipe". Жесты я определяла по выпрямленным пальцам. 


Впрямлен ли палец я проверяю таким образом, находя расстояние между точек:


```
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
```

Проверяю выполнение жеста сединения двух пальцев:

```
def jest(results):
    ax1 = results.multi_hand_landmarks[0].landmark[4].x
    ay1 = results.multi_hand_landmarks[0].landmark[4].y
    ax2 = results.multi_hand_landmarks[0].landmark[20].x
    ay2 = results.multi_hand_landmarks[0].landmark[20].y
    if math.hypot(ax1 - ax2, ay1 - ay2) < 0.05:
        return True
```

В моей работе так же присутсвуют недостатки, такие как:

1) Из-за несовершенства библиотеки "Mediapipe" некоторые жесты могу распознаваться не точно и вам выведется не то, изображение которые вы хотите
2) Так же если рука у вас сжата в кулак, то это можно распознать как третий жест (опять же это происходит из-за несовершентсва бибилиотеки). Однако я думаю, что эту проблему можно исправить,тем что поставить условие, что третий и второй пальцы должны быть выпрямлены тоже.
