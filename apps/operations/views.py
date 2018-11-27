from django.shortcuts import render
from .forms import *
from .models import *
from django.http import JsonResponse
from orgs.models import *
from courses.models import *
from django.db.models import Q , F

# Create your views here.
def user_ask(request):
    user_ask_from = UserAskForms(request.POST)
    print(user_ask_from)
    if user_ask_from.is_valid():
        user_ask_from.save(commit=True)
        #保存提交的数据
        return JsonResponse({
            'status':'ok',
            'msg':'提交成功',
        })
    else:
        return JsonResponse({
            'status':'fail',
            'msg':'提交失败',
        })

def user_love(request):
    loveid = request.GET.get('loveid','')
    lovetype = request.GET.get('lovetype','')

    if loveid and lovetype:
        # 判断是哪一种收藏类型 并做加减处理
        obj = None
        if lovetype == 1:
            obj = CourseInfo.objects.filter(id = loveid)[0]
        if lovetype == 2:
            obj = OrgInfo.objects.filter(id=loveid)[0]
        if lovetype == 3:
            obj = TeacherInfo.objects.filter(id=loveid)[0]


        #如果收藏已存在 ，验证收藏记录
        love = UserLove.objects.filter(loveid=loveid,lovetype=lovetype)
        if love:
            if love[0].love_status:
                #如果状态是真 当用户再次请求时 把状态改为假
                love[0].love_status = False
                love[0].save()
                obj.love_num -= 1
                obj.save()
                return JsonResponse({
                    'success':'ok',
                    'msg':'收藏',
                })
            else:
                #如果状态为假 把状态改为真
                love[0].love_status = True
                love[0].save()
                obj.love_num +=1
                obj.save()
                return JsonResponse({
                    'success': 'ok',
                    'msg': '取消收藏',
                })
        else:
            #如果没有收藏数据 ，创建收藏数据
            a = UserLove()
            a.love_man = 'aaa'
            a.love_id = loveid
            a.love_type = lovetype
            a.love_status = True
            a.save()
            obj.love_num +=1
            obj.save()
            return JsonResponse({
                'success':'ok',
                'msg':'收藏成功',
            })

    else:
        return JsonResponse({
            'fail':'error',
            'msg':'失败',
        })


def user_dellove(request):
    loveid = request.GET.get('love_id','')
    lovetype = request.GET.get('love_type','')
    print(loveid,lovetype)

    if loveid and lovetype:
        love = UserLove.objects.filter(love_id=loveid,love_type=lovetype,love_status=True,love_man=request.user)
        if love:
            love[0].love_status = False
            love[0].save()
            return JsonResponse({
                'status':'ok',
                'msg':'cancel success'
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': 'cancel fail'
            })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': 'cancel fail'
        })


def orginfo(request):
    orglist = OrgInfo.objects.all()
    #根据base页面 传回来的搜索关键字 检索相关内容并返回
    keyword = request.GET.get('keyword','')
    if keyword:
        orglist = orglist.filter(Q(name__icontains=keyword)|Q(desc__icontains=keyword))




