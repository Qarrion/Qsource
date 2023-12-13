# lambda arguments: expression

add = lambda x, y: x + y

# 함수 사용
result = add(5, 3)
print(result)  # 출력: 8


# 튜플 리스트 정렬
data = [(2, 'apple'), (1, 'banana'), (4, 'cherry'), (3, 'date')]
sorted_data = sorted(data, key=lambda x: x[0])

print(sorted_data)