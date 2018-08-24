from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def hello(request):
   if request.method =="GET":
       name =request.GET.get("name")
       if name is None:
           return HttpResponse("请传name")
       else:
           return HttpResponse("hello"+name)

#登录
def login(request):
    return render(request,"index.html")

#登录动作的处理
# 对form定义的action提交的数据进行处理
# http://127.0.0.1:8001/login_actionform/?username=zhuziqi&password=

def login_action(request):
    if request.method=="POST":
        print(request.method+"打印请求方法")
        # username_=request.GET.get("username","")
        #  password_=request.GET.get("password","")
        username_=request.POST.get("username","")
        password_=request.POST.get("password","")
        print(username_)
        print(password_)
        if username_=="" or password_=="":
            return render(request,"index.html",{"error":"用户名或密码为空"})
        user1=auth.authenticate(username=username_,password=password_)
        if username_!="zhuziqi" or password_!="1":
            return render(request,"index.html",{"error":"用户名或密码错误"})
        else:
            #登录成功后，跳转
            response=HttpResponseRedirect("/event_manage/")
            # response.set_cookie("user",username_,3600)
            request.session["user"]=username_
            return response

#发布会管理
def event_manage(request):
    # user_cookie=request.COOKIES.get("user","")
    user_cookie=request.session.get("user","")
    print(user_cookie)
    return render(request,"event_manage.html",{"user":user_cookie})

