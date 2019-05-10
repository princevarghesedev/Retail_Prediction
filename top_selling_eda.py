import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns


df1 = pd.read_csv('C:\\Users\\Prince\\Downloads\\cproducts.csv')
df = pd.DataFrame(df1)
df['transactionDate'] = pd.to_datetime(df['transactionDate'])

cols=['customerID','DOB','store_code','PinCode','store_description',
      'till_no','transaction_number_by_till','promotion_description']
df.drop(cols,axis=1,inplace=True)
df=df.sort_values('transactionDate')

# x=df[df['product_description'][['transactionDate'] == '2016-01-01':'2016-12-31']].sum()
# print(x)

# df['transactionDate'] = pd.date_range('2015-06-01', periods=200, freq='D')
df = df.set_index(['transactionDate'])
start='2016-01-01'
end='2016-12-31'
df=df.loc[start:end]

pro_grp=df.groupby('transactionDate')['product_description'].sum()
# df=df.set_index('transactionDate')
x = df['product_description'].value_counts()
p_count= x.iloc[[2,5,6,7,8,9,11,12,13,14],]
# xaxis_name= p_count.unique()
print(p_count)
y_pos = np.arange(len(p_count))
p_bar = plt.barh(y_pos,p_count, align='center', alpha=0.5)
# sns.countplot(y=p_count,alpha=0.5,data=p_count)
plt.yticks(y_pos,p_count.keys(),fontsize=7,weight='light')
# plt.xticks(np.arange(1,39,2))
plt.xlabel('count for {} to {}'.format(start,end))
plt.title('Item')
plt.show()