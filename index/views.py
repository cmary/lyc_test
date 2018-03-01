# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import GoodsInfo,TypeInfo
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

# Create your views here.
# 查询每类商品最新的4个和点击率最高的4个
def index(request):
    """
    index函数负责查询页面中需要展示的商品内容，
    主要是每类最新的4种商品和4中点击率最高的商品，
    每类商品需要查询2次
    """
    count = request.session.get('count')
    fruit = GoodsInfo.objects.filter(gtype__id=2).order_by("-id")[:4]
    fruit2 = GoodsInfo.objects.filter(gtype__id=2).order_by("-gclick")[:4]
    fish = GoodsInfo.objects.filter(gtype__id=4).order_by("-id")[:4]
    fish2 = GoodsInfo.objects.filter(gtype__id=4).order_by("-gclick")[:3]
    meat = GoodsInfo.objects.filter(gtype__id=1).order_by("-id")[:4]
    meat2 = GoodsInfo.objects.filter(gtype__id=1).order_by("-gclick")[:4]
    egg = GoodsInfo.objects.filter(gtype__id=5).order_by("-id")[:4]
    egg2 = GoodsInfo.objects.filter(gtype__id=5).order_by("-gclick")[:4]
    vegetables = GoodsInfo.objects.filter(gtype__id=3).order_by("-id")[:4]
    vegetables2 = GoodsInfo.objects.filter(gtype__id=3).order_by("-gclick")[:4]
    frozen = GoodsInfo.objects.filter(gtype__id=6).order_by("-id")[:4]
    frozen2 = GoodsInfo.objects.filter(gtype__id=6).order_by("-gclick")[:4]
    # count = CartInfo.objects.filter(
    #     user_id=request.session.get('userid')).count()   'count':count,
    # # 构造上下文
    context = {'title': '首页', 'fruit': fruit,
               'fish': fish, 'meat': meat, 'egg': egg,
               'vegetables': vegetables, 'frozen': frozen,
               'fruit2': fruit2, 'fish2': fish2, 'meat2': meat2,
               'egg2': egg2, 'vegetables2': vegetables2, 'frozen2': frozen2,
               'guest_cart': 1,'page_name':0,'count':count}

    # 返回渲染模板
    return render(request, 'index/index.html', context)


def list(request,id,pageid):
    id = int(id)

    sumGoodlist=GoodsInfo.objects.filter(gtype_id=id).order_by('-id')

    paginator = Paginator(sumGoodlist, 15)
    goodList = Paginator.page(int(pageid))
    pindexlist = paginator.page_range

    return HttpResponse(pageid)
    context = {'title': '商品详情', 'list': 1,
               'guest_cart': 1, 'goodtype': goodtype,
                'goodList': goodList,
               'typeid': id,
               'pindexlist': pindexlist, 'pageid': int(pageid)}

    return render(request, 'index/list.html', context)

def goodlist(request,typeid,pageid,sort):
    """
        goodlist函数负责展示某类商品的信息。
        url中的参数依次代表
        typeid:商品类型id;selectid:查询条件id，1为根据id查询，2位根据价格查询，3位根据点击量查询
        """
    count=request.session.get('count')
    newgood=GoodsInfo.objects.all().order_by('-id')[:2]
    if sort == '1':
        sumGoodlist=GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')
    elif sort == '2':
        sumGoodlist=GoodsInfo.objects.filter(gtype_id=typeid).order_by('gprice')
    elif sort == '3':
        sumGoodlist=GoodsInfo.object.filter(gtype_id=typeid).order_by('-gclick')
    paginator=Paginator(sumGoodlist,15)
    goodList=Paginator.page(int(pageid))
    pindexlist=paginator.page_range

    goodtype =TypeInfo.object.get(id=typeid)

    context = {'title': '商品详情', 'list': 1,
               'guest_cart': 1, 'goodtype': goodtype,
               'newgood': newgood, 'goodList': goodList,
               'typeid': typeid, 'sort': sort,
               'pindexlist': pindexlist, 'pageid': int(pageid), 'count': count}

    # 渲染返回结果
    return render(request, 'index/list.html', context)
