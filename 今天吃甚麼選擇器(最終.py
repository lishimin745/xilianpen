import tkinter as tk
from tkinter import ttk
import random
import time
from threading import Thread

#設定
FONT_FAMILY = "標楷體"
FONT_LARGE = (FONT_FAMILY, 18)
FONT_MEDIUM = (FONT_FAMILY, 16)
FONT_SMALL = (FONT_FAMILY, 14)
BG_COLOR = "#f9f5f0"
FG_COLOR = "#4a4a4a"
BTN_BG = "#c8e6c9"
BTN_FG = "#2e7d32"


meal_items = {
    "早餐": ["起司蛋餅+奶茶", "燒餅+豆漿", "油條+杏仁茶", "稀飯+牛奶", "鐵板麵+紅茶",
            "饅頭夾蛋+米漿", "蘿蔔糕+豆漿紅茶", "豬肉漢堡+紅茶", "肉鬆三明治+奶茶", "熱狗+奶茶",
            "小肉豆+紅茶", "火腿蛋餅+紅茶", "肉包+豆漿", "厚片吐司+奶茶", "飯糰+米漿",
            "韭菜盒子+豆漿", "蔥抓餅+奶茶", "麥片牛奶", "麵線羹", "荷包蛋+牛奶",
            "地瓜粥", "炒泡麵+紅茶", "7-11茶葉蛋+奶茶", "鹹豆漿", "薯餅蛋餅+玉米濃湯",
            "牛肉漢堡+紅茶", "鮪魚蛋餅+奶茶", "鍋貼+杏仁茶", "火腿三明治+豆漿", "小籠包+米漿"],
    "午餐": ["鹽酥雞便當 + 珍珠奶茶","滷肉飯加滷蛋 + 紅茶牛奶","雞腿排便當 + 冬瓜檸檬",
            "蚵仔麵線 + 青草茶","雙拼鐵路便當（排骨+香腸）+ 黑糖鮮奶","排骨便當 + 鮮奶茶",
            "鐵板牛肉飯 + 柳橙汁","滷味拼盤（附麵）+ 百香綠茶","肉羹飯 + 檸檬愛玉",
            "炒米粉＋貢丸湯 + 薏仁漿","虱目魚肚飯 + 鳳梨冰茶","酸菜白肉鍋定食 + 檸檬紅茶",
            "牛肉捲餅＋小菜 + 黑咖啡","刈包＋四神湯 + 鮮榨西瓜汁","牛肉湯＋肉燥飯 + 木瓜牛奶",
            "韓式拌飯台味版 + 青梅綠茶","蚵仔煎＋米糕 + 芒果冰沙","控肉飯 + 芋頭鮮奶",
            "鹽水雞拼飯 + 桂花烏梅汁","泰式椒麻雞飯 + 柚子茶","香煎雞腿排飯 + 仙草蜜",
            "鍋燒意麵 + 鮮奶紅茶","魯排骨飯 + 黑糖仙草凍飲","麻油雞飯 + 金桔檸檬","鴨肉飯＋筍乾 + 烏龍茶",
            "炸醬麵＋小菜三樣 + 可可牛奶","滷雞腿飯 + 鮮榨葡萄柚汁","花枝羹米粉 + 山粉圓飲",
            "滷大腸＋乾麵 + 米漿","沙茶牛肉炒飯 + 四季春青茶"],
    "晚餐": ["壽司", "速食店", "夜市", "火鍋", "義大利麵", "學餐", "漢堡", "便當", "小吃", "滷味",
            "咖哩飯", "炒麵", "炒飯", "拉麵", "便利商店", "鍋貼", "披薩", "牛排", "沙拉", "粥",
            "鬆餅", "越南河粉", "章魚燒", "蛋包飯", "滷肉飯", "鍋燒意麵", "關東煮", "泡麵", "飯糰"],
    "宵夜": ["漢堡", "薯條", "串燒", "珍珠奶茶", "粥", "包子", "拉麵", "鍋燒意麵", "鹽水雞", "去睡覺，睡了就不餓了", 
            "炸甜不辣", "雞排", "炸百頁", "麥片牛奶", "玉米濃湯", "麥脆雞", "無糖豆漿+茶葉蛋", "炸四季豆+大豆干", 
            "碗裝泡麵", "冰箱裡有什麼吃什麼","可樂","汽水","炒海瓜子"]
}

afternoon_desserts = ["提拉米蘇", "馬卡龍", "檸檬塔", "抹茶蛋糕", "千層蛋糕", "可麗露",
    "布朗尼","蘋果派","起司蛋糕","奶酪","泡芙","舒芙蕾","蛋塔","瑪德蓮",
    "冰淇淋","芝麻湯圓","紅豆湯","綠豆糕","鳳梨酥","黑糖糕 ","地瓜球",
    "愛玉凍","剉冰","豆花","車輪餅","蛋黃酥","月餅","花生糖","麻糬","仙草凍"]

afternoon_drinks = ["珍珠奶茶", "抹茶拿鐵", "黑咖啡", "水果茶", "奶蓋紅茶", "熱可可",
          "仙草凍奶茶", "烏龍奶茶", "四季春青茶", "百香果綠茶", "檸檬愛玉", "芒果冰沙",
          "拿鐵", "卡布奇諾", "摩卡咖啡", "焦糖瑪奇朵", "榛果拿鐵", "柚子茶",
          "冬瓜檸檬", "東方美人茶", "烏龍茶", "普洱茶", "洛神花茶", "檸檬紅茶",
          "蜜香紅茶", "茉莉花綠茶", "桂花烏龍", "桂圓紅棗茶（熱飲）", "龍井茶", "葡萄柚綠茶"]

brunch_desserts = ["豬肉煎蛋堡", "蘑菇麵", "燻雞沙拉", "薯餅蛋堡", "韓式泡菜豬肉總匯",
              "高麗蔬菜火腿蛋吐司", "培根蛋可頌", "低脂舒肥雞+烤土司+水煮蛋", "烤奶油吐司+西式炒蛋",
              "鮪魚馬芬堡+生菜沙拉", "法國吐司佐蜂蜜+太陽蛋+生菜沙拉", "烤奶油吐司+德國香腸+西式炒蛋", "雞腿帕瑪森軟法+太陽蛋+生菜沙拉", 
              "法式火腿考乳酪三明治+水果優格", "牛肉可頌堡", "奶油起司雞肉麵", "火腿蛋方形海苔御飯糰", 
              "蘿蔔糕+火腿蛋餅", "鬆餅+德國香腸+西式炒蛋", "草莓果醬吐司+雞塊", "蔬菜起司蛋堡+薯條", "肉醬焗烤土司", 
              "火腿潛挺堡+生菜沙拉", "山形吐司+培根+西式炒蛋", "蘿蔔糕+唐揚雞塊+脆薯", "煎豬排+生菜沙拉+水果優格", 
              "法式吐司+玉米蛋+水果優格", "雙層起司牛肉堡+脆薯+生菜沙拉", "火腿歐姆蛋貝果+莫札瑞拉起司條", "蜂蜜鬆餅+水果優格",
              "全麥吐司+西式炒蛋", "藍莓果醬吐司+蜂蜜優格"]
brunch_drinks = ["紅茶拿鐵", "抹茶拿鐵", "黑咖啡", "水果茶", "柳橙汁", "南瓜濃湯",
                  "美式咖啡", "鮮奶", "玉米濃湯", "蘋果汁", "葡萄汁", "水",
                  "熱水", "莓果茶", "摩卡咖啡", "柚子茶","水果花茶", "熱紅茶", "開水", "豆漿", "薏仁茶", "米漿"]



class MealRoulette:
    def __init__(self, frame, items):
        self.items = items
        frame.configure(bg=BG_COLOR)
        self.label = tk.Label(frame, text="今天吃……", font=FONT_LARGE, width=30, height=3, bg=BG_COLOR, fg=FG_COLOR)
        self.label.pack(pady=20)
        self.button = tk.Button(frame, text="開始", command=self.start_spin, font=FONT_SMALL, bg=BTN_BG, fg=BTN_FG)
        self.button.pack(pady=10)

    def start_spin(self):
        Thread(target=self.spin).start()

    def spin(self):
        self.button.config(state="disabled")
        for i in range(30):
            choice = random.choice(self.items)
            self.label.config(text=choice)
            time.sleep(0.1 + i * 0.01)
        self.button.config(state="normal")


class ComboSpinPicker:
    def __init__(self, frame, list1, list2, title="隨機組合"):
        self.list1 = list1
        self.list2 = list2
        self.title = title
        self.frame = frame
        frame.configure(bg=BG_COLOR)

        self.label = tk.Label(
            frame, text=f"今天{title}吃……", font=FONT_MEDIUM,
            wraplength=300, justify="center", bg=BG_COLOR, fg=FG_COLOR
        )
        self.label.pack(pady=20)

        self.button = tk.Button(
            frame, text="🎲 開始轉動", font=FONT_SMALL,
            command=self.start_spin, bg=BTN_BG, fg=BTN_FG
        )
        self.button.pack(pady=10)

    def start_spin(self):
        Thread(target=self.spin).start()

    def spin(self):
        self.button.config(state="disabled")
        for i in range(30):
            combo = f"{random.choice(self.list1)} + {random.choice(self.list2)}"
            self.label.config(text=combo)
            time.sleep(0.1 + i * 0.01)
        self.button.config(state="normal")


#主畫面
root = tk.Tk()
root.title("多功能餐點轉盤")
root.geometry("500x450")
root.configure(bg=BG_COLOR)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')


tab_order = [
    ("早餐", meal_items["早餐"]),
    ("早午餐", (brunch_desserts, brunch_drinks)),
    ("午餐", meal_items["午餐"]),
    ("下午茶", (afternoon_desserts, afternoon_drinks)),
    ("晚餐", meal_items["晚餐"]),
    ("宵夜", meal_items["宵夜"])
]

for name, items in tab_order:
    frame = tk.Frame(notebook)
    frame.pack_propagate(False)
    notebook.add(frame, text=name)

    if name in meal_items:
        MealRoulette(frame, items)
    elif name == "早午餐":
        ComboSpinPicker(frame, brunch_desserts, brunch_drinks, title="早午餐")
    elif name == "下午茶":
        ComboSpinPicker(frame, afternoon_desserts, afternoon_drinks, title="下午茶")

root.mainloop()


