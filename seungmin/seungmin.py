import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

'''
file1 = './1데이터산업_인력_현황.csv'
basicDF = pd.read_csv(file1)
#basicDF = basicDF.loc[1:3]
basicDF.drop(axis = 0, index = [0], inplace = True)
basicDF.reset_index(drop = True, inplace = True)        # drop = True를 주면 컬럼으로 안 밀어내고 삭제
print(basicDF)
#print(basicDF.dtypes)
#basicDF_year_list = []
basicDF_data_list = []
basicDF_nondata_list = []
basicDF_per_list = []
for k in range(7):
    basicDF_data_list.append(basicDF.iloc[0, 1+k])
    basicDF_nondata_list.append(basicDF.iloc[1, 1+k])
    basicDF_per_list.append(round((basicDF_data_list[k] / (basicDF_data_list[k] + basicDF_nondata_list[k]) * 100),1))
print(basicDF_per_list)

#fig, axes = plt.subplots(2, 4, figsize=(14,8))
plt.figure(figsize=(14,8))
plt.suptitle("데이터산업 인력 현황비", fontsize='50')
idx = 0
for i in range(0,2):

    for j in range(0,4):
        print(idx, i, j)
        plt.subplot2grid((2, 4), (i, j))
        if idx == 7:
            plt.title("추이")
            plt.bar(range(7),list(map(float,basicDF_per_list)), color = 'skyblue')
            plt.xlabel("년도")
            plt.ylabel("%", rotation = 180, loc='top')
            plt.xticks(range(7),[k for k in range(2016,2023)])
            #plt.yticks([a for a in range(10,101,10)],['10','20','30','40','50','60','70','80','90','100'])
            break
        plt.pie([int(basicDF_data_list[idx]), int(basicDF_nondata_list[idx])], startangle=90, autopct='%.1f%%', labels = ['데이터직무', '데이터직무 외'])
        plt.title(basicDF.columns[idx+1])
        idx += 1

plt.tight_layout()
plt.show()
# axes[i, j].pie([int(basicDF_data_list[idx]), int(basicDF_nondata_list[idx])], startangle=90, autopct='%.1f%%', labels = ['데이터직무', '데이터직무 외'])
# axes[i, j].set_title(basicDF.columns[idx+1])
# idx += 1
# if idx == 7:
#     axes[i, j+1].title("추이")
#     axes[i, j+1].bar([k for k in range(2016,2023)],list(map(float,basicDF_per_list)))
#     break
'''
file2 = './2데이터산업의_데이터직무별_인력_현황.csv'
data2DF = pd.read_csv(file2)
mydata2DF = data2DF.iloc[:, [0, 5, 13, 21, 29, 37, 45, 53]]
#print(mydata2DF)

mydata2DF.columns = ['데이터직무별', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
print(mydata2DF)
# 8개 직무별 인력 비율
mydata2_arcList = []
mydata2_devList = []
mydata2_engList = []
mydata2_anaList = []
mydata2_manList = []
mydata2_sciList = []
mydata2_conList = []
mydata2_plaList = []


for i in range(1,8):
    mydata2_arcList.append(float(mydata2DF.iloc[3, i]))
for i in range(1,8):
    mydata2_devList.append(float(mydata2DF.iloc[4, i]))
for i in range(1,8):
    mydata2_engList.append(float(mydata2DF.iloc[5, i]))
for i in range(1,8):
    mydata2_anaList.append(float(mydata2DF.iloc[6, i]))
for i in range(1,8):
    mydata2_manList.append(float(mydata2DF.iloc[7, i]))
for i in range(1,8):
    mydata2_sciList.append(float(mydata2DF.iloc[8, i]))
for i in range(1,8):
    mydata2_conList.append(float(mydata2DF.iloc[9, i]))
for i in range(1,8):
    mydata2_plaList.append(float(mydata2DF.iloc[10, i]))

print(mydata2_conList)

mydata2_yearlist = []
mydata2_yearlist.append(mydata2DF.columns[1:].astype('int32'))


print(mydata2_yearlist)
a=[1,2,3,4,5,6,7]

plt.bar(a, mydata2_arcList)
plt.show()