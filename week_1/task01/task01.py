import pandas as pd
import numpy as np

# 1번
arr1 = np.random.randn(5, 3)
arr2 = np.random.randn(3, 2)
arr_new = arr1 @ arr2

print(arr_new, arr_new.shape)


# 2번
arr1 = np.array([[5,7], [9,11]])
arr2 = np.array([[2,4], [6,8]])
result1 = np.concatenate((arr1,arr2),axis=0)
result2 = np.concatenate((arr1,arr2),axis=1)

print(result1, result2)

# 3번
idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

arr = pd.Series(data, idx)
series = arr[(arr>=10) & (arr<=20)]

print(series)


# 4번
df1 = pd.DataFrame([
    ['cherry', 'fruit', 100],
    ['mango', 'fruit', 110],
    ['potato', 'vegetable', 60],
    ['onion', 'vegetable', 80]],
    columns=['name', 'type', 'price'], index=[1, 2, 3, 4]
)

df2 = pd.DataFrame([
    ['pepper', 'vegetable', 50],
    ['carrot', 'vegetable', 70],
    ['banana', 'fruit', 90],
    ['kiwi', 'fruit', 120]],
    columns=['name', 'type', 'price'], index=[1, 2, 3, 4]
)

df_total = pd.concat([df1, df2])


# print(df_total.sort_values('type'))
# type기준 데이터 정렬, 가장 비싼 야채와 과일 구하기
df_sort = df_total.sort_values(['type', 'price'], ascending=[True, False])
df_sort_top = df_sort.groupby('type').head(1)

# 가격 합 구하기
sum_of_Top = df_sort_top['price'].sum()
print(sum_of_Top)

# 5번
df1 = pd.DataFrame([
    [55, 65, 60, 66, 57],
    [64, 77, 71, 79, 67],
    [88, 81, 79, 89, 77],
    [45, 35, 30, 46, 47],
    [91, 96, 90, 97, 99]],
    columns=['1r', '2r', '3r', '4r', '5r'],
    index=['Sue', 'Ryan', 'Jay', 'Jane', 'Anna']
)

print(df1.describe().loc[['mean', 'max', 'min']])




