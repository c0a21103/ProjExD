import random


def shutudai():
    que = random.choice(qa_lst)
    print(f'問題：{que["q"]}')
    return que["a"]

def kaitou(ans_lst):
    ans = input("解答：")
    if ans in ans_lst:
        print("正解！")
    else:
        print("不正解...")
    
    

if __name__ == "__main__":
    qa_lst = [{"q":"サザエの旦那の名前は？","a":["ますお","マスオ"]},
              {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
              {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}]
    ans_lst = shutudai()
    kaitou(ans_lst)