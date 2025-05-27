import tkinter as tk
import random

desserts = ["提拉米蘇", "馬卡龍", "檸檬塔", "抹茶蛋糕", "千層蛋糕", "可麗露",
            "布朗尼","蘋果派","起司蛋糕","奶酪","泡芙","舒芙蕾","蛋塔","瑪德蓮",
            "冰淇淋","芝麻湯圓","紅豆湯","綠豆糕","鳳梨酥","黑糖糕 ","地瓜球",
            "愛玉凍","剉冰","豆花","車輪餅","蛋黃酥","月餅","花生糖","麻糬"
            ,"仙草凍"]
drinks = ["珍珠奶茶", "抹茶拿鐵", "黑咖啡", "水果茶", "奶蓋紅茶", "熱可可",
          "仙草凍奶茶", "烏龍奶茶", "四季春青茶", "百香果綠茶", "檸檬愛玉", "芒果冰沙",
          "拿鐵", "卡布奇諾", "摩卡咖啡", "焦糖瑪奇朵", "榛果拿鐵", "柚子茶",
          "冬瓜檸檬", "東方美人茶", "烏龍茶", "普洱茶", "洛神花茶", "檸檬紅茶",
          "蜜香紅茶", "茉莉花綠茶", "桂花烏龍", "桂圓紅棗茶（熱飲）", "龍井茶", "葡萄柚綠茶",
          ]

def spin_combo():
    dessert = random.choice(desserts)
    drink = random.choice(drinks)
    result_label.config(text=f"下午茶組合：{dessert} + {drink}")

root = tk.Tk()
root.title("下午茶隨機轉盤")
root.geometry("300x150")

# 設定文字置中並佔滿水平跟垂直空間
result_label = tk.Label(root, text="今天的下午茶吃什麼？", font=("Arial", 16), anchor="center", justify="center")
result_label.pack(expand=True, fill='both')

spin_button = tk.Button(root, text="轉組合", command=spin_combo, width=20, height=2)
spin_button.pack(side="bottom", pady=20)

root.mainloop()




import tkinter as tk
import random

# 食物清單
foods = [
    "壽司", "速食店", "夜市", "火鍋", "義大利麵", "學餐", "漢堡", "便當", "小吃", "滷味",
    "咖哩飯", "炒麵", "炒飯", "拉麵", "便利商店", "鍋貼", "披薩", "牛排", "沙拉", "粥",
    "鬆餅", "越南河粉", "章魚燒", "蛋包飯", "滷肉飯", "鍋燒意麵", "關東煮", "泡麵", "飯糰"
]

def spin_wheel():
    spin_button.config(state="disabled")  # 轉盤期間禁用按鈕
    for i in range(20):  # 模擬轉動 20 次
        result = random.choice(foods)
        result_label.config(text=f"轉啊轉… {result}")
        root.update()
        root.after(100 + i * 10)  # 每次轉慢一點
    final_result = random.choice(foods)
    result_label.config(text=f"今晚吃：{final_result}！")
    spin_button.config(state="normal")  # 啟用按鈕

# 建立視窗
root = tk.Tk()
root.title("今晚吃什麼？")
root.geometry("300x200")

# 顯示結果
result_label = tk.Label(root, text="點下按鈕開始", font=("Arial", 16))
result_label.pack(pady=30)

# 轉盤按鈕
spin_button = tk.Button(root, text="開始轉盤", font=("Arial", 14), command=spin_wheel)
spin_button.pack()

# 啟動主迴圈
root.mainloop()
