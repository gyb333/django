from django.shortcuts import render
from django.shortcuts import redirect
from time import *
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
from . import models
from . import forms
from django.http import HttpResponse

@ensure_csrf_cookie
def hello(request):

    if request.method=='GET':
        print(request.GET.get("name"))
        #print(request.COOKIES['gyb'])
        print(request.get_signed_cookie('key',salt='加密key'))
    elif request.method=='POST':
        #get_token(request)       #两者选一
        #rotate_token(request)   #此方法每次设置新的cookies
        print(request.POST)
        print(request.POST.get("username"))
        #print(request.POST['pwd'])

    response=HttpResponse(strftime('%Y-%m-%d %H:%M:%S')+'你好：'+"Hello world!")
    #response.set_cookie('gyb','gyb333')
    response.set_signed_cookie('key','key',salt='加密key')

    return response


def index(request):
    pass
    return render(request, 'login/index.html')

def test(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})

def login(request):
    if request.method=="POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/index/")
