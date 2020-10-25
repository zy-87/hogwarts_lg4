# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 23:41
# @Author   : zhaoyang
# @File     : task_1.py


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}会吃")

    def sleep(self):
        print(f"{self.name}会睡")


class Mao(Animal):
    def play_ball(self):
        print(f"{self.name}会玩毛线球")


class Gou(Animal):
    def eat(self):
        print(f"{self.name}会啃骨头")


class Lang(Animal):
    def baiyue(self):
        print(f"{self.name}会饿狼拜月")


class Tu(Animal):
    def wadong(self):
        print(f"{self.name}会狡兔三窟")


class Xiong(Animal):
    def sleep(self):
        print(f"{self.name}会冬眠")


mao = Mao('小猫11')
mao.eat()
mao.sleep()
mao.play_ball()

gou = Gou('小狗旺财')
gou.eat()
gou.sleep()

lang = Lang('灰太狼')
lang.eat()
lang.sleep()
lang.baiyue()

tu = Tu('玉兔精')
tu.eat()
tu.sleep()
tu.wadong()

xiong = Xiong('熊二')
xiong.eat()
xiong.sleep()
