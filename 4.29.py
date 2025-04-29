print("hello word")


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 假設目前未排序部分的第一個元素是最小值
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 將最小值放到已排序部分的末尾
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 測試
arr = [3, 25, 1, 62, 11]
print("原始數組:", arr)
sorted_arr = selection_sort(arr)
print("排序後數組:", sorted_arr)
