import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=[
  [2,3,4,0],
  [3,2,4,5],
  [4,5,2,1],
  [4,3,5,2]
]
 
df=pd.DataFrame(data)
sns.heatmap(df,annot=True,cmap="coolwarm")
plt.title("heatmap of player")
plt.show()