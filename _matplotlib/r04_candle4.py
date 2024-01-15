import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load your data
data = pd.read_excel('AAPL.xlsx', index_col=0)
data.index.name = 'DT'
data = data.drop(columns=['Adj Close'])
data.columns = ['O', 'H', 'L', 'C', 'V']

# Filter data
idx = data.index
data = data.loc[(idx >= '2024-01-02') & (idx <= '2024-01-05')]
data = data.assign(X=range(len(data)))

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 5))
w_body = 0.9
w_tail = 0.2
k = 10

# Function to format date on x-axis
def format_date(x, _):
    try:
        return data.index[round(x)].strftime('%y-%m-%d %H:%M')
    except IndexError:
        pass



# Initialize the bars
# Create empty bar containers
bars_inc_body = ax.bar([], [], w_body, color='green')
bars_inc_tail = ax.bar([], [], w_tail, color='green')
bars_des_body = ax.bar([], [], w_body, color='red')
bars_des_tail = ax.bar([], [], w_tail, color='red')

# Animation update function
def animate(i):
    ax.clear()  # Clear the axis (not optimal for blit but necessary for updating date labels)
    
    f_data = data.iloc[i:i + k]
    inc = f_data[f_data.C >= f_data.O]
    des = f_data[f_data.C < f_data.O]

    ax.set_xlim([i, i + k]) 
    ax.xaxis.set_major_formatter(format_date)
    # Update the data for each bar
    bars_inc_body = ax.bar(inc.X, inc.C - inc.O, w_body, bottom=inc.O, color='green')
    bars_inc_tail = ax.bar(inc.X, inc.H - inc.L, w_tail, bottom=inc.L, color='green')
    bars_des_body = ax.bar(des.X, des.C - des.O, w_body, bottom=des.O, color='red')
    bars_des_tail = ax.bar(des.X, des.H - des.L, w_tail, bottom=des.L, color='red')

    return bars_inc_body + bars_inc_tail + bars_des_body + bars_des_tail

# Creating the animation
ani = FuncAnimation(fig, animate, frames=len(data) - k, interval=200, blit=True, repeat=False)

plt.show()