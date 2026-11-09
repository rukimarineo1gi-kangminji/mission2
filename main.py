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
        self.quizzes = []           # 퀴즈 목록 바구니
        self.best_score = 0         # 최고 점수
        
        # 파일 경로를 두 개로 나눕니다!
        self.quiz_file = "movies.json"   # [읽기 전용] 문제들이 들어있는 곳
        self.state_file = "state.json"   # [쓰기 가능] 내 점수를 저장할 곳
        
        self.load_data()            # 시작하자마자 데이터를 불러옵니다.

    def load_data(self):
        """두 개의 파일에서 각각 문제와 점수를 불러옵니다."""

        # 1. movies.json(문제 파일) 불러오기
        if os.path.exists(self.quiz_file):
            try:
                with open(self.quiz_file, 'r', encoding='utf-8') as f:
                    quiz_data = json.load(f)
                    # 파일에 있는 리스트를 Quiz 객체 리스트로 변환
                    self.quizzes = [Quiz(**q) for q in quiz_data]
            except Exception as e:
                print(f"문제 로딩 중 오류 발생: {e}")
                self.quizzes = []
        else:
            print("movies.json 파일이 없습니다!")

        # 2. state.json(점수 파일) 불러오기
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    state_data = json.load(f)
                    self.best_score = state_data.get("best_score", 0)
            except:
                self.best_score = 0

   
    def save_data(self):
        """최고 점수를 state.json 파일에 저장합니다."""
        # 저장할 데이터 구조 (점수만 저장)
        state_data = {
            "best_score": self.best_score
        }
        # self.file_path 대신 self.state_file을 사용합니다!
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(state_data, f, ensure_ascii=False, indent=4)
        
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

    def add_quiz(self):
        """[메뉴 2] 새로운 퀴즈를 추가하는 기능"""
        print("\n🆕 새로운 퀴즈를 추가합니다.")
        movie_title = input("영화 제목: ").strip()
        question = input("문제 내용: ").strip()
        choices = []
        for i in range(1, 5):
            choices.append(input(f"보기 {i}: ").strip())
        answer = int(input("정답 번호 (1-4): ").strip())

        new_quiz = Quiz(movie_title, question, choices, answer)
        self.quizzes.append(new_quiz)
        
        # 추가된 퀴즈를 movies.json에 저장
        quiz_list = [q.__dict__ for q in self.quizzes]
        with open(self.quiz_file, 'w', encoding='utf-8') as f:
            json.dump(quiz_list, f, ensure_ascii=False, indent=4)
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")
        

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
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("="*40)
            
            choice = input("선택: ").strip()

            if choice == '1':
                self.play_quiz()
            elif choice == '2':
                self.add_quiz()
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
    