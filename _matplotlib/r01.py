import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 가운데 동그라미 점 하나
fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_subplot()
ax.set(xlim=(-1, 1), ylim=(-1, 1), xticks=[], yticks=[])

circle = ax.scatter(0, 0, s=10, lw=1, ec="b", fc="none")


# marker 크기 변경 함수
def update(frame_number):
    circle.set_sizes([frame_number*30])

# marker 크기
update(10)

plt.show()