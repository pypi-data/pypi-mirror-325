from bmob import Bmob,BmobQuery

b = Bmob('','')
user = b.login('admin','123456')
print(user.objectId)

islogin = b.checkSession('826e2c8f9a')
if islogin is None:
    print(b.getError())
else:
    print(islogin)