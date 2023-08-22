import random

def get_user_choice():
    user_choice = input("가위, 바위, 보 중에서 선택하세요 : ")
    return user_choice.lower()

def get_ai_choice():
    choices = ["가위", "바위", "보"]
    Ai_choice = random.choice(choices)
    return Ai_choice

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "무승부"
    elif user_choice == "가위":
        return "유저" if ai_choice == "보" else "인공지능"
    elif user_choice == "바위":
        return "유저" if ai_choice == "가위" else "인공지능"
    elif user_choice == "보":
        return "유저" if ai_choice == "바위" else "인공지능"
    
def game():
    user_wins = 0
    ai_wins = 0
    ties = 0
    
    while True:
     user_choice = get_user_choice()
     ai_choice = get_ai_choice()
    
     print(f"유저의 선택 : {user_choice}")
     print(f"인공지능의 선택 : {ai_choice}")
    
     winner = determine_winner(user_choice, ai_choice)
     if winner == "무승부":
        print("무승부 입니다.")
        ties += 1
     else:
        print(f"{winner}가 이겼습니다!")
        if winner == "유저":
            user_wins += 1
        else:
            ai_wins += 1
        play_again = input("게임을 계속하시겠습니까? (yes/no): ")
        if play_again.lower() != "yes":
            break
        
        print("게임 통계: ")
        print(f"유저 승리 횟수: {user_wins}")
        print(f"인공지능 승리 횟수: {ai_wins}")
        print(f"무승부 횟수: {ties}")
        
game()