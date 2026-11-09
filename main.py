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
        Quiz("타이타닉", "여주인공의 이름은?", "로즈"),
        Quiz("아이언맨", "주인공 '토니 스타크'가 직접 만든 슈트의 이름은?", "마크"),
        Quiz("겨울왕국", "안나의 언니이자 얼음 마법을 쓰는 주인공의 이름은?", "엘사"),
        Quiz("기생충", "봉준호 감독의 영화로, '너는 계획이 다 있구나'라는 명대사가 나온 영화는?", "기생충"),
        Quiz("어벤져스", "타노스가 인구 절반을 날리기 위해 사용한 장갑의 이름은?", "인피니티 건틀렛"),
        Quiz("해리포터", "해리의 이마에 있는 흉터 모양은?", "번개")
    ]

    print("🎬 영화 퀴즈 게임을 시작합니다!")
    print("-" * 30)

    score = 0  # 점수를 저장할 변수

    # 반복문(for)을 사용하여 리스트 안의 문제를 하나씩 꺼냅니다.
    for i, quiz in enumerate(quiz_list):
        print(f"\n[{i+1}번 문제] [{quiz.movie_title}] 문제: {quiz.question}")
        user_input = input("정답을 입력하세요: ").strip().lower() # 공백 제거 및 소문자 변환

        # 💡 [수정] 입력값과 정답 모두에서 공백(" ")을 제거하고 비교합니다!
        clean_user_input = user_input.replace(" ", "")
        clean_answer = quiz.answer.lower().replace(" ", "")

        # 정답 비교 로직
        if clean user_input == clean_answer:
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"아쉽네요. 정답은 '{quiz.answer}'입니다. 😢")
        print("-" * 30)

    # 모든 문제가 끝난 후 최종 점수 발표
    print("\n" + "="*40)
    print("🎉 모든 퀴즈가 끝났습니다! 🎉")
    print(f"당신의 최종 점수는 {score} / {len(quiz_list) * 10}점입니다.")

        if score == len(quiz_list) * 10:
            print("와우! 만점입니다! 당신은 진정한 영화 전문가! 🎬")
        elif score >= (len(quiz_list) * 10) / 2:
            print("오~ 제법인데요? 영화를 좋아하시는군요! 👍")
        else:
            print("아쉽네요! 영화를 좀 더 보셔야겠어요! 😊")
            print("="*40)