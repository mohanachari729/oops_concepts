# #Abstraction method using heirachical class
# from abc import ABC , abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def taste():
#         pass
#     def color():
#         pass
# class fruit(abstract_demo):
#     def taste(self):
#         print("the fruit is apple taste is sweet")
#     def color(self):
#         print("the color of apple is red")
# class fruit1(abstract_demo):
#     def taste(self):
#         print("the banana fruite taste is sweet")
#     def color(self):
#         print("the banana color is yellow")
# obj = fruit1()
# obj.color()
# obj.taste()
# obj1 = fruit()
# obj.color()
# obj.taste()

# # #Abstraction method 
# from abc import ABC , abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self,_a):
#         pass
# class gf(abstract_demo):
#     def display(self,_a):##using protection
#         print(f"the property is {_a} ")
# class father(gf):
#     def display(self,_a):
#         print(f"the property is {_a}")
# class child(father):
#      def display(self,_a):
#         print(f"the property is {_a}")
# obj = child()
# obj.display('10 hectres land')
# obj2 = father()
# obj2.display('10 hectres land')


 # #Abstraction method 
from abc import ABC , abstractmethod
class abstract_demo(ABC):
    @abstractmethod
    def display(self,_a):
        pass
class father(abstract_demo):
    def display(self,__a):## using private 
        print(f"the property is {__a}")
class child(father):
     def display(self,__a):##using protection
        print(f"the property is {__a}")
obj = father()
obj.display('100cr')
obj1 =  child()
obj.display('empty')






