from django.shortcuts import render ,redirect ,reverse
from django.http import HttpResponse ,JsonResponse
from .models import *
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from operations.models import *
from .forms import *
from orgs.models import *



def CouresInfo(request):
    couresinfo = CourseInfo.objects.all()

    sort = request.GET.get('sort','')
    if sort:
        couresinfo = couresinfo.order_by('-'+sort)

    pagenum = request.GET.get('pagenum','')
    pa = Paginator(couresinfo,10)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'coures/coures.html',{
        'couresinfo':couresinfo,
        'pages':pages,
        'sort':sort,
    })


def CouresDetail(request,couresid):
    if couresid:
        couresdetail = CourseInfo.objects.filter(id = couresid)[0]
        print(couresdetail)
        #点击量自动增加
        couresdetail.click_num += 1
        couresdetail.save()
        #获取收藏信息 如果用户存在 且收藏里有记录则改False 为 True 再把值返回给前端页面
        # lovecoures = False
        # loveorg = False
        # if request.user.is_authenticated():
        #     love = UserLove.objects.filter(love_id=couresid, love_status=True, love_type=1, love_man=request.user)
        #     if love:
        #         lovecoures = True
        #     loveorgs = UserLove.objects.filter(love_id=couresdetail.orginfo.id,love_status=True, love_type=2, love_man=request.user))
        #     if loveorgs:
        #         loveorg = True

        return render(request,'coures/couresdetail.html',{
            'couresdetail':couresdetail,
            # 'lovecoures':lovecoures,
            # 'loveorg':loveorg,
        })


def CouresVideo(request,couresid):
    if couresid:
        couresinfo = CourseInfo.objects.filter(id=couresid)[0]
        #用户是否学习过该课程
        studyuser = UserCourse.objects.filter(study_man=request.user,study_course=couresinfo)
        #如果用户已学习过 直接返回 没有学习就保存数据
        if not studyuser:
            a = UserCourse()
            a.study_man = request.user
            a.study_course = couresinfo
            a.save()

        #学过课程的用户还学过什么
        coureslist = UserCourse.objects.filter(study_course=couresid)
        userlist = [ couresuser.study_man for couresuser in coureslist ]
        #排除当前所在课程的其它课程
        usercoureslist = UserCourse.objects.filter(study_man__in=userlist).exclude(study_course=couresid)
        usercoure = list(set([usercou.study_course for usercou in usercoureslist ]))
        #用set 集合去重
        print(usercoure)

        sort_coures = UserCourse.objects.order_by('-id')

        return render(request,'coures/couresvideo.html',{
            'couresinfo':couresinfo,
            'sort_coures':sort_coures,
            # 'lesson':lesson,
        })

def CouresComment(request):
    usercomment = UserCommentForm(request.POST)
    if usercomment.is_valid():
        coures = usercomment.cleaned_data['coures']
        content = usercomment.cleaned_data['content']

        a = UserComment()
        a.comment_course = coures
        a.comment_man = request.user
        a.comment_content = content
        a.save()
        return JsonResponse({
            'status':'ok',
            'msg':'ok'
        })
    else:
        return JsonResponse({
            'status':'fail',
            'msg':'error'
        })




