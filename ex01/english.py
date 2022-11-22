import random
import datetime

q_chr = 15 
abs_chr = 4
roop = 5

def mondai(en_lst):
    que = random.sample(en_lst,q_chr)
    abs_que = random.sample(que,abs_chr)
    print("対象文字：")
    [print(i,end=" ") for i in que]
    print("\n")
    print("欠損文字(デバッグ用)：")
    [print(x,end=" ") for x in abs_que]
    print("\n")
    print("表示文字：")
    [print(j,end=" ") for j in que if j not in abs_que]
    print("\n")
    
    return abs_que
    
    

def kaitou(abs_que):
    flag = True
    num = input("欠損文字の数は？：")
    try:
        if int(num) != abs_chr:
            print("不正解...もう一度チャレンジしてね\n")
        else:
            print("正解！では、欠損している文字は何でしょうか？")
            for k in range(abs_chr):
                ans = input(f"{k+1}つ目:")
                if ans not in abs_que:
                    print("不正解...もう一度チャレンジしてね\n")
                    flag = False
                    break
                else:
                    continue
    except:
        print("予期しない入力がされました。\n再実行します。\n")
        flag = False
    
    return flag

if __name__ == "__main__":
    st = datetime.datetime.now()
    en_lst = [chr(i) for i in range(65,91)]
    for i in range(roop):
        question = mondai(en_lst)
        flag = kaitou(question)
        if flag == True:
            print("全問正解おめでとう！")
            break
    ed = datetime.datetime.now()
    print(f"実行時間：{(ed-st).seconds}sec")
        