"""
Create command line tools with Python

Operation
input data: username, password, age, language, country
show data: username, password, age, language, country
delete data: username
update data: username, password, age, language, country
show menu: show all commands
"""

import sys


def display_menu():
    print("\n=== コマンドラインツール ===")
    print("1. データを作成")
    print("2. データを表示")
    print("q. 終了")


def create_data(data_store):
    name = input("名前を入力してください: ")
    age = input("年齢を入力してください: ")
    # データのバリデーション（例: 年齢が数字かどうか）
    if not age.isdigit():
        print("エラー: 年齢は数字でなければなりません。")
        return
    data_store.append({"name": name, "age": int(age)})
    print(f"データを作成しました: 名前={name}, 年齢={age}")


def display_data(data_store):
    if not data_store:
        print("データが存在しません。")
        return
    print("\n--- データ一覧 ---")
    for idx, entry in enumerate(data_store, start=1):
        print(f"{idx}. 名前: {entry['name']}, 年齢: {entry['age']}")


def main():
    data_store = []
    while True:
        display_menu()
        choice = input("選択肢を入力してください: ").strip().lower()

        if choice == '1':
            create_data(data_store)
        elif choice == '2':
            display_data(data_store)
        elif choice == 'q':
            print("ツールを終了します。")
            sys.exit(0)
        else:
            print("無効な選択肢です。もう一度入力してください。")


if __name__ == "__main__":
    main()
