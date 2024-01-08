
# ---------------------------------- partial --------------------------------- #
from functools import partial

def myfunc(x):
    return x * 2

# partial을 사용하여 x=1로 고정
fixed_x_func = partial(myfunc, 1)

# 함수 호출
print(fixed_x_func())  # 결과: 2


# ---------------------------------- lambda ---------------------------------- #
def myfunc(x):
    return x * 2

# lambda를 사용하여 x=1로 고정
fixed_x_func = lambda: myfunc(1)

# 함수 호출
print(fixed_x_func())  # 결과: 2