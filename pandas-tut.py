import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('survey.csv')
df = pd.DataFrame(data)
print(f"Head of the DataFrame: \n{df.head()}")
print(f"Tail of the DataFrame: \n{df.tail()}")

df['pie'].value_counts().plot(kind = 'bar', color = '#FFFFFF', edgecolor = 'black')
plt.title("most popular thanksgiving pies!!!!!!")
plt.xlabel("PIE TYPE")
plt.ylabel("# OF RESPONSES")
plt.tight_layout()
plt.xticks(rotation=45)
df.info()
plt.show()