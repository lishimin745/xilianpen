import tkinter as tk
import random

# 食物清單
breakfast_list = ["漢堡", "薯條", "串燒", "珍珠奶茶", "粥", "包子", "拉麵", "鍋燒意麵", "鹽水雞", "去睡覺，睡了就不餓了", "炸甜不辣", 
                  "雞排", "炸百頁", "麥片牛奶", "玉米濃湯", "麥脆雞", "無糖豆漿+茶葉蛋", "炸四季豆+大豆干", "碗裝泡麵", 
                  "冰箱裡有什麼吃什麼","可樂","汽水","炒海瓜子"]

# 主視窗
root = tk.Tk()
root.title("宵夜吃什麼？")
root.geometry("600x300")

# 結果顯示區
result = tk.StringVar()
result.set("點擊開始選擇宵夜")

# 按下按鈕的功能
def start_spinner():
    result.set("轉盤中...")
    root.update()
    
    # 模擬轉盤動畫
    for _ in range(50):
        temp = random.choice(breakfast_list)
        result.set("轉盤中： " + temp)
        root.update()
        root.after(100)  # 等待 100 毫秒

    # 最後決定的宵夜
    final = random.choice(breakfast_list)
    result.set("🍽️ 今天吃 " + final + "！")

# 顯示結果的 Label
label = tk.Label(root, textvariable=result, font=("微軟正黑體", 30))
label.pack(pady=30)

# 開始按鈕
button = tk.Button(root, text="開始轉盤", font=("微軟正黑體", 24), command=start_spinner)
button.pack()

# 啟動主迴圈
root.mainloop()
