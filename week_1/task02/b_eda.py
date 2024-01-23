import warnings
warnings.filterwarnings("ignore")

import os
from os.path import join

import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold, cross_val_score
import xgboost as xgb
import lightgbm as lgb

import matplotlib.pyplot as plt
import seaborn as sns


train_data_path = './data/train.csv'
test_data_path = './data/test.csv'

data = pd.read_csv(train_data_path)
sub = pd.read_csv(test_data_path)
print('train data dim : {}'.format(data.shape))
print('sub data dim : {}'.format(sub.shape))

# data의 price를 y로 옮기기
y = data['price']

## 코드시작 ##
# 미션 2 코드 작성 : data에서 price 컬럼을 완전히 삭제하기

data = data.drop('price', axis=1)


## 코드종료 ##

print(data.columns)

train_len = len(data) # 학습데이터의 수
data = pd.concat((data, sub), axis=0) # 학습데이터와 테스트 데이터 합치기

print(len(data)) # 합쳐진 데이터의 수
data.head() # 데이터 확인

data.info()


## 코드시작 ##
# 미션 3-1 코드 작성 : data에 isna와 sum을 적용하여 각 컬럼의 결측치 수를 확인해보세요.

missing = data.isna().sum() # '...' 을 코드로 채워주세요
print(missing)


## 코드종료 ##

missing/data.shape[0]

data.describe()


import missingno as msno # 라이브러리 임포트

## 코드시작 ##
# 미션 3-2 코드 작성 : data에 결손치를 missingno 라이브러리를 이용하여 시각화 해보세요.
msno.matrix(data)
plt.show()

## 코드종료 ##

sub_id = data['id'][train_len:]
del data['id']

print(data.columns)

data['date'] = data['date'].apply(lambda x : str(x[:6]))
data.head()

fig, ax = plt.subplots(9, 2, figsize=(12, 50))   # 가로스크롤 때문에 그래프 확인이 불편하다면 figsize의 x값을 조절해 보세요.

# date 변수(count==0인 경우)는 제외하고 분포를 확인
count = 1
columns = data.columns
for row in range(9):
    for col in range(2):
        sns.kdeplot(data=data[columns[count]], ax=ax[row][col])
        ax[row][col].set_title(columns[count], fontsize=15)
        count += 1
        if count == 19 :
            break

## 코드시작 ##
# 미션 4 코드 작성 : 로그변환을 수행해보세요.

# 치우친 분포의 컬럼을 저장해 두기
skew_columns = ['bedrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_lot15', 'sqft_living15']

for c in skew_columns:
    data[c] = np.log1p(data[c])   # '...' 을 코드로 채워주세요

## 코드종료 ##

fig, ax = plt.subplots(4, 2, figsize=(12, 24))

count = 0
for row in range(4):
    for col in range(2):
        if count == 7:
            break
        sns.kdeplot(data=data[skew_columns[count]], ax=ax[row][col])
        ax[row][col].set_title(skew_columns[count], fontsize=15)
        count += 1


xx = np.linspace(0, 10, 500)
yy = np.log(xx)

plt.hlines(0, 0, 10)
plt.vlines(0, -5, 5)
plt.plot(xx, yy, c='r')
plt.show()

sns.kdeplot(y) # y는 미션 2에서 price를 저장하고 있음.
plt.show()

y_log_transformation = np.log1p(y) # 미션4의 힌트가 되겠네요 ^^

sns.kdeplot(y_log_transformation)
plt.show()

sub = data.iloc[train_len:, :]
x = data.iloc[:train_len, :]

print(x.shape)
print(sub.shape)
