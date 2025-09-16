# -*- coding: utf-8 -*-

# 구구단 수 입력받기
num = int(input("몇 단? (1-9): "))

# 구구단 출력
print(f"\n=== {num}단 ===")
for i in range(1, 10):
    print(f"{num} × {i} = {num * i}")