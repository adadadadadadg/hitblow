def select_digits():
    """ユーザーに3桁か4桁かを選択させ、その数値を返す"""
    while True:
        choice = input("桁数を選択してください (3 または 4) > ").strip()
        if choice in ["3", "4"]:
            digits = int(choice)
            print(f"\nそれでは、{digits} 桁でゲームをスタートします！\n")
            return digits
        print("3 か 4 の数字を入力してください。")