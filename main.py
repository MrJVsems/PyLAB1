import time

def smwt13(arr):
    start_time = time.perf_counter()
    rsm = 0
    if 13 in arr:
        for i in range(arr.index(13)):
            rsm += arr[i]
    else:
        for el in arr:
            rsm += el
    elap_time = time.perf_counter() - start_time
    print(f"Вычисление заняло {elap_time} секунд")
    return rsm

def smwt13_2(arr):
    start_time = time.perf_counter()
    rsm = 0
    for el in arr:
        if el == 13:
            break
        rsm += el
    elap_time = time.perf_counter() - start_time
    print(f"Вычисление заняло {elap_time} секунд")
    return rsm



print('Введите размер массива, затем элементы массива')

s = []
for i in range(int(input())):
    s.append(int(input()))

print(smwt13(s))
print(smwt13_2(s))