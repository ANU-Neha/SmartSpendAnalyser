
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Total Bill per Day")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Total Bill per Day")
plt.show()

