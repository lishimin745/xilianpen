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
