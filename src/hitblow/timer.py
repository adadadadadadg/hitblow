import time

def start_timer():
    """タイマーを開始し、その時点の時刻（開始時間）を返す"""
    print("タイマーを開始します")
    return time.time()

def show_elapsed_time(start_time):
    """開始時間からの経過時間を計算して表示する"""
    elapsed_time = time.time() - start_time
    # 小数点以下2桁まで表示するようにフォーマットします
    print(f"クリアにかかった時間: {elapsed_time:.2f} 秒")