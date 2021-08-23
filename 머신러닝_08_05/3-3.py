import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()#남파이 라이브러리로 교체
print(perch_full)

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )
train_input,test_input,train_target,test_target\
    = train_test_split(perch_full, perch_weight, random_state=42)

lr=LinearRegression()
lr.fit(train_input,train_target)

train_score=lr.score(train_input,train_target)
test_score = lr.score(test_input,test_target)

print(train_score)
print(test_score)


prevalues=lr.predict([[ 8.4 ,2.11 , 1.41],[10,20,30]])
print(prevalues)

poly = PolynomialFeatures()
poly.fit(train_input)
#print(train_input[0])
print(poly.get_feature_names())
test_poly = poly.transform(test_input)
train_poly = poly.transform(train_input)

lr=LinearRegression()
lr.fit(train_poly,train_target)

train_score=lr.score(train_poly,train_target)
test_score=lr.score(test_poly,test_target)

print("훈련데이터:",train_score)
print(test_score)


poly=PolynomialFeatures(degree=5,include_bias=False)
poly.fit(train_input,train_target)

train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print(poly.get_feature_names())
print(train_poly.shape)

lr=LinearRegression()
lr.fit(train_poly,train_target)

train_score=lr.score(train_poly,train_target)
test_score=lr.score(test_poly,test_target)

print("훈련데이터:",train_score)
print("테스트데이터:",test_score)


