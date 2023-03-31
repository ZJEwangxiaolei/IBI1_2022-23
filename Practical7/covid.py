import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/wangxiaolei/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:1100:100,0:2]
my_columns = [False, True,True, False, False, False]
covid_data.iloc[0:82,my_columns]
covid_data.loc[covid_data.iloc[:,1]=="Afghanistan"]["total_cases"]
new_data = covid_data.loc[covid_data.iloc[:,0]=="2020-03-31",["new_cases","new_deaths"]]
print(new_data.mean())
plt.boxplot(new_data)
plt.show()
world_dates = covid_data.loc[covid_data.iloc[:,1]=="World"]["date"]
world_new_cases =covid_data.loc[covid_data.iloc[:,1]=="World"]["new_cases"]
world_new_deaths=covid_data.loc[covid_data.iloc[:,1]=="World"]["new_deaths"]
plt.plot(world_dates, world_new_cases, 'ro')
plt.plot(world_dates, world_new_deaths, 'bo')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
#How have new cases and total cases developed over time in the UK
UK_dates=covid_data.loc[covid_data.iloc[:,1]=="United Kingdom"]["date"]
UK_new_cases=covid_data.loc[covid_data.iloc[:,1]=="United Kingdom"]["new_cases"]
UK_total_cases=covid_data.loc[covid_data.iloc[:,1]=="United Kingdom"]['total_cases']
plt.plot(UK_dates,UK_new_cases,"r+")
plt.plot(UK_dates,UK_total_cases,"b+")
plt.xticks(world_dates.iloc[0:len(UK_dates):4],rotation=-90)
plt.show()