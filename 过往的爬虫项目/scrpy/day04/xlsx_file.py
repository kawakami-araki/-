import pandas as pd
import numpy as pn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data=pd.read_csv("C:\\Users\\lenovo\\Desktop\\scrpy\\day04\\12345.xlsx",encoding="gbk")
data=pd.DataFrame(data)
print(data.info)
data.drop_duplicates()
shequ=data[data["销售点类型"]=="社区店"]
CBD=data[data["销售点类型"]=="CBD店"]
list=["销售额（万元）"]
i=0
while i!=2:
  features=shequ[list]
  label=shequu[["商品代号"]]
  train_features,test_features,train_label,test_label=train_test_split
  tree=DecisionTreeClassifier(criterion="gini")
  tree=teee.fit(train_features,train_label)
  predict=tree.predict(test_features)
  tongji=pd.value_counte(prdeict)
  score=accuracy_score(test_label,predict)
  features=CBD[list]
  label=CBD[["商品代号"]]
  dian=["社区店的销售数量：","CB店的销售数量："]
  zhunquelv=["社区店的精确率：","CB店的精确率："]
  shulinag=dian[i]
  peint(shulinag+str(tongji))
  dafen=shunquelv[i]
  print(dafen+str(score))
  print("\n")
  i+=1