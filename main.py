import json
import os

# [1] 퀴즈 하나하나의 정보를 담는 '설계도'입니다.
class Quiz:
    def __init__(self, movie_title, question, choices, answer):
        self.movie_title = movie_title  # 영화 제목
        self.question = question        # 문제 내용
        self.choices = choices          # 4개의 선택지 (리스트)
        self.answer = answer            # 정답 번호 (1, 2, 3, 4 중 하나)

# [2] 게임 전체를 관리하는 '관리자'입니다.
class QuizGame:
    def __init__(self):
        self.quizzes = []        # 퀴즈 목록을 담을 바구니
        self.best_score = 0      # 최고 점수
        self.file_path = "state.json" # 데이터를 저장할 파일 이름
        self.load_data()         # 시작하자마자 기존 데이터를 불러옵니다.

    def load_data(self):
        """저장된 데이터를 불러오는 기능"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.best_score = data.get("best_score", 0)
                    # 저장된 딕셔너리 데이터를 다시 Quiz 객체로 바꿉니다.
                    self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
            except:
                self.set_default_quizzes()
        else:
            self.set_default_quizzes()

    def set_default_quizzes(self):
        """민지님이 만든 10개의 퀴즈 데이터를 기본값으로 설정합니다."""
        self.quizzes = [
            Quiz("겨울왕국", "눈사람의 이름은?", ["올라프", "스벤", "크리스토프", "한스"], 1),
            Quiz("어벤져스", "아이언맨의 본명은?", ["브루스 배너", "스티브 로저스", "토니 스타크", "토르"], 3),
            Quiz("기생충", "기생충의 감독 이름은?", ["박찬욱", "봉준호", "이창동", "홍상수"], 2),
            Quiz("알라딘", "램프 요정의 이름은?", ["자파", "이아고", "아부", "지니"], 4),
            Quiz("타이타닉", "여주인공의 이름은?", ["로즈", "엘사", "나탈리", "엠마"], 1),
            Quiz("아이언맨", "주인공 '토니 스타크'가 직접 만든 슈트의 이름은?", ["자비스", "울트론", "마크", "헐크버스터"], 3),
            Quiz("겨울왕국", "안나의 언니이자 얼음 마법을 쓰는 주인공은?", ["엘사", "안나", "올라프", "이두나"], 1),
            Quiz("기생충", "'너는 계획이 다 있구나'라는 명대사가 나온 영화는?", ["괴물", "마더", "설국열차", "기생충"], 4),
            Quiz("어벤져스", "타노스가 사용한 장갑의 이름은?", ["인피니티 건틀렛", "나노 건틀렛", "파워 건틀렛", "아이언 건틀렛"], 1),
            Quiz("해리포터", "해리의 이마에 있는 흉터 모양은?", ["별", "달", "번개", "구름"], 3)
        ]

    def save_data(self):
        """현재 상태(퀴즈, 점수)를 파일에 저장하는 기능"""
        data = {
            "best_score": self.best_score,
            "quizzes": [q.__dict__ for q in self.quizzes]
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        """[메뉴 1] 퀴즈를 푸는 기능"""
        print("\n🚀 퀴즈를 시작합니다!")
        score = 0
        
        for i, q in enumerate(self.quizzes, 1):
            print(f"\n[{i}번 문제] 영화: {q.movie_title}")
            print(f"질문: {q.question}")
            
            # 보기 출력
            for idx, choice in enumerate(q.choices, 1):
                print(f"{idx}. {choice}")
            
            # 입력 받기 (민지님이 강조하신 공백 제거 포함!)
            user_input = input("정답 번호를 입력하세요: ").strip()
            
            if user_input.isdigit() and int(user_input) == q.answer:
                print("정답입니다! 🎉")
                score += 10
            else:
                print(f"아쉽네요. 정답은 {q.answer}번입니다. 😢")
        
        print(f"\n✅ 모든 문제를 풀었습니다! 당신의 점수는 {score}점입니다.")
        
        # 최고 점수 갱신 확인
        if score > self.best_score:
            print(f"🎊 축하합니다! 최고 점수 경신! ({self.best_score} -> {score})")
            self.best_score = score
            self.save_data()

    def show_list(self):
        """[메뉴 3] 퀴즈 목록을 보여주는 기능"""
        print(f"\n📋 현재 등록된 퀴즈 (총 {len(self.quizzes)}개)")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. [{q.movie_title}] {q.question}")

    def run(self):
        """게임의 메인 메뉴를 실행하는 기능"""
        while True:
            print("\n" + "="*40)
            print("        🎬 영화 퀴즈 게임 🎬")
            print("="*40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가 (준비 중)")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("="*40)
            
            choice = input("선택: ").strip()

            if choice == '1':
                self.play_quiz()
            elif choice == '2':
                print("\n(아직 개발 중인 기능입니다. 조금만 기다려주세요!)")
            elif choice == '3':
                self.show_list()
            elif choice == '4':
                print(f"\n🏆 현재 최고 점수: {self.best_score}점")
            elif choice == '5':
                print("게임을 종료합니다. 다음에 또 만나요! 👋")
                break
            else:
                print("⚠️ 1번부터 5번 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    # 1. 게임 객체 생성
    game = QuizGame()
    
    # 2. 게임 시작 (메뉴 호출)
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n게임을 종료합니다. 다음에 또 만나요! 👋")
    