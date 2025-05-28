import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Поиск лиц в видео!!!")
        self.root.geometry("800x600")
        
        # Загрузка каскада Хаара для обнаружения лиц
        self.face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        if self.face_cascade.empty():
            print("Ошибка загрузки каскада Хаара!")
            exit()
        
        self.video_path = ""
        self.is_playing = False
        self.current_frame = None
        self.create_widgets()
    
    def create_widgets(self):
        # Фрейм для видео
        self.video_frame = tk.Label(self.root)
        self.video_frame.pack(pady=10)
        
        # Кнопка выбора видео
        self.select_btn = tk.Button(self.root, text="Выбрать видео", command=self.select_video)
        self.select_btn.pack(pady=5)
        
        # Кнопка запуска/остановки
        self.play_btn = tk.Button(self.root, text="Старт", command=self.toggle_playback, state=tk.DISABLED)
        self.play_btn.pack(pady=5)
        
        # Кнопка выхода
        self.exit_btn = tk.Button(self.root, text="Выход", command=self.root.quit)
        self.exit_btn.pack(pady=5)
        
        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("Выберите видеофайл")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def select_video(self):
        filetypes = (("Видео файлы", "*.mp4 *.avi *.mov"), ("Все файлы", "*.*"))
        self.video_path = filedialog.askopenfilename(title="Выберите видеофайл", filetypes=filetypes)
        
        if self.video_path:
            self.status_var.set(f"Выбрано видео: {self.video_path}")
            self.play_btn.config(state=tk.NORMAL)
    
    def toggle_playback(self):
        if not self.is_playing:
            self.is_playing = True
            self.play_btn.config(text="Стоп")
            self.select_btn.config(state=tk.DISABLED)
            
            # Запуск обработки видео в отдельном потоке
            self.thread = threading.Thread(target=self.process_video, daemon=True)
            self.thread.start()
        else:
            self.is_playing = False
            self.play_btn.config(text="Старт")
            self.select_btn.config(state=tk.NORMAL)
    
    def process_video(self):
        cap = cv2.VideoCapture(self.video_path)
        
        if not cap.isOpened():
            self.status_var.set("Ошибка: не удалось открыть видео!")
            return
        
        while self.is_playing:
            ret, frame = cap.read()
            
            # Видео закончилось
            if not ret:
                self.is_playing = False
                self.play_btn.config(text="Старт")
                self.select_btn.config(state=tk.NORMAL)
                self.status_var.set("Видео завершено")
                break
            
            # Обнаружение лиц
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            # Рисование прямоугольников вокруг лиц
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Отображение кадра в интерфейсе
            self.display_frame(frame)
            
            # Небольшая задержка для контроля скорости воспроизведения
            cv2.waitKey(30)
        
        cap.release()
    
    def display_frame(self, frame):
        # Конвертация кадра для отображения в Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        
        # Обновление изображения
        self.video_frame.config(image=img)
        self.video_frame.image = img
        
        # Обновление статуса
        self.root.update()

root = tk.Tk()
app = FaceDetectionApp(root)
root.mainloop()