import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time 


from matplotlib.animation import ArtistAnimation

fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_subplot()


# Axes 주변부 요소 삭제
ax.set(xlim=(-1, 1), ylim=(-1, 1), xticks=[], yticks=[])


circles = []
for i_frame in range(120):
    # scatter marker 생성
    
    circle = ax.scatter(0, 0, s=10, lw=3, ec="b", fc="none")
    circle.set_sizes([i_frame*500])  
    circles.append([circle])

# animation 객체 생성
anim = ArtistAnimation(fig, circles, interval=5)

# animation을 gif로 저장
plt.show()

