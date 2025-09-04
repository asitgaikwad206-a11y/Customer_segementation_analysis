#customer segmentation in banks
import pandas as pd
import numpy as np
df=pd.read_csv("bank_transactions_real.csv.csv")
df.head(5)
df.info()
#checking for nulls
if (df.isnull().sum().sum())==0:
  print("No nulls")
else:
    print("nulls found")

df.isnull().sum()
#nulls found

#checking for duplicates
if (df.duplicated().sum())==0:
  print("No duplicates")
else:
    print("duplicates found")
#no duplicates found
#dealing with nulls
df.dropna(inplace=True)
df.isnull().sum()

#EDA
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#loading the data
df=pd.read_csv("bank_transactions_real.csv.csv")

# Select only numerical columns for correlation calculation
numerical_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,6))
sns.heatmap(numerical_df.corr(),annot=True)
plt.show()

sns.countplot(x='CustGender',data=df,palette='Set2')
plt.show()


df.columns
ax=sns.countplot(x='CustLocation',data=df)
for bars in ax.containers:
  ax.bar_label=(bars)
  plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='CustGender', y='CustAccountBalance', data=df)
plt.title("Customer Account Balance vs Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Account Balance (INR)")
plt.show()

#basic eda

df.head()
df.describe()
df['CustLocation'].mode() #most city with customers-mumbai

df['CustAccountBalance'].mean() #avg account balance=115403.54005

top_city=df.groupby(['CustLocation'],as_index=False)['CustAccountBalance'].sum().sort_values(by='CustAccountBalance',ascending=False).head()
top_city
#top 5 states with most account balance
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x="CustLocation",y="CustAccountBalance",data=top_city)
from datetime import datetime

df=pd.read_csv("bank_transactions_real.csv.csv")
# Convert DOB to datetime (day/month/year format)
df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'], format='%d/%m/%y', errors='coerce')
df

# Today's date
today = pd.Timestamp.today()

# Calculate age in years
df['Age'] = df['CustomerDOB'].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))
df

bins = [0, 25, 35, 50, 65, 100]
labels = ['<25', '25-35', '35-50', '50-65', '65+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
df.dropna(subset=['AgeGroup'])

#most transactions for a group
df['AgeGroup'].value_counts()
df

#recent tranbsactions , freq of transactions , avg transactions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import MiniBatchKMeans

# 🔹 Fix negative ages
df['Age'] = df['Age'].apply(lambda x: np.nan if x < 0 else x)

# 🔹 Drop rows with missing/incorrect Age
df = df.dropna(subset=['Age'])
#categorical to numerical data
df['CustLocation'] = LabelEncoder().fit_transform(df['CustLocation'])
df['CustGender'] = LabelEncoder().fit_transform(df['CustGender'])

#features
X = df[['Age', 'CustGender', 'CustLocation',
        'CustAccountBalance', 'TransactionAmount (INR)']].dropna()

#scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Elbow Method 
# Use at most 10,000 rows for elbow (faster)
sample_size = min(10000, len(X_scaled))
X_sample = X_scaled[:sample_size]

wcss = []
for i in range(1, 11):
    kmeans = MiniBatchKMeans(n_clusters=i, random_state=42, batch_size=1000, n_init=10)
    kmeans.fit(X_sample)
    wcss.append(kmeans.inertia_)

sns.set()
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.title('Elbow Method with Sampling - Optimal k')
plt.show()

#
optimal_k = 4  
kmeans = MiniBatchKMeans(n_clusters=optimal_k, random_state=42, batch_size=1000, n_init=10)

# Assign cluster labels back to the original DataFrame using the index of X
df.loc[X.index, 'Cluster'] = kmeans.fit_predict(X_scaled)


print("Cluster Centers (scaled values):")
print(kmeans.cluster_centers_)

# Cluster profiling
cluster_profile = df.groupby('Cluster')[['Age','CustAccountBalance','TransactionAmount (INR)']].mean()
print("\nCluster Profiles:")
print(cluster_profile)

import seaborn as sns
import matplotlib.pyplot as plt

# Plot Age vs TransactionAmount
plt.figure(figsize=(8,6))
sns.scatterplot(x=df['Age'], y=df['TransactionAmount (INR)'], hue=df['Cluster'], palette="Set1")
plt.title("Clusters by Age vs Transaction Amount")
plt.xlabel("Age")
plt.ylabel("Transaction Amount (INR)")
plt.show()

# Plot Age vs CustAccountBalance
plt.figure(figsize=(8,6))
sns.scatterplot(x=df['Age'], y=df['CustAccountBalance'], hue=df['Cluster'], palette="Set2")
plt.title("Clusters by Age vs Account Balance")
plt.xlabel("Age")
plt.ylabel("Account Balance (INR)")
plt.show()

