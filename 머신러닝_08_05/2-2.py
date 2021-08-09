import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
#bream 도미 큰물고기 35
#smelt 빙어 작은물고기 14

#큰물고기 작은 물고기 판별해주는 프로그램



fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


#fish_length = np.array(fish_length)로 넘파이 배열로 만들어도 되지만 다른 방법을 이용한다.

#fish_data=[[l,w] for l,w in zip(fish_length,fish_weight)] 저번 시간에는 리스트 컴프레이션을 이용했고 이번시간에는 다른 방법을 사용한다.

fish_data = np.column_stack([fish_length,fish_weight]) #위 방법과 동일한 결과가 나오는 다른 방법이다.

#print(fish_data[:5])

fish_target= np.concatenate(( np.ones(35),np.zeros(14)) )
#print(fish_target[33:38])


train_input,test_input,traint_target,test_target = train_test_split(fish_data,fish_target,random_state=42)

#print(train_input.shape)
#print(test_input.shape)

plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(test_input[:,0],test_input[:,1])
plt.xlabel("length")
plt.ylabel("weigth")
#plt.show()


#수상한 도미 한마리


knclf = KNeighborsClassifier()
knclf.fit(train_input,traint_target)

prevalues=knclf.predict([[25,150]])
#print(prevalues)

plt.scatter(25,150)
#plt.show() #원래는 이 값은 test 값에 가까우나 prevalues 값은 0이라고 나온다 이것은 좌표 때문인데 이것을 수정해보려고 한다.

distances, indexes = knclf.kneighbors([[25,150]])


plt.scatter(train_input[indexes,0],train_input[indexes,1], marker='D')
plt.xlim((0,1000))

mean = np.mean(train_input, axis=0)#훈련데이터 평균값
std=np.std(train_input, axis=0)#표준점수


train_scaled = (train_input - mean) / std
new = ([25,150]-mean)/std
print(new[0],new[1])
plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(new[0],new[1],marker='^')
plt.xlabel('length')
plt.ylabel('weight')


knclf= KNeighborsClassifier(n_neighbors=7)
knclf.fit(train_scaled,traint_target)

distances,indexes=knclf.kneighbors([new])
plt.scatter(train_scaled[indexes,0],train_scaled[indexes,1])
plt.show()





#(실제데이터-평균값)/표준점수
#x좌표측의 데이터 범위와 y 좌표측의 데이터 범위가 다를때에는
#데이터 전처리 표준점수로 구해주어야 한다.

#train_scaled-> 표준점수 나온 훈련데이터
#kneighborsclassfier 학습기에다가 학습시켜서
#nebores() 제일가까운 좌표 5개를 구한뒤 5개 데이터를 그래프에다가 시각화를 합니다.


#plt.show()
#print(distances)
#print(indexes)

