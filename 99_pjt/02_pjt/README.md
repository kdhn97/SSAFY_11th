# 학습내용 (파이썬 패키지)
- Numpy - 수학 계산용 패키지, Pandas와 Matplotlib를 사용하기 위해 활용되는 패키지
- Pandas - 원하는 데이터만 추출하거나 데이터를 분석할 때 활용되는 패키지
- Matplotlib - 그래프를 그려주는 패키지

[ Numpy ]
- 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 파이썬 패키지
- 장점 : Python 반복문에 비해 빠르다, 다차원 행렬자료 구조 제공
- 특징 : Python에서만 사용 가능

[ Pandas ]
- Numpy의 한계 - 유연성이 부족, 그룹화, 피벗 구조화 부족
- Pandas는 프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조
- Numpy 기반으로 만들어진 패키지로, 1차원 배열과 2차원 배열이라는 효율적인 자료구조 제공

[ Matplotlib ]
- Python에서 데이터 시각화를 위해 가장 널리 사용되는 라이브러리
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 오늘의 PJT (Netflix 주가 데이터 분석)
### 패키지 설치 및 import
pip install numpy
pip install pandas
pip install matplotlib

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### csv파일 읽어오기
pd.read_csv('NFLX.csv', encoding='cp949')

### 2021년 이후 데이터 필터
df[df['Date'] >= '2021-01-01']

### 그래프 생성
plt.plot(df_after_2021['Date'], df_after_2021['Close'])

### 제목 및 x축, y축 생성
plt.title('NFLX Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')

### x축 45도 기울이기
plt.xticks(rotation=45)

### 그래프 보이기
plt.show()

### 최댓값, 최솟값 출력
df['Close'].max()
df['Close'].min()
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 어려웠던 내용 - 2021년도 이후 월 별 평균 종가 그룹화하기
df_after_2021.groupby(df_after_2021['Date'].dt.to_period('M')).mean()
### 그룹화에 대한 내용을 이해하는데 시간이 오래 걸렸습니다.