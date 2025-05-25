import tkinter as tk
import random
import time
from threading import Thread


breakfast_items = [
    "起司蛋餅+奶茶", "燒餅+豆漿", "油條+杏仁茶", "稀飯+牛奶", "鐵板麵+紅茶", 
    "饅頭夾蛋+米漿", "蘿蔔糕+豆漿紅茶", "豬肉漢堡+紅茶", "肉鬆三明治+奶茶", "熱狗+奶茶",
    "小肉豆+紅茶", "火腿蛋餅+紅茶", "肉包+豆漿", "厚片吐司+奶茶", "飯糰+米漿", 
    "韭菜盒子+豆漿", "蔥抓餅+奶茶", "麥片牛奶", "麵線羹", "荷包蛋+牛奶", 
    "地瓜粥", "炒泡麵+紅茶", "7-11茶葉蛋+奶茶", "鹹豆漿", "薯餅蛋餅+玉米濃湯", 
    "牛肉漢堡+紅茶", "鮪魚蛋餅+奶茶", "鍋貼+杏仁茶", "火腿三明治+豆漿", "小籠包+米漿"
]

class BreakfastRoulette:
    def __init__(self, root):
        self.root = root
        self.root.title("早餐選擇轉盤")

        self.label = tk.Label(root, text="今天吃……", font=("Arial", 24), width=30, height=3)
        self.label.pack(pady=30)

        self.button = tk.Button(root, text="開始", command=self.start_spin, font=("Arial", 16))
        self.button.pack(pady=20)

    def start_spin(self):
        Thread(target=self.spin).start()

    def spin(self):
        self.button.config(state="disabled")
        for i in range(30):  
            choice = random.choice(breakfast_items)
            self.label.config(text=choice)
            time.sleep(0.1 + i * 0.01)  
        self.button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakfastRoulette(root)
    root.mainloop()

