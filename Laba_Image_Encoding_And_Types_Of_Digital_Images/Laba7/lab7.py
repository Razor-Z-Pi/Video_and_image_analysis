import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
while True:
    print("Запустить поиск лиц в видео? 1 - Да; 2 - Нет")
    result = int(input())
    if(result == 2):
        break
    elif result > 2:
        continue
    else:
        print("Поехали!!!")

    while True:
        print("Выберите цифру с видое: 1) Люди; 2) Аниме; 3) Игра.")
        index = int(input())
        if index == 1:
            capture_io = cv2.VideoCapture('./people.mp4')
            break
        elif index == 2:
            capture_io = cv2.VideoCapture('./template.mp4')
            break
        elif index == 3:
            capture_io = cv2.VideoCapture('./template2.mp4')
            break
        else:
            print("Что-то пошло не так!!! Попробуйте ещё раз")

    if not capture_io.isOpened():
        print("Ошибка: видео не найдено или путь указан неверно!")
        break

    while True:
        _, img = capture_io.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('img', img)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    capture_io.release()
    cv2.destroyAllWindows()