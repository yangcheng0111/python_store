import random


class Character:
    def __init__(self, name,dodge):
        # 血量
        self.hp = 100
        # 名称
        self.name = name
        # 攻击
        self.atk = 10

        #闪避
        self.dodge = self.getRandomList(dodge)



    def getRandomList(self,dodge):
        randomList=[]
        while True:
            if len(randomList)==dodge:
                return randomList
            num=random.randint(1, 101)
            if num in randomList:
                continue
            else:
                randomList.append(num)



    def setHp(self, atk):
        if random.randint(1, 101) in self.dodge:
            print(f'{self.name}闪避了攻击,剩余血量{self.hp}')
            return True
        self.hp -= atk
        if self.hp <= 0:
            self.hp=0
        print(f'{self.name}受到攻击，剩余血量{self.hp}')
        if self.hp <= 0:
            print(f'{self.name}死亡')
            return False
        return True

    def getAtk(self):
        atk=0
        if self.name == '敌人':
            atk= self.atk + random.randint(1, 10)
        atk=self.atk + random.randint(1, 5)
        print(f'{self.name}进行攻击,攻击力{atk}')
        return atk



if __name__ == '__main__':
    c1 = Character('玩家',5)
    c2 = Character('敌人',100)
    input('当前有一个敌人,回车攻击')
    while True:
        if not c2.setHp(c1.getAtk()):
            break
        elif not c1.setHp(c2.getAtk()):
            break
        print('*' * 10)
