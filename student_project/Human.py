# 一个人（human）类
# class human:
#              def set_info(self,name,age,address='不详'):
#                             '''此方法用来给文件对象添加姓名，年龄，家庭住址属性''''

#                   def show_info(self)
#                         '此处显市此人的信息



# 调用如下：
#       h1=Huamn()
#        h2=human()
#         h1.set_info()#'张’，20，‘北京市东区’
#         h2.set_info()
#          h1.show_info()#‘李’，18
#            h2.show_info()


class Human():
  def set_info(self,name,age,address='不详'):
    self.name=name
    self.age=age
    self.address=address

#                             '''此方法用来给文件对象添加姓名，年龄，家庭住址属性''''

    def show_info(self):
      print(self.name,'今年',self.age,'家听数值',self.address)




h1=Human()
h2=human()
h1.set_info()#'张’，20，‘北京市东区’
h2.set_info()
h1.show_info()#‘李’，18
h2.show_inf






















