#coding=utf-8
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from models import *
from hashlib import *
from hashlib import sha1
from django.http import JsonResponse


# Create your views here.
#用户注册页面展示

def register(request):
    return render(request,'test1/register.html')


#注册用户是否已经存在
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

#用户注册数据处理

def register_handle(request):
    post=request.POST
    if post.get('user_name')!=None and post.get('pwd')!=None and post.get('cpwd')!=None :
        upwd1=post.get('pwd')
        uname=post.get('user_name')
        upwd2=post.get('cpwd')
        uemail=post.get('email')
        if upwd1 != upwd2:
            return redirect('/user/register/')
    #密码加密
        s1=sha1()
        s1.update(upwd1)
        upwd3=s1.hexdigest()

        user=UserInfo()
        user.uname=uname
        user.upwd=upwd3
        user.uemail=uemail
        user.save()

        return redirect('/user/login/')
    else:
        return redirect('/user/register/')





#用户登陆页面展示

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登陆','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'test1/login.html',context)

#登陆数据处理

def login_handle(request):
    post=request.POST
    uname=post.get('username')


    count=UserInfo.objects.filter(uname=uname)
    #return HttpResponse(count[0].uname)
    if count!=None:
        upwd = post.get('pwd')
        jizhu=post.get('jizhu',0)
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest() == count[0].upwd :
            red=HttpResponseRedirect('/index/index')
            #是否记住该用户，创建COOKIES
            if jizhu !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=count[0].id
            request.session['user_name']=count[0].uname
            count1 = UserInfo.objects.filter(uname=uname).count()
            #object 不能直接放到json格式里
            request.session['count']=count1
            return red

            #return redirect('/user/info')
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname}
            return render(request, 'test1/login.html', context)

    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname}
        return render(request, 'test1/login.html', context)






