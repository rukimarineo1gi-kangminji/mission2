# 1. 퀴즈 클래스 설계 (영화 제목 필드를 추가했어요!)
class Quiz:
    def __init__(self, movie_title, question, answer):
        self.movie_title = movie_title  # 영화 제목
        self.question = question        # 문제 내용
        self.answer = answer            # 정답

# 2. 게임 실행부
if __name__ == "__main__":
    # 여러 개의 퀴즈 객체를 리스트([])에 담습니다.
    quiz_list = [
        Quiz("겨울왕국", "눈사람의 이름은?", "올라프"),
        Quiz("어벤져스", "아이언맨의 본명은?", "토니스타크"),
        Quiz("기생충", "기생충의 감독 이름은?", "봉준호"),
        Quiz("알라딘", "램프 요정의 이름은?", "지니"),
        Quiz("타이타닉", "여주인공의 이름은?", "로즈")
    ]

    print("🎬 영화 퀴즈 게임을 시작합니다!")
    print("-" * 30)

    score = 0  # 점수를 저장할 변수

    # 반복문(for)을 사용하여 리스트 안의 문제를 하나씩 꺼냅니다.
    for quiz in quiz_list:
        print(f"[{quiz.movie_title}] 문제: {quiz.question}")
        user_input = input("정답을 입력하세요: ").strip()

        if user_input == quiz.answer:
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"아쉽네요. 정답은 '{quiz.answer}'입니다. 😢")
        print("-" * 30)

    # 모든 문제가 끝난 후 최종 점수 발표
    print(f"게임 종료! 당신의 점수는 {score}/{len(quiz_list)}점입니다.")