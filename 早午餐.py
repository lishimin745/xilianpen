import tkinter as tk
import random

desserts = ["豬肉煎蛋堡", "蘑菇麵", "燻雞沙拉", "薯餅蛋堡", "韓式泡菜豬肉總匯",
    "高麗蔬菜火腿蛋吐司+紅茶拿鐵", "培根蛋可頌", "低脂舒肥雞+烤土司+水煮蛋", "烤奶油吐司+西式炒蛋",
    "鮪魚馬芬堡+生菜沙拉", "法國吐司佐蜂蜜+太陽蛋+生菜沙拉", "烤奶油吐司+德國香腸+西式炒蛋", "雞腿帕瑪森軟法+太陽蛋+生菜沙拉", 
    "法式火腿考乳酪三明治+水果優格", "牛肉可頌堡", "奶油起司雞肉麵", "火腿蛋方形海苔御飯糰", 
    "蘿蔔糕+火腿蛋餅", "鬆餅+德國香腸+西式炒蛋", "草莓果醬吐司+雞塊", "蔬菜起司蛋堡+薯條", "肉醬焗烤土司", 
    "火腿潛挺堡+生菜沙拉", "山形吐司+培根+西式炒蛋", "蘿蔔糕+唐揚雞塊+脆薯", "煎豬排+生菜沙拉+水果優格", 
    "法式吐司+玉米蛋+水果優格", "雙層起司牛肉堡+脆薯+生菜沙拉", "火腿歐姆蛋貝果+莫札瑞拉起司條", "蜂蜜鬆餅+水果優格",
    "全麥吐司+西式炒蛋", "藍莓果醬吐司+蜂蜜優格"]
drinks = ["紅茶拿鐵", "抹茶拿鐵", "黑咖啡", "水果茶", "柳橙汁", "南瓜濃湯",
              "美式咖啡", "鮮奶", "玉米濃湯", "蘋果汁", "葡萄汁", "水",
              "熱水", "莓果茶", "摩卡咖啡", "柚子茶","水果花茶", "熱紅茶", "開水", "豆漿", "薏仁茶", "米漿",
          ]

def spin_combo():
    dessert = random.choice(desserts)
    drink = random.choice(drinks)
    result_label.config(text=f"早午餐組合：{dessert} + {drink}")

root = tk.Tk()
root.title("早午餐隨機轉盤")
root.geometry("300x150")

# 設定文字置中並佔滿水平跟垂直空間
result_label = tk.Label(root, text="今天的早午餐吃什麼？", font=("Arial", 16), anchor="center", justify="center")
result_label.pack(expand=True, fill='both')

spin_button = tk.Button(root, text="轉組合", command=spin_combo, width=20, height=2)
spin_button.pack(side="bottom", pady=20)

root.mainloop()
