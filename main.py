def main():
    print("あなたは目を覚ますと、暗い部屋に閉じ込められていました。")
    print("扉には奇妙な模様が刻まれています。")
    print("何をしますか？")
    
    while True:
        action = input("選択肢: [調べる, 開ける, 待つ] > ").strip()
        
        if action == "調べる":
            print("模様の中に小さな文字が隠れていることに気づきました。")
            print("「正しい言葉を言えば、扉は開く」と書かれている。")
            if solve_puzzle():
                success_ending()
                break
        elif action == "開ける":
            print("扉を力任せに開けようとしましたが、びくともしません。")
        elif action == "待つ":
            print("あなたは何もせず待ち続けましたが、救いは訪れませんでした。")
            bad_ending()
            break
        else:
            print("無効な選択肢です。もう一度試してください。")


def solve_puzzle():
    print("扉に向かって何か言葉を話します。")
    while True:
        word = input("何を言いますか？ > ").strip()
        if word == "脱出":
            print("扉が音を立てて開き始めました！")
            return True
        elif word == "助けて":
            print("扉は反応しません。")
        else:
            print("何も起こりません。")
            retry = input("もう一度試しますか？ [はい/いいえ] > ").strip()
            if retry == "いいえ":
                return False


def success_ending():
    print("あなたは無事に脱出しました！おめでとうございます！")
    print("=== 脱出成功エンド ===")


def bad_ending():
    print("暗闇の中、あなたは永遠に閉じ込められました…")
    print("=== 閉じ込めエンド ===")


if __name__ == "__main__":
    main()

