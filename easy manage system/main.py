#1、显示功能界面
def menu():
    print("请选择功能"+'*'*12)
    print("1、增")
    print("2、删")
    print("3、改")
    print("4、查")
    print("5、显示列表")
    print("6、退出")
    print("*" * 20)

#2、用户输入学号
def Selections():
    user_input = int(input("请选择:")) #input函数默认输入为字符类型 强制转换为int()型
    judge(user_input)
#3.根据用户的输入 调用对应的函数
def judge(user_input):
    if user_input == 1:
        print(1)
    elif user_input == 2:
        print(2)
    elif user_input == 3:
        print(3)
    elif user_input == 4:
        print(4)
    elif user_input == 5:
        print(5)
    elif user_input == 6:
        print(6)
    else:
        print('输入错误')

#程序运行
isflag = True
while isflag:
    menu()
    Selections()