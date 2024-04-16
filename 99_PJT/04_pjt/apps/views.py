from django.shortcuts import render

# 하단에 3.9.13 누르고 venv로 활성화
import matplotlib.pyplot as plt 

# io : 입출력 연산을 위한 python 표준 라이브러리
# BytesIO : 이진 데이터를 다루기 위한 버퍼를 제공
from io import BytesIO

# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
import base64

import pandas as pd



# Create your views here.
def index(request):
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    plt.plot(x, y)
    plt.title('test graph')
    plt.xlabel('x label')
    plt.ylabel('y label')

    # plt.show() # 새 창이 열린다
    buffer = BytesIO()

    # buffer에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8'.replace('\n', ''))
    buffer.close()

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ csv 파일 읽어오기
    # 파일을 읽어야 함
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)

    context = {
        # 라이브러리를 통채로 넘기는 건 아니다
        # 'plt': plt,

        # 이미지를 웹 페이지에 표시하기 위해서는 이미지 경로가 필요하다
        # 'img_base64': img_base64,
        'image': f'data:image/png;base64, {img_base64}',
        'df': df,
    }
    return render(request, 'index.html', context)
