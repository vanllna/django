from django.shortcuts import render ,redirect ,reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from tools.send_mail_tools import send_mail_code
from django.http import JsonResponse
from orgs.models import *
from operations.models import *
from django.views.generic import View

'''使用类方法完成视图'''
def error_404(request):
    return render(request,'error_404.html')

def error_500(request):
    return render(request,'error_500.html')

class IndexHone(View):
    def get(self,request):
        return render(request,'users/index.html')
    def post(self,request):
        return render(request,'users/index.html')


def Home(request):
    return render(request,'users/index.html')

def register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'users/register.html',{
            'user_register_form':user_register_form
        })
    elif request.method == 'POST':
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            userlist = UserProfile.objects.filter(Q(username = email)|Q(email = email))
            if userlist:
                return HttpResponse('success')
            else:
                a = UserProfile()
                a.username = email
                a.set_password(password)
                a.email = email
                send_mail_code(email,1)
                a.save()
                return redirect(reverse('users:index'))
        else:
            return render(request,'users/register.html',{
                'user_register_form':user_register_form
            })



def userlogin(request):
    if request.method == 'GET':
        return render(request,'users/login.html')
    else:
        user_login_forms = UserLoginForm(request.POST)
        if user_login_forms.is_valid():
            email = user_login_forms.cleaned_data['email']
            password = user_login_forms.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user.is_start:
                login(request.user)
                return redirect(reverse('users:index'))
            else:
                return HttpResponse('请到邮箱里激活账号')
        else:
            return render(request,'users/login.html',{
                'user_login_forms':user_login_forms
            })


def users_active(request,code):
    if code:
        email_ver_list = EmailVerifyCode.objects.filter(code = code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            email = email_ver.email
            user_list = UserProfile.objects.filter(username=email)
            if user_list:
                user = user_list[0]
                user.is_start = True
                user.save()
                return redirect(reverse('users:index'))
            else:
                pass
        else:
            pass
    else:
        pass


def forgetpwd(request):
    if request.method == 'GET':
        forget_pwd = ForgetPwd()
        return render(request,'users/forgetpwd.html',{
            'forget_pwd':forget_pwd
        })
    else :
        user_forget_form = ForgetPwd(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            userlist = UserProfile.objects.filter(email=email)
            # print(userlist.values())  返回的是一个queryset 对象
            if userlist:
                user = userlist[0]
                email = user.email
                send_mail_code(email,2)
                return HttpResponse('please go email update password')
            else:
                return render(request,'users/forgetpwd.html',{
                    'msg':'user not in '
                })

        else:
            return render(request , 'users/forgetpwd.html',{
                'user_forget_form':user_forget_form
            })

def users_reset(request,code):
    if code:
        if request.method == 'GET':
            return render(request,'users/reset.html',{
                'code':code
            })
        else:
            user_reset_form = UserResetForm(request.POST)
            if user_reset_form.is_valid():
                password = user_reset_form.cleaned_data['password']
                password1 = user_reset_form.cleaned_data['password1']
                if password == password1:
                    email_ver_list = EmailVerifyCode.objects.filter(code = code)
                    if email_ver_list:
                        email_ver = email_ver_list[0]
                        email = email_ver.email
                        user_list = UserProfile.objects.filter(email = email)
                        if user_list:
                            user = user_list[0]
                            user.set_password(password)
                            user.save()
                            return redirect(reverse('users:login'))
                        else:
                            pass
                    else:
                        pass
                elif password != password1:
                    return render(request,'users/reset.html',{
                        'msg':'password error',
                        'code':code
                    })
                else:
                    pass

            else:
                return render(request, 'users/reset.html', {
                    'user_reset_form': user_reset_form,
                    'code': code
                })
    else:
        pass




def UserInfo(request):
    user = request.user
    print(user)
    return render(request,'users/userinfo.html')


def UserChangeImageForm(request):
    userchangeimageform = UserChangeImageForm(request.POST,request.FILES,instance=request.user) #instance 对当前用户做修改
    if userchangeimageform.is_valid():
        userchangeimageform.save(commit=True)
        return JsonResponse({
            'status':'ok'
        })
    else:
        return JsonResponse({
            'status':'fail'
        })



def UserChangeInfo(request):
    '''修改用户名与电话'''
    userchangeinfoforms = UserChangeInfoForm(request.POST,instance=request.user)
    if userchangeinfoforms.is_valid():
        userchangeinfoforms.save(commit=True)
        return JsonResponse({
            'status':'ok'
        })
    else:
        return JsonResponse({
            'status':'fail'
        })

def UpdateEmail(request):
    return render(request,'users/updateemail.html')

from datetime import datetime

def EmailCode(request):
    userchangeemail_form = UserChangeEmailForm(request.POST)
    if userchangeemail_form.is_valid():
        email = userchangeemail_form.cleaned_data['email']
        userlist = UserProfile.objects.filter(Q(email=email)|Q(username=email))
        if userlist:
            return JsonResponse({
                'status':'fail',
                'msg':'email exist'
            })
        else:
            '''
            查询邮箱验证码表中有没有发送过验证码 如果有就 60秒后再发送 如果没有就直接发送
            '''
            email_list_ever = EmailVerifyCode.objects.filter(email=email,send_type=3)
            if email_list_ever:
                '''获取当前最新的验证码信息'''
                email_list = email_list_ever.order_by('-add_time')[0]
                if (datetime.now()-email_list.add_time).seconds > 60:
                    '''删除之前的验证码'''
                    email_list_ever.delete()
                    send_mail_code(email,3)
                    return JsonResponse({
                        'status':'ok',
                        'msg':'email send code success'
                    })
                else:
                    return JsonResponse({
                        'status':'fail',
                        'msg':'time error'
                    })
            else:
                send_mail_code(email,3)
                return JsonResponse({
                        'status':'ok',
                        'msg':'email send code success'
                    })

    else:
        return JsonResponse({
            'status':'fail',
            'msg':'email not exist'
        })

def ResetEmail(request):
    resetemail_form = UserResetEmailForm(request.POST)
    if resetemail_form.is_valid():
        email = resetemail_form.cleaned_data['email']
        code = resetemail_form.cleaned_data['code']

        email_list_ver = EmailVerifyCode.objects.filter(email=email,code=code)
        if email_list_ver:
            email_list = email_list_ver[0]
            if (datetime.now() - email_list.add_time).seconds > 160 :
                return JsonResponse({
                    'status':'fail',
                    'msg':'timeout',
                })
            else :
                request.user.email = email
                request.user.username = email
                request.user.save()
                return JsonResponse({
                    'status':'ok',
                    'msg':'reset success'
                })
        else:
            pass

    else:
        pass


def UserCoures(request):
    usercoures = request.user.usercourse_set.all()
    coureslist = [coures.study_course  for coures in usercoures ]
    return render(request,'users/usercoures.html',{
        'coureslist':coureslist
    })


def UserLoveOrg(request):
    '''获取当前用户的收藏机构信息'''
    userloveorg_list = UserLove.objects.filter(love_man=request.user,love_type=1,love_status=True)
    userloveorgid = [ loveorg.love_id for loveorg in userloveorg_list ]

    orgs = OrgInfo.objects.filter(id__in = userloveorgid)
    print(orgs)
    return render(request,'users/usercoures.html',{
        'orgs':orgs,
    })







