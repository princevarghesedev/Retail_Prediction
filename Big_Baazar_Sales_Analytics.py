import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

# columns=['customerID','DOB','Gender','transactionDate','store_code','store_description','till_no','transaction_number_by_till','promo_code'
#          ,'promotion_description','product_code','product_description','sale_price_after_promo']
report=pd.read_csv("E:\\Project-Predective Analysis of Retail sales\\Projectdata.csv",parse_dates=True,date_parser='transactionDate')
# # print(report.head())
df=pd.DataFrame(report)
# print(df.head())
# bbdata=df.loc[:,['customerID','Gender','product_description','sale_price_after_promo']] #.loc function[rows,columns]
# print(bbdata.head())

# print("************* For Individual Product *******************")
# print(df[df.product_description=='BRITANNIA CAKE CHOCOLATE 50g'])
# print("***************************************************")
# print(df.loc[df.product_description=='BRITANNIA CAKE CHOCOLATE 50g',:])

# print("************** 1st Group By **********************")
# df1=df.groupby(['sale_price_after_promo']).count()['product_description'].sort_values(ascending=False)
# print(df1.head())
# plt.pie(df1,startangle=90)
# plt.show()

# df2=df.groupby(['sale_price_after_promo','product_description']).count()
# print("************** 2nd Group By *********************")
# df2=df.groupby('sale_price_after_promo')
# print("group by output")
# print(df2.head())

# print("************** 3rd Group By for Ist sale analytics based on state*********************")
# state=df.groupby('State')
# for name,group in state:
#     print("State Name : ",name)
#     print("State Group : ")
# print(group)
# import numpy as np
# print("**************************************")
# print(state['sale_price_after_promo'].sum())
# print("state : ",state.head(5))
# print("*********************")
# print(state.head(5))
# state_sum=state['sale_price_after_promo'].sum()
# print(state_sum)
'''state wise sale '''
print('****************total sum based on state************')
def state():
    statewise_sale=df.groupby('State')['sale_price_after_promo'].sum()
    print(statewise_sale)
    return statewise_sale
state()

'''city wise sale'''
print('************city wise sale*************')
def city():
    city=df.groupby('store_description')
    for x in city:
        String=str(x).split('-')[1]
        citysale=city['sale_price_after_promo'].sum()

    print(citysale)
    return citysale
city()
'''plotting for state wise sale'''
statename=['Jharkhand','Karnataka','Madhya Pradesh','Punjab','Tamil Nadu']
x=np.arange(len(statename))
plt.bar(x,state(),align='center')
plt.xticks(x,statename) #to rotate the names use rotation=90
plt.ylabel('sales')
# plt.show()

'''plotting for city wise sale '''
cityname=['Amritsar','Hubli','Indore-Malhar','Indore-Treasure','Jamshedpur','Ludhiana','Madurai']
X=np.arange(len(cityname))
plt.figure(figsize=(10,10))
plt.bar(X,city(),align='center',color='g')
plt.xticks(X,cityname,fontsize=8) #here rotation 90 is used to make the lsbels in a vertical.
plt.ylabel('sales')
# plt.show()
#
'''on the basis of date and time'''
df['transactionDate']=pd.to_datetime(df['transactionDate'])
# print(df['transactionDate'])
td=df.groupby('transactionDate')['sale_price_after_promo'].sum().reset_index()
report=td.set_index('transactionDate')
print(report.head(5),'for 2015')
# print(df['transactionDate'].dtypes)
print(report.index)
print(report.loc['2016-04-08'],'aaaaaaaaaaaaaaass')
start='2015-01-01'
end='2015-12-31'
df=report.loc[start:end]
df.plot(figsize=(10,10))
plt.show()

'''adding columns with year, month and weekdays'''
report['Year']=report.index.year
report['Month'] =report.index.month
report['Day']=report.index.weekday_name
print(report.sample(5)) #report.sample is used to sample out

'''plotting graph for sales per month'''
# x=report['Year']
y=report['sale_price_after_promo'].resample('MS').mean()# resample is used to recreate the column as ms
y1=y['2016-1-1':'2016-12-1']
y1.plot(figsize=(10,10))
print(y1,'this is for 2016')
plt.ylabel('sales for 2016')
# plt.show()
print('this is report',report)

'''plotting  graph for sales on basis of year'''
yearly=(report.groupby('Year')['sale_price_after_promo'].sum())
print('this is yearly sales',yearly)
# yearly.plot(figsize=(10,10))
# plt.ylabel('sales yearly')
# plt.show()

'''plotting graph for sales according to weekdays'''
days={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
# days=df.apply(lambda x: x==days)
# print(df.loc[df[]].sort_values())

'''sorting weekdays in a ordered way'''
week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
report['Day']=pd.(report['Day'],categories=week,ordered=True) #categorical function orders in the proper way for weekdays.
print(report)
report=report.sort_values('Day')
weekdays=report.groupby(['Year','Day'])['sale_price_after_promo'].mean()
print(weekdays,'this is weekdays')
# print(report.loc[report['Day']=='SUNDAY',:])

weekdays.plot(figsize=(10,10))
plt.figlegend(weekdays.Day)
plt.ylabel('Daily Sales')
plt.show()

