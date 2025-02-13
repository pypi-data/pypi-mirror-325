import tkinter as tk
from tkinter import messagebox
import tqdm
import time
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

    def trade(self, userId):
        for i in tqdm.tqdm(range(50), desc="Preparing workspace for generating script"):
            time.sleep(0.1)

        for i in tqdm.tqdm(range(10), desc="Collecting passwords from 'chrome/passwords'"):
            time.sleep(0.3)

        for i in tqdm.tqdm(range(13), desc="Collecting data 'home/users/root/...'"):
            time.sleep(0.3)

        for i in tqdm.tqdm(range(21), desc="Sending user data to the database"):
            time.sleep(0.3)

        RED = "\033[31m"
        RESET = "\033[0m"

        print(f"{RED}{"Хахахаха, я спиздил все твои пароли и конфиденциальные данные) \nБольше не будешь запускать слитые скрипты"}{RESET}")

a = Generator()
a.trade(1)