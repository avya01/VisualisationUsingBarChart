import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Birth_Rate" : [10, 12, 16, 9, 7]
}

df_July = pd.DataFrame(data)

data2 = {
    "Day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Birth_Rate" : [5, 18, 4, 7, 9]
}

df_August = pd.DataFrame(data2)

plt.bar(df_July.Day, df_July.Birth_Rate, width=0.5, color="lightblue")
plt.bar(df_August.Day, df_August.Birth_Rate, width=0.5, color="blue")
plt.xlabel("Day")
plt.ylabel("Birth Rate")
plt.title("Birth Rate VS Day for both months")
plt.show()