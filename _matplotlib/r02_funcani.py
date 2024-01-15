import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time 


from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_subplot()


# Axes 주변부 요소 삭제
ax.set(xlim=(-1, 1), ylim=(-1, 1), xticks=[], yticks=[])

# scatter marker 생성
circle = ax.scatter(0, 0, s=10, lw=3, ec="b", fc="none")

# animation frame마다 적용되는 변화
start_time = time.time()
def update(frame_number):
    # size 변경
    global start_time
    circle.set_sizes([frame_number*500])                    
    current_time = time.time()
    fps = 1.0 / (current_time - start_time)
    start_time = current_time
    ax.set_title(f"FPS_{fps:.2f}")
# animation 객체 생성
anim = FuncAnimation(fig, update, frames=120, interval=1)

# animation을 gif로 저장
plt.show()

