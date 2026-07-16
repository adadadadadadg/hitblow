import random

def get_safe_digit(secret):
    """secretに含まれていない数字を1つランダムに選んで返す"""
    # 0〜9のすべての数字から、secretで使われている数字を除外（引き算）する
    all_digits = set("0123456789")
    secret_digits = set(secret)
    
    # 残った「ハズレの数字」のリストを作る
    available_digits = list(all_digits - secret_digits)
    
    # その中からランダムに1つ選んで返す
    return random.choice(available_digits)