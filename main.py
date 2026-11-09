# 1. 퀴즈 하나하나의 정보를 담는 설계도(클래스)입니다.
class Quiz:
    def __init__(self, question, answer):
        self.question = question  # 문제 내용
        self.answer = answer      # 정답

# 2. 퀴즈 객체를 생성해봅니다.
if __name__ == "__main__":
    q1 = Quiz("겨울왕국에서 눈사람의 이름은?", "올라프")
    
    print("--- 영화 퀴즈 게임 ---")
    print(f"문제: {q1.question}")
    
    user_input = input("정답을 입력하세요: ")
    
    if user_input == q1.answer:
        print("정답입니다! 🎉")
    else:
        print(f"아쉽네요. 정답은 {q1.answer}입니다.")