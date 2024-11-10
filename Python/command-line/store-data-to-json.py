import sys
import json
import os


class CommandLineTool:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.data_store = self.load_data()
        self.is_running = True

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print("警告: データファイルが壊れています。新しいデータストアを作成します。")
                    return []
        return []

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.data_store, f, ensure_ascii=False, indent=4)

    def display_menu(self):
        print("\n=== コマンドラインツール ===")
        print("1. データを作成")
        print("2. データを表示")
        print("q. 終了")

    def create_data(self):
        name = input("名前を入力してください: ")
        age = input("年齢を入力してください: ")
        if not age.isdigit():
            print("エラー: 年齢は数字でなければなりません。")
            return
        self.data_store.append({"name": name, "age": int(age)})
        self.save_data()
        print(f"データを作成しました: 名前={name}, 年齢={age}")

    def display_data(self):
        if not self.data_store:
            print("データが存在しません。")
            return
        print("\n--- データ一覧 ---")
        for idx, entry in enumerate(self.data_store, start=1):
            print(f"{idx}. 名前: {entry['name']}, 年齢: {entry['age']}")

    def process_choice(self, choice):
        if choice == '1':
            self.create_data()
        elif choice == '2':
            self.display_data()
        elif choice == 'q':
            print("ツールを終了します。")
            self.is_running = False
        else:
            print("無効な選択肢です。もう一度入力してください。")

    def run(self):
        while self.is_running:
            self.display_menu()
            choice = input("選択肢を入力してください: ").strip().lower()
            self.process_choice(choice)


def main():
    tool = CommandLineTool()
    tool.run()


if __name__ == "__main__":
    main()
