import json
import os
import shutil
import sys

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

class QuizGame:
    def __init__(self):
        self.file_path = 'state.json'
        self.quizzes = []
        self.best_score = 0
        self.default_data = [
            {"question": "봉준호 감독의 황금종려상 수상작은?", "choices": ["기생충", "괴물", "마더", "설국열차"], "answer": 1},
            {"question": "디즈니 '겨울왕국'의 주인공 이름은?", "choices": ["벨", "모아나", "엘사", "자스민"], "answer": 3},
            {"question": "아이언맨이 속한 히어로 팀의 이름은?", "choices": ["저스티스 리그", "어벤져스", "엑스맨", "판타스틱4"], "answer": 2},
            {"question": "영화 '인셉션'의 감독은?", "choices": ["스필버그", "놀란", "카메론", "셔말란"], "answer": 2},
            {"question": "해리포터의 기숙사 이름은?", "choices": ["슬리데린", "후플푸프", "래번클로", "그리핀도르"], "answer": 4}
        ]
        self.load_data()

    def load_data(self):
        # 1. 메인 파일이 없는 경우
        if not os.path.exists(self.file_path):
            # 백업 파일이라도 있는지 확인
            backup_path = self.file_path + ".bak"
            if os.path.exists(backup_path):
                print("메인 데이터가 없어 백업 파일에서 복구합니다.")
                shutil.copy(backup_path, self.file_path) # 백업으로 복구
            else:
                self.reset_to_default("데이터 파일이 없어 초기화합니다.")
                return

        # 2. 데이터 로드 시도
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data.get("quizzes", [])]
        except (json.JSONDecodeError, KeyError):
            # 3. 파일이 깨졌을 경우 백업 파일로 2차 시도
            backup_path = self.file_path + ".bak"
            if os.path.exists(backup_path):
                print("데이터가 손상되어 백업 파일로 복구를 시도합니다.")
                # 여기서 백업 파일을 다시 로드하는 로직을 넣거나, 
                # 사용자에게 알림을 주고 백업 파일을 메인으로 교체할 수 있습니다.
                self.recover_from_backup(backup_path)
            else:
                self.reset_to_default("데이터 파일 손상 및 백업 없음으로 초기화합니다.")

    def recover_from_backup(self, backup_path):
        """백업 파일로부터 데이터를 복구하는 보조 함수"""
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data.get("quizzes", [])]
                # 복구 성공 후 메인 파일로 다시 저장
                self.save_data()
                print("백업 파일로부터 성공적으로 복구되었습니다.")
        except:
            self.reset_to_default("백업 파일마저 손상되어 초기화합니다.")

    def reset_to_default(self, message):
        print(f"\n💡 {message}")
        self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in self.default_data]
        self.best_score = 0
        self.save_data()

    def save_data(self):
        # 1. 기존 파일이 있다면 안전하게 .bak 파일로 백업 먼저 수행
        if os.path.exists(self.file_path):
            shutil.copy(self.file_path, self.file_path + ".bak")
        
        # 2. 데이터 저장
        data = {"best_score": self.best_score, "quizzes": [q.to_dict() for q in self.quizzes]}
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_game(self):
        if not self.quizzes:
            print("\n❌ 풀 수 있는 문제가 없습니다."); return

        current_score = 0
        total_possible = len(self.quizzes) * 10 # 총점 계산 (문제수 * 10)
        
        print("\n--- 🎮 퀴즈 시작! (문제당 10점) ---")
        for i, q in enumerate(self.quizzes, 1):
            print(f"\nQ{i}. {q.question}")
            for idx, choice in enumerate(q.choices, 1):
                print(f"  {idx}) {choice}")
            
            while True:
                ans = input("정답 번호: ").strip()
                if ans in ['1', '2', '3', '4']:
                    if int(ans) == q.answer:
                        print("✅ 정답입니다! (+10점)")
                        current_score += 10 # 10점씩 추가
                    else:
                        print(f"❌ 틀렸습니다. (정답: {q.answer}번)")
                    break
                print("⚠️ 1~4 사이의 숫자를 입력해주세요.")

        print(f"\n🏁 게임 종료!")
        print(f"최종 점수: {current_score}점 / {total_possible}점")
        
        if current_score > self.best_score:
            print(f"🔥 축하합니다! 최고 기록 경신! ({current_score}점)")
            self.best_score = current_score
            self.save_data()
        else:
            print(f"현재 최고 기록은 {self.best_score}점입니다.")

    def show_best_score(self):
        print("\n--- 🏆 최고 점수 확인 ---")
        if self.best_score == 0:
            print("아직 기록이 없습니다. 첫 게임을 시작해보세요!")
        else:
            print(f"현재 최고 기록은 {self.best_score}점입니다.")

    def add_quiz(self):
        print("\n--- ➕ 새 퀴즈 추가 ---")
        q_text = input("문제: ").strip()
        if not q_text: return
        choices = [input(f"선택지 {i}: ").strip() for i in range(1, 5)]
        while True:
            ans = input("정답 번호(1-4): ").strip()
            if ans in ['1', '2', '3', '4']:
                self.quizzes.append(Quiz(q_text, choices, int(ans)))
                self.save_data()
                print("✨ 추가 완료!"); break
            print("⚠️ 1~4 사이만 입력하세요.")

    def show_quizzes(self):
        print("\n--- 📜 퀴즈 목록 ---")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

    def run(self):
        while True:
            print(f"\n=== 🎬 영화 퀴즈 게임 ===")
            print("1. 게임 시작")
            print("2. 퀴즈 추가")
            print("3. 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("========================")
            choice = input("선택: ").strip()
            
            if choice == '1': self.play_game()
            elif choice == '2': self.add_quiz()
            elif choice == '3': self.show_quizzes()
            elif choice == '4': self.show_best_score()
            elif choice == '5': print("안녕히 가세요! 👋"); break
            else: print("⚠️ 올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    try:
        QuizGame().run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램을 안전하게 종료합니다.")
        sys.exit(0)