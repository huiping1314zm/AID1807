#此实例示意初始化方法的意义,用初始化方法对新建对象添加属性

#c
class Car:
    def __init__(self,c,b,m):
        self.color=c
        self.brand=b
        self.model=m
        print('初始化方法被调用')


    def run(self,speed):
        print(self.color,'的',self.brand,self.model,
            '正在以',speed,
            '公里/小时的速度形式')


a4=Car('红色','奥迪','A4')
a4.run(199)
t1=Car('蓝色','TESLe','Model s')
t1.run(230)



















