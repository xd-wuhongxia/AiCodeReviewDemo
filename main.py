import os


def main():
    print("Hello, World!")
    


# 用python 写一个逻辑，随机生成一个小的 数字解迷游戏，适合小朋友玩
def generate_number_puzzle():
    """
    随机生成一个适合小朋友玩的数字解谜游戏。
    游戏规则：给出一个1-20之间的随机数字，玩家有5次机会猜测这个数字，每次猜测后会提示大了还是小了。
    """
    import random

    answer = random.randint(1, 20)
    max_attempts = 5
    print("欢迎来到数字解谜游戏！")
    print("我已经选择了1到20之间的一个数字，你有5次机会来猜它。")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"第{attempt}次猜测，请输入你的数字："))
        except ValueError:
            print("请输入有效的数字！")
            continue

        if guess == answer:
            print(f"恭喜你，猜对了！答案就是{answer}！")
            break
        elif guess < answer:
            print("你猜的数字小了。")
        else:
            print("你猜的数字大了。")
    else:
        print(f"很遗憾，机会用完了。正确答案是{answer}。")



def run_game():
    generate_number_puzzle()


if __name__ == "__main__":
    main()