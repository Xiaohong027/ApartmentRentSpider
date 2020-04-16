from django.shortcuts import render
from rental_house_infos_display.models import HouseInfos
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

def indexen(request):
    return render(request, 'indexen.html')

def indexch(request):
    return render(request, 'indexch.html')

def list_ty(request):
    limit = 50 #给生成器传的第二个参数，表示每页的数目
    house_info = HouseInfos.objects #从model中传来的collection类，生成实例，拿到数据
    paginatior = Paginator(house_info,limit) #生成分页
    page = request.GET.get('page',1) #获取页数，这样写后面翻页的url会为/page=3
    data = paginatior.page(page) #获取每页的数据对象
    content = {
        'house_info':data, #传入content，前面又类似于面向对象
        'counts':house_info.count(),
        #'last-time':house_info.order_by('price').limit(1)
    }
    return render(request, 'list_ty.html', content)