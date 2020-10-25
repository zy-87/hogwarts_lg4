# -*- coding: utf-8 -*-
# @Time     : 2020/10/26 0:15
# @Author   : zhaoyang
# @File     : task_2.py
import random


class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    @staticmethod
    def see_people(name):
        if name == '无崖子':
            print('师弟!!!!我就知道你爱的是我!!!!!')
        elif name == '李秋水':
            print("贱人, 师弟是我的!")
        elif name == '丁春秋':
            print("叛徒 ! 我杀了你 !")
        else:
            print("八荒六合, 唯我独尊!!")

    @staticmethod
    def fight_zms(obj, enemy_hp, enemy_power):
        my_power = obj.power * 10
        my_hp = obj.hp / 2

        while True:
            my_hp = my_hp - enemy_power
            enemy_hp = enemy_hp - my_power
            # 判断血量是否小于0,小于零后跳出循环
            if my_hp <= 0:
                print("你这是什么功夫,好厉害!")
                break
            elif enemy_hp <= 0:
                print("太菜了, 要不要姥姥教你两招!")
                break


class XuZhu(TongLao):
    def read(self):
        print("阿弥陀佛, 罪过罪过!")


if __name__ == '__main__':
    # 随机生成敌人的血量和攻击力
    enemy_hp = random.randint(800, 1000)
    enemy_power = random.randint(500, 5000)
    # 自定义要实例化的对象和对象的血量和攻击力
    while True:
        choice = input("请选择要实例化的对象  1.天山童姥  2.虚竹\n")
        if choice=='1':
            hp = input("请输入天山童姥的血量>>>")
            # 判断输入的是否是纯数字
            hp = int(hp) if hp.isdigit() else print("请输入数字")
            power = input("请输入天山童姥的攻击力>>>")
            power = int(power) if power.isdigit() else print("请输入数字")
            # hp和power都有值的时候跳出循环
            if hp and power:
                obj = TongLao(hp, power)
                break
        elif choice=='2':
            hp = input("请输入虚竹的血量>>>")
            # 判断输入的是否是纯数字
            hp = int(hp) if hp.isdigit() else print("请输入数字")
            power = input("请输入虚竹的攻击力>>>")
            power = int(power) if power.isdigit() else print("请输入数字")
            # hp和power都有值的时候跳出循环
            if hp and power:
                obj = XuZhu(hp, power)
                break
        else:
            print("请输入正确的选择编号")
    # 最后的实例化对象只有两种
    if type(obj) is TongLao:
        names = ['无崖子', '李秋水', '丁春秋', '其他']
        name = names[random.randint(0,len(names))]
        obj.see_people(name)
        obj.fight_zms(obj, enemy_hp, enemy_power)
    else:
        obj.read()
