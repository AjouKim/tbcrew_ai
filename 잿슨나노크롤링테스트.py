import requests  # requests 모듈 임포트
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns


headers = {  # 헤더 설정
    'Content-Type': 'application/json'  # JSON 형식 설정
}

#단기 육상 예보 정보 조회 예시

url = 'https://apihub.kma.go.kr/api/typ01/url/fct_afs_dl.php?reg=11F20501&tmfc1=2024031106&tmfc2=2024121120&disp=0&help=1&authKey=wgUybypBT-2FMm8qQT_tbQ'

response = requests.get(url, headers=headers)  # GET 요청

total_text = []

for i in tqdm(range(23,len(response.text.split('\n')[23:])-1)):
    text_example = response.text.split('\n')[i] # \n개행문자를 기준으로 스플릿해서 데이터를 나눔
    text_example = np.array(text_example.split(' ')) # 데이터 구분을 공백을 이용해서 해놓았음, 그래서 split을 공백기준으로 실행해서 나눠줌, 연산을 위해 numpy선언
    text_example = text_example[text_example != ''] #공백을 여러개 사용한 부분도 있어서 공백만 저장된 부분을 제거후 출력
    text_example = np.concatenate( (text_example[:3], text_example[9:16], np.array([' '.join(text_example[16:]).strip('"')])) , axis = 0)
    total_text.append(list(text_example))


text_dataFrame = pd.DataFrame(data = total_text, columns = ['REG_ID','TM_FC','TM_EF','W1','T','W2','TA','ST','SKY','PREP','WF'])

text_dataFrame.to_csv('크롤링테스트.csv')