# -*- coding: utf-8 -*-

"""
구구단 프로그램
사용자로부터 구구단 수를 입력받아 해당 구구단을 출력합니다.
"""

def print_multiplication_table(num):
    """
    주어진 숫자의 구구단을 출력하는 함수
    
    Args:
        num (int): 구구단을 출력할 숫자
    """
    print(f"\n=== {num}단 ===")
    for i in range(1, 10):
        result = num * i
        print(f"{num} × {i} = {result}")
    print("=" * 15)

def get_valid_number():
    """
    사용자로부터 유효한 숫자를 입력받는 함수
    
    Returns:
        int: 입력받은 구구단 숫자
    """
    while True:
        try:
            num = int(input("몇 단을 출력할까요? (1-9): "))
            if 1 <= num <= 9:
                return num
            else:
                print("1부터 9까지의 숫자를 입력해주세요.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

def main():
    """
    메인 실행 함수
    """
    print("🔢 구구단 프로그램에 오신 것을 환영합니다! 🔢")
    
    while True:
        # 구구단 수 입력받기
        table_num = get_valid_number()
        
        # 구구단 출력
        print_multiplication_table(table_num)
        
        # 계속 실행할지 물어보기
        while True:
            continue_choice = input("\n다른 구구단을 보시겠습니까? (y/n): ").lower().strip()
            if continue_choice in ['y', 'yes', '예', 'ㅇ']:
                break
            elif continue_choice in ['n', 'no', '아니오', 'ㄴ']:
                print("구구단 프로그램을 종료합니다. 안녕히 가세요! 👋")
                return
            else:
                print("'y' 또는 'n'을 입력해주세요.")

if __name__ == "__main__":
    main()