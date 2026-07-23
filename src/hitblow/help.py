import random

# スキル使用回数の上限
MAX_SKILL_COUNT = 3


def get_safe_digit(secret):
    """secretに含まれていない数字を1つランダムに選んで返す"""
    all_digits = set("0123456789")
    secret_digits = set(secret)

    # secretで使われていない数字
    available_digits = list(all_digits - secret_digits)

    return random.choice(available_digits)


def show_skill_info():
    """スキルの説明を表示"""
    print("skill : sを押すと使用されていない数字を知ることができます。(3回まで使用可能)")


def use_skill(secret, skill_count):
    """
    スキルを使用する

    Parameters
    ----------
    secret : str
        正解の数字
    skill_count : int
        現在の使用回数

    Returns
    -------
    tuple
        (更新後の使用回数, ヒント数字)
    """

    if skill_count >= MAX_SKILL_COUNT:
        print("スキルは3回までしか使用できません。")
        return skill_count, None

    safe_digit = get_safe_digit(secret)
    skill_count += 1

    print(f"ヒント: {safe_digit} は答えに含まれていません。")
    print(f"スキル使用回数: {skill_count}/{MAX_SKILL_COUNT}")

    return skill_count, safe_digit
