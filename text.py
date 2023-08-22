import random

def game():
    number = random.randint(1, 100)
    attempts = 0
    best_attempt = float("inf")
    
    while True:
        user_input = input("1~100 사이의 숫자를 맞추어보세요: ")
        
        if not user_input.isdigit():
            print("숫자를 입력해주세요.")
            continue
        
        user_input = int(user_input)
        
        if user_input < 1 or user_input > 100:
            print("1~100 사이의 숫자를 입력해주세요.")
            continue
        
        attempts += 1
        
        if user_input < number:
            print("Up")
            
        elif user_input > number:
            print("Down")
        else:
            print(f"축하합니다~ {attempts}번 만에 숫자를 맞추었습니다.")
            if attempts < best_attempt:
                best_attempt = attempts
                print(f"최고 시도 횟수: {best_attempt}번")
            break

def main():
    print("숫자 맞추기 게임을 시작합니다.")
    
    while True:
        game()
        
        restart = input("게임을 다시 시작하겠습니까? (Y, N): ")
        if restart.lower() != "y":
            print("게임을 종료합니다.")
            break
        
if __name__ == "__main__":
    main()