import tkinter as tk
from tkinter import messagebox
class Generator():

    def __init__(self, appId = None):
        self.appId = appId

    def show_popup(self, title, message, color):
        # Создаем новое всплывающее окно
        popup = tk.Toplevel()
        popup.title(title)

        # Настраиваем надпись с цветом
        label = tk.Label(popup, text=message, fg=color)
        label.pack(padx=20, pady=20)

        # Кнопка для закрытия окна
        close_button = tk.Button(popup, text="Закрыть", command=popup.destroy)
        close_button.pack(pady=10)

    def generate(self, userId):
        root = tk.Tk()
        root.title("Угроза утечки данных!")

        # Кнопка для вызова первого всплывающего окна
        button1 = tk.Button(root, text="Раскрыть",
                            command=lambda: self.show_popup("Утечка конфиденциальной информации!", "Обнаружена программа-шпион!", "red"))
        button1.pack(pady=10)

        # Кнопка для вызова второго всплывающего окна
        button2 = tk.Button(root, text="Раскрыть",
                            command=lambda: self.show_popup("Утечка паролей", "Обнаружена программа-шпион", "red"))
        button2.pack(pady=10)

        # Запускаем главный цикл
        root.mainloop()
