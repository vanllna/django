from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage

def OrgsList(request):
    #获取相关模型中的数据
    orgslist = OrgInfo.objects.all()
    # print(orgslist.values())
    # 排序
    sort_orgs = orgslist.order_by('-love_num')[:2]
    #查询的切片操作
    citylist = CityInfo.objects.all()
    #按照机构分类筛选
    cate = request.GET.get('cate','')
    if cate:
        orgslist = orgslist.filter(category=cate)
        #如果 cate 存在 就过滤相关数据
        # print(catelist.values())
    # elif cate == '':
    #     orgslist = orgslist
    #全部数据
    #按照城市筛选
    city = request.GET.get('city','')
    if city:
        orgslist = orgslist.filter(cityinfo_id=city)
    sort = request.GET.get('sort','')
    if sort:
        orgslist = orgslist.order_by('-'+sort)
    #接收前端的pagenum参数
    pagenum = request.GET.get('pagenum','')
    #把查询到的数据，按多少条数据分页
    pa = Paginator(orgslist,4)
    try :
        #正常情况下的分页显示
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        #上一页
        pages = pa.page(1)
    except EmptyPage:
        #下一页
        pages = pa.page(pa.num_pages)

    return render(request,'orgs/orgslist.html',{
        'orgslist':orgslist,
        'sort_orgs':sort_orgs,
        'pages':pages,
        'cate':cate, #把cate 再传回给前端
        'city':city,
        'citylist':citylist,
        'sort':sort,
    })


def OrgsDetail(request,orgs_id):
    if orgs_id:
        orgs = OrgInfo.objects.filter(id = orgs_id)
    return render(request,'orgs/orgsdetail.html',{
        'orgs':orgs,
    })

