import tkinter as tk
import random


meal_combos = [
    "鹽酥雞便當 + 珍珠奶茶",
    "滷肉飯加滷蛋 + 紅茶牛奶",
    "雞腿排便當 + 冬瓜檸檬",
    "蚵仔麵線 + 青草茶",
    "雙拼鐵路便當（排骨+香腸）+ 黑糖鮮奶",
    "排骨便當 + 鮮奶茶",
    "鐵板牛肉飯 + 柳橙汁",
    "滷味拼盤（附麵）+ 百香綠茶",
    "肉羹飯 + 檸檬愛玉",
    "炒米粉＋貢丸湯 + 薏仁漿",
    "虱目魚肚飯 + 鳳梨冰茶",
    "酸菜白肉鍋定食 + 檸檬紅茶",
    "牛肉捲餅＋小菜 + 黑咖啡",
    "刈包＋四神湯 + 鮮榨西瓜汁",
    "牛肉湯＋肉燥飯 + 木瓜牛奶",
    "韓式拌飯台味版 + 青梅綠茶",
    "蚵仔煎＋米糕 + 芒果冰沙",
    "控肉飯 + 芋頭鮮奶",
    "鹽水雞拼飯 + 桂花烏梅汁",
    "泰式椒麻雞飯 + 柚子茶",
    "香煎雞腿排飯 + 仙草蜜",
    "鍋燒意麵 + 鮮奶紅茶",
    "魯排骨飯 + 黑糖仙草凍飲",
    "麻油雞飯 + 金桔檸檬",
    "鴨肉飯＋筍乾 + 烏龍茶",
    "炸醬麵＋小菜三樣 + 可可牛奶",
    "滷雞腿飯 + 鮮榨葡萄柚汁",
    "花枝羹米粉 + 山粉圓飲",
    "滷大腸＋乾麵 + 米漿",
    "沙茶牛肉炒飯 + 四季春青茶"
]


def spin():
    count = 0
    def update():
        nonlocal count
        result_label.config(text=random.choice(meal_combos))
        count += 1
        if count < 15:
            root.after(100, update)
        else:
            final_choice = random.choice(meal_combos)
            result_label.config(text=f"☀️ 今日推薦 ☀️\n\n{final_choice}")
    update()


root = tk.Tk()
root.title("今天午餐ㄔ什麼?")
root.geometry("500x300")
root.configure(bg="#f9f5f0")  


font_family = "標楷體"


result_label = tk.Label(
    root,
    text="點擊按鈕，雖然你也沒錢吃，笑你。",
    font=(font_family, 16),
    wraplength=460,
    justify="center",
    anchor="center",
    bg="#f9f5f0",
    fg="#5a5a5a"
)
result_label.pack(pady=20, expand=True)


btn = tk.Button(
    root,
    text="🎡 開始轉盤 🎡",
    font=(font_family, 14),
    command=spin,
    bg="#c8e6c9",
    fg="#2e7d32",
    relief="groove",
    padx=10,
    pady=5
)
btn.pack(pady=10)

root.mainloop()
