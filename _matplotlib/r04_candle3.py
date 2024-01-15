import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# import yfinance as yf
# df = yf.desload("AAPL", start="2024-01-01", end="2024-1-10", interval='5m', progress=False)
# df.index = pd.to_datetime(df.index)
# df.index = df.index.tz_localize(None)

# df.to_excel('AAPL.xlsx')

# Load your data
data = pd.read_excel('AAPL.xlsx', index_col=0)
data.index.name = 'DT'
data = data.drop(columns=['Adj Close'])
data.columns = ['O','H','L','C','V']

# Filter data
idx = data.index
data = data.loc[(idx >= '2024-01-02')&(idx <= '2024-01-05')]
data = data.assign(X=range(len(data)))



# Set up the figure
fig, ax = plt.subplots(figsize=(10, 5))
w_body = 0.9
w_tail = 0.2

# data.iloc[0:10]

def format_date(x, _):
    try:
        return data.index[round(x)].strftime('%y-%m-%d,%H:%M')
    except IndexError:
        pass
# Animation function
k=10
def animate(i):
    ax.clear()

    f_data = data.iloc[i:i+k]
    # Plot only the first 'i' candles
    inc = f_data[f_data.C >= f_data.O] 
    des = f_data[f_data.C < f_data.O] 

    ax.bar(inc.X, inc.C-inc.O, w_body, bottom=inc.O, color='green') 
    ax.bar(inc.X, inc.H-inc.L, w_tail, bottom=inc.L, color='green') 

    ax.bar(des.X, des.C-des.O, w_body, bottom=des.O, color='red')
    ax.bar(des.X, des.H-des.L, w_tail, bottom=des.L, color='red')

    ax.xaxis.set_major_formatter(format_date)

# Function to format date on x-axis


# Creating the animation
ani = FuncAnimation(fig, animate, frames=len(data)-k, interval=200, repeat=False)

plt.show()
