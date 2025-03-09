# #oops 1
# class details():
#     user_name = 'mohanachari'
#     id = 123456
#     dept = 'python'
#     def user_info(self ):
#         print(f"the user name is {self.user_name}")
#     def user_info2(self):
#         print(f"the user id is {self.id} and department is {self.dept}")
# obj = details()
# obj.user_info()
# obj.user_info2()
# print(obj.id)
# obj2 = details()
# obj.user_info()

# #oops 2
# class mobile():
#     bn = 'apple'
#     ROM = '256gb'
#     colour = 'white'
#     def calling(self):
#         print(f"i calling in phone of {self.bn}")
#     def browsing(self):
#         print(f"browsing in {self.bn}")
#     def capturing(self):
#         print(f"capturing photo in {self.bn} it's storage is {self.ROM}")
# phone = mobile()
# phone.calling()
# phone.browsing()
# phone.capturing()
# phone1 = mobile()
# phone1.browsing()
# phone1.calling()
# phone1.capturing()

#oops using init method
class car():
    def __init__(self , bn , colour , model , version):
        self.bn = bn
        self.colour = colour
        self.model = model
        self.version = version
    def driving(self):
        print(f"your are driving in {self.bn} and it's colour is {self.colour}")
    def engine(self):
        print(f"the engine is v6 the version is {self.version}")
    def braking(self):
        print(f"the car model is {self.model}")
bmw = car('bmw','white',2025,'GDS12345' )
bmw.driving()
bmw.engine()
bmw.braking()
print("--"*20)
tata = car('tata','black', 2023,'fgd123234')
tata.driving()
tata.engine()
tata.braking()

