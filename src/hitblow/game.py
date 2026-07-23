"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)


    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .select_digits import select_digits

    digits = select_digits()        # 新しいファイルから関数を呼び出して桁数を取得
    secret = make_secret(digits)   # 新しい桁数で答えを作り直す

    from .timer import start_timer
    start_time = start_timer()

   
   # ★追加①：スキル説明と使用回数
    from .help import show_skill_info
    skill_count = 0
    show_skill_info()
   
    tries = 0
    print(f"Hit & Blow（{digits} 桁・重複なし）")
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue
        if guess == "s":
            from .help import get_safe_digit
            from .help import use_skill
            skill_count, _ = use_skill(secret, skill_count)
            continue
           
        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .timer import show_elapsed_time

            show_elapsed_time(start_time)

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
