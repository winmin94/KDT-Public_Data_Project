import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib


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

# -----------------------------------------------------------------------------------------------------

file2 = './2데이터산업의_데이터직무별_인력_현황.csv'
data2DF = pd.read_csv(file2)
mydata2DF = data2DF.iloc[:, [0, 5, 13, 21, 29, 37, 45, 53]]
#print(mydata2DF)

mydata2DF.columns = ['데이터직무별', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
#print(mydata2DF)
# 8개 직무별 인력 비율
mydata2_arcList = []
mydata2_devList = []
mydata2_engList = []
mydata2_anaList = []
mydata2_manList = []
mydata2_sciList = []
mydata2_conList = []
mydata2_plaList = []
mydata2_Totallist=[mydata2_arcList,mydata2_devList,mydata2_engList,mydata2_anaList,
           mydata2_manList,mydata2_sciList,mydata2_conList,mydata2_plaList]


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

#print(mydata2_conList)

mydata2_yearlist = []
mydata2_yearlist.append(mydata2DF.columns[1:].astype('int32'))


print(mydata2_yearlist)

plt.figure(figsize=(14,9))

num = 3
for i in range(2):
    for j in range(4):
        plt.subplot2grid((2, 4), (i, j))
        plt.plot(list(range(1,8)), mydata2_Totallist[num-3], color = "#8E24AA", label=mydata2DF.iloc[num,0])
        plt.xlabel("연(년)", loc='right')
        plt.ylabel("%", loc = 'top', rotation = 180)
        plt.xticks(list(range(1, 8)), *list(mydata2_yearlist), rotation=70)
        plt.legend()
        num = num + 1


# plt.subplot2grid((2, 4), (0, 1))
# plt.plot(list(range(1,8)), mydata2_arcList, color = "#40897B", label="데이터 아키텍트")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (0, 2))
# plt.plot(list(range(1,8)), mydata2_engList, color = "#40897B", label="데이터 엔지니어")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (0, 3))
# plt.plot(list(range(1,8)), mydata2_anaList, color = "#40897B", label="데이터 분석가")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (1, 0))
# plt.plot(list(range(1,8)), mydata2_manList, color = "#40897B", label="데이터베이스관리자")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (1, 1))
# plt.plot(list(range(1,8)), mydata2_sciList, color = "#40897B", label="데이터 과학자")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (1, 2))
# plt.plot(list(range(1,8)), mydata2_conList, color = "#40897B", label="데이터 컨설턴트")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()
# plt.subplot2grid((2, 4), (1, 3))
# plt.plot(list(range(1,8)), mydata2_plaList, color = "#40897B", label="데이터 기획자")
# plt.xticks(list(range(1,8)), *list(mydata2_yearlist), rotation=70)
# plt.xlabel("연(년)", loc='right')
# plt.ylabel("퍼센트(%)")
# plt.legend()

plt.suptitle("데이터산업의 데이터직무별 인력 현황", size=30)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------------------------------------
file3 = './3전_산업_내_데이터직무별_인력현황.csv'
data3DF = pd.read_csv(file3)
mydata3DF = data3DF.iloc[:, [0, 2, 8, 14, 20, 26, 32, 38]]
mydata3DF.columns = ['데이터직무별', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
# print(mydata3DF)

mydata3_arcList = []
mydata3_devList = []
mydata3_engList = []
mydata3_anaList = []
mydata3_manList = []
mydata3_sciList = []
mydata3_conList = []
mydata3_plaList = []
mydata3_Totallist=[mydata3_arcList,mydata3_devList,mydata3_engList,mydata3_anaList,
           mydata3_manList,mydata3_sciList,mydata3_conList,mydata3_plaList]

for i in range(1,8):
    mydata3_arcList.append(float(mydata3DF.iloc[3, i]))
for i in range(1,8):
    mydata3_devList.append(float(mydata3DF.iloc[4, i]))
for i in range(1,8):
    mydata3_engList.append(float(mydata3DF.iloc[5, i]))
for i in range(1,8):
    mydata3_anaList.append(float(mydata3DF.iloc[6, i]))
for i in range(1,8):
    mydata3_manList.append(float(mydata3DF.iloc[7, i]))
for i in range(1,8):
    mydata3_sciList.append(float(mydata3DF.iloc[8, i]))
for i in range(1,8):
    mydata3_conList.append(float(mydata3DF.iloc[9, i]))
for i in range(1,8):
    mydata3_plaList.append(float(mydata3DF.iloc[10, i]))

mydata3_yearlist = []
mydata3_yearlist.append(mydata3DF.columns[1:].astype('int32'))
# print(mydata3_yearlist)

plt.figure(figsize=(14,9))

num = 3
for i in range(2):
    for j in range(4):
        plt.subplot2grid((2, 4), (i, j))
        plt.plot(list(range(1,8)), mydata3_Totallist[num-3], color = "violet", label=mydata3DF.iloc[num,0])
        plt.xlabel("연(년)", loc='right')
        plt.ylabel("%", loc = 'top', rotation = 180)
        plt.xticks(list(range(1, 8)), *list(mydata3_yearlist), rotation=70)
        plt.legend()
        num = num + 1

plt.suptitle("전 산업의 데이터직무별 인력 현황", size=30)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------------------

file8 = './8향후_5년_내_데이터산업의_데이터직무_인력_부족률.csv'
data8DF = pd.read_csv(file8)
mydata8DF = data8DF.iloc[:, [0, 1, 6, 11, 15, 19, 23, 27]]
mydata8DF.columns = ['데이터직무별', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
print(mydata8DF)

mydata8_arcList = []
mydata8_devList = []
mydata8_engList = []
mydata8_anaList = []
mydata8_manList = []
mydata8_sciList = []
mydata8_conList = []
mydata8_plaList = []
mydata8_Totallist=[mydata8_arcList,mydata8_devList,mydata8_engList,mydata8_anaList,
           mydata8_manList,mydata8_sciList,mydata8_conList,mydata8_plaList]

for i in range(1,8):
    mydata8_arcList.append(float(mydata8DF.iloc[2, i]))
for i in range(1,8):
    mydata8_devList.append(float(mydata8DF.iloc[3, i]))
for i in range(1,8):
    mydata8_engList.append(float(mydata8DF.iloc[4, i]))
for i in range(1,8):
    mydata8_anaList.append(float(mydata8DF.iloc[5, i]))
for i in range(1,8):
    mydata8_manList.append(float(mydata8DF.iloc[6, i]))
for i in range(1,8):
    mydata8_sciList.append(float(mydata8DF.iloc[7, i]))
for i in range(1,8):
    mydata8_conList.append(float(mydata8DF.iloc[8, i]))
for i in range(1,8):
    mydata8_plaList.append(float(mydata8DF.iloc[9, i]))

print(mydata8_arcList)

mydata8_yearlist = []
mydata8_yearlist.append(mydata8DF.columns[1:].astype('int32'))

plt.figure(figsize=(14,9))

num = 2
for i in range(2):
    for j in range(4):
        plt.subplot2grid((2, 4), (i, j))
        plt.plot(list(range(1,8)), mydata8_Totallist[num-3], color = "#40897B", label=mydata8DF.iloc[num,0])
        plt.xlabel("연(년)", loc='right')
        plt.ylabel("%", loc = 'top', rotation = 180)
        plt.xticks(list(range(1, 8)), *list(mydata8_yearlist), rotation=70)
        plt.ylim(0, 37)
        plt.legend()
        num = num + 1

plt.suptitle("향후 5년 내 데이터산업의 데이터직무 인력 부족률", size=30)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------------------

file7 = './7향후_5년_내_전_산업의_데이터직무별_인력_부족률.csv'
data7DF = pd.read_csv(file7)
mydata7DF = data7DF.iloc[:, [0, 1, 4, 7, 10, 13, 16, 19]]
mydata7DF.columns = ['데이터직무별', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
print(mydata7DF)

mydata7_arcList = []
mydata7_devList = []
mydata7_engList = []
mydata7_anaList = []
mydata7_manList = []
mydata7_sciList = []
mydata7_conList = []
mydata7_plaList = []
mydata7_Totallist=[mydata7_arcList,mydata7_devList,mydata7_engList,mydata7_anaList,
           mydata7_manList,mydata7_sciList,mydata7_conList,mydata7_plaList]

for i in range(1,8):
    mydata7_arcList.append(float(mydata7DF.iloc[2, i]))
for i in range(1,8):
    mydata7_devList.append(float(mydata7DF.iloc[3, i]))
for i in range(1,8):
    mydata7_engList.append(float(mydata7DF.iloc[4, i]))
for i in range(1,8):
    mydata7_anaList.append(float(mydata7DF.iloc[5, i]))
for i in range(1,8):
    mydata7_manList.append(float(mydata7DF.iloc[6, i]))
for i in range(1,8):
    mydata7_sciList.append(float(mydata7DF.iloc[7, i]))
for i in range(1,8):
    mydata7_conList.append(float(mydata7DF.iloc[8, i]))
for i in range(1,8):
    mydata7_plaList.append(float(mydata7DF.iloc[9, i]))

print(mydata7_arcList)

mydata7_yearlist = []
mydata7_yearlist.append(mydata7DF.columns[1:].astype('int32'))

plt.figure(figsize=(14,9))

num = 2
for i in range(2):
    for j in range(4):
        plt.subplot2grid((2, 4), (i, j))
        plt.plot(list(range(1,8)), mydata7_Totallist[num-3], color = "#2196F3", label=mydata7DF.iloc[num,0])
        plt.xlabel("연(년)", loc='right')
        plt.ylabel("%", loc = 'top', rotation = 180)
        plt.xticks(list(range(1, 8)), *list(mydata7_yearlist), rotation=70)
        plt.ylim(0, 37)
        plt.legend()
        num = num + 1

plt.suptitle("향후 5년 내 전 산업의 데이터직무 인력 부족률", size=30)
plt.tight_layout()
plt.show()