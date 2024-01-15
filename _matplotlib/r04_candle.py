import pandas as pd


# import yfinance as yf
# df = yf.desload("AAPL", start="2024-01-01", end="2024-1-10", interval='5m', progress=False)
# df.index = pd.to_datetime(df.index)
# df.index = df.index.tz_localize(None)

# df.to_excel('AAPL.xlsx')


data = pd.read_excel('AAPL.xlsx',index_col=0)
data.index.name = 'DT'
data = data.drop(columns=['Adj Close'])
data.columns = ['O','H','L','C','V']



idx = data.index
data = data.loc[(idx >= '2024-01-02')&(idx <= '2024-01-05')]

data = data.assign(X=range(len(data)))
# data.notna()
print(data)
inc = data[data.C >= data.O] 
des = data[data.C < data.O] 

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5), constrained_layout=True)
ax = fig.add_subplot()
w_body = 0.9
w_tail = 0.2


ax.bar(inc.X, inc.C-inc.O, w_body, bottom=inc.O, color='green') 
ax.bar(inc.X, inc.H-inc.L, w_tail, bottom=inc.L, color='green') 
# ax.bar(inc.X, inc.H-inc.C, w_tail, bottom=inc.C, color='green') 
# ax.bar(inc.X, inc.L-inc.O, w_tail, bottom=inc.O, color='green') 

ax.bar(des.X, des.C-des.O, w_body, bottom=des.O, color='red')
ax.bar(des.X, des.H-des.L, w_tail, bottom=des.L, color='red')
# ax.bar(des.X, des.H-des.O, w_tail, bottom=des.O, color='red')
# ax.bar(des.X, des.L-des.C, w_tail, bottom=des.C, color='red')


# data.index
def format_date(x, _):
    try:
        # convert datetime64 to datetime, and use datetime's strftime:
        return data.index[round(x)].strftime('%H:%M')
    except IndexError:
        pass

ax.xaxis.set_major_formatter(format_date)


plt.show()

