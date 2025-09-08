import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Customer-Churn.csv',encoding='UTF-8')
# print(df.head)
# print(df.info())

# replacing blanks with 0 as tenure is 0 no total charges are recorded
df['TotalCharges']=df['TotalCharges'].replace(' ','0')
df['TotalCharges']=df['TotalCharges'].astype('float')
# print(df.info())

# checking the null values
print(df.isnull().sum())
print(df.describe)
print(df.duplicated().sum())
print(df['customerid'].duplicated().sum())

# changing the value of senior citizens 1 with yes and 0 with no
def convert(value):
    if value==1:
        return 'yes'
    else:
        return 'no'
df['SeniorCitizen']=df['SeniorCitizen'].apply(convert)
print(df['SeniorCitizen'])
# print(df.head(20))

plt.figure(figsize=(4,4))
ax=sns.countplot(x='Churn',data=df,color='salmon')
ax.bar_label(ax.containers[0])
plt.title('Count of customers by Churn')
plt.show()

# from the given pie chart we can conclude that 26.54% of our customers have churned out.
plt.figure(figsize=(3,4))
gb=df.groupby('Churn').agg({'Churn':'count'})
plt.pie(gb['Churn'],labels=gb.index,autopct='%1.2f%%',colors=['skyblue','salmon'])
plt.title('Percentage of Churned Customers')
plt.show()

# churn by gender
plt.figure(figsize=(3,3))
sns.countplot(x='gender',data=df,hue='Churn')
plt.title('Churn by Gender')
plt.show()

# churn by senior citizens

# Step 1: Group and calculate percentages
grouped = df.groupby(['SeniorCitizen', 'Churn']).size().unstack(fill_value=0)
percentages = grouped.div(grouped.sum(axis=1), axis=0) * 100

# Step 2: Plot stacked bar chart with percentages
fig, ax = plt.subplots(figsize=(6,6))
bars = percentages.plot(kind='bar', stacked=True, ax=ax, color=['skyblue', 'salmon'])

# Step 3: Add percentage labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Step 4: Final touches
plt.title('Churn Percentage by Senior Citizen')
plt.xlabel('Senior Citizen')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.legend(title='Churn')
plt.tight_layout()
plt.show()

# people who have used our services for a long time have stayed and people who have used our services 1 or 2 months have churned
plt.figure(figsize=(9,4))
sns.histplot(x='tenure',data=df,bins=72,hue='Churn')
plt.show()


# people who have month to month contract are likely to churn then from those who have 1 or 2 years or contract.
plt.figure(figsize=(3,3))
sns.countplot(x='Contract',data=df,hue='Churn')
plt.title('Count of customer by contract')
plt.show()

print(df.columns)

import matplotlib.pyplot as plt
import seaborn as sns

cols = ['PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies']

# Smaller figure size and tighter spacing
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(11, 8))
axes = axes.flatten()

for i, col in enumerate(cols):
    ax = axes[i]
    sns.countplot(data=df, x=col, ax=ax, palette='Set2')
    ax.set_title(f'{col}', fontsize=10)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(axis='x', labelsize=8)
    for container in ax.containers:
        ax.bar_label(container, fontsize=8)

plt.tight_layout(pad=1.0)
plt.suptitle('Service Usage Overview', fontsize=14, y=1.02)
plt.show()

# Churned customers by payment method
# customer 
plt.figure(figsize=(6,4))
ax=sns.countplot(x='PaymentMethod',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title('Churned Customers By payment method')
plt.show()