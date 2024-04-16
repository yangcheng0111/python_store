import random


class numGame:
    def __init__(self):
        self.num = random.randint(1, 10)
        self.count = 0

    def game(self):
        while True:
            try:
                num = int(input("请输入一个数字："))
                self.count += 1
            except:
                print('输入不是整数')
                continue
            if num == self.num:
                print("恭喜你猜对了,次数为：", self.count)
                break
            elif num > self.num:
                print("猜大了")
            else:
                print("猜小了")


if __name__ == '__main__':
    game = numGame()
    game.game()
