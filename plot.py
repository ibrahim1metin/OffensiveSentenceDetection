from matplotlib import pyplot as plt
import pandas as pd
from utils import sortDictByValues
data=pd.read_csv("labeled_data.csv")
plotData=data[["hate_speech","offensive_language","neither"]]
sums={}
sums["hateSum"]=0
sums["offensiveSum"]=0
sums["neitherSum"]=0
for i,j,k in zip(plotData["hate_speech"],plotData["offensive_language"],plotData["neither"]):
    sums["hateSum"]+=i
    sums["offensiveSum"]+=j
    sums["neitherSum"]+=k
counts=dict()
counts["hateCount"]=0
counts["offensiveCount"]=0
counts["neitherCount"]=0
for i,j,k in zip(plotData["hate_speech"],plotData["offensive_language"],plotData["neither"]):
    counts["hateCount"]+=(1 if i!=0 else 0)
    counts["offensiveCount"]+=(1 if j!=0 else 0)
    counts["neitherCount"]+=(1 if k!=0 else 0)
nulls={}
nulls["hateNulls"]=0
nulls["offensiveNulls"]=0
nulls["neitherNulls"]=0
for i,j,k in zip(plotData["hate_speech"],plotData["offensive_language"],plotData["neither"]):
    nulls["hateNulls"]+=(0 if i!=0 else 1)
    nulls["offensiveNulls"]+=(0 if j!=0 else 1)
    nulls["neitherNulls"]+=(0 if k!=0 else 1)
sums=sortDictByValues(sums)
counts=sortDictByValues(counts)
nulls=sortDictByValues(nulls)
print(nulls)
print(counts)
print(sums)
meanSums=sum(sums.values())/len(sums.values())
meanNulls=sum(nulls.values())/len(nulls.values())
meanCounts=sum(counts.values())/len(counts.values())
fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(15,5))
ax1.set_title("Sums")
ax1.set_xlabel('categories')
ax1.set_ylabel('Corresponding sums')
ax1.bar((sums.keys()),(sums.values()),color ='maroon',width = 0.4)
for i in range(len(sums.values())):
    ax1.text(i,list(sums.values())[i]//2,list(sums.values())[i],ha="center")
ax1.axhline(meanSums, color='red', linestyle='--')
ax1.text(0., meanSums+3000, f'Mean: {meanSums:.2f}', color='red', ha='left', va='center')

ax2.set_title("Nulls")
ax2.set_xlabel('categories')
ax2.set_ylabel('Corresponding nulls')
ax2.bar((nulls.keys()),(nulls.values()),color ='maroon',width = 0.4)
for i in range(len(nulls.values())):
    ax2.text(i,list(nulls.values())[i]//2,list(sums.values())[i],ha="center")
ax2.axhline(meanNulls, color='red', linestyle='--')
ax2.text(0., meanNulls+3000, f'Mean: {meanSums:.2f}', color='red', ha='left', va='center')

ax3.set_title("Counts")
ax3.set_xlabel('categories')
ax3.set_ylabel('Corresponding counts')
ax3.bar((counts.keys()),(counts.values()),color ='maroon',width = 0.4)
for i in range(len(counts.values())):
    ax3.text(i,list(counts.values())[i]//2,list(counts.values())[i],ha="center")
ax3.axhline(meanNulls, color='red', linestyle='--')
ax3.text(0., meanNulls+3000, f'Mean: {meanSums:.2f}', color='red', ha='left', va='center')

plt.show()