import csv

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import StoreId
from .crawllist import aladin_book

# Create your views here.
def index(request):
    # userid = get_object_or_404(StoreId, pk=userid)
    return render(request, 'ebooklist/index.html', context=None)

def ids(request):
    return render(request, 'ebooklist/ids.html', context=None)

def getlist(request):
    return render(request, 'ebooklist/getlist.html', context=None)

def collect(request):
    try:
        userid = StoreId.objects.get(userid=request.POST['userid'])
    except (KeyError, StoreId.DoesNotExist):
        return render(request, 'ebooklist/getlist.html', {})
    else:
        # print(userid, "is OK")
        context = {}
        if StoreId.objects.get(userid=request.POST['userid']).aladin_id == request.POST['aladin_id']:
            context['aladin_list']=aladin_book(request.POST['aladin_id'], request.POST['aladin_pw'])

            print(context)
        else:
            print("NO")
        if StoreId.objects.get(userid=request.POST['userid']).yes24_id == request.POST['yes24_id']:
            print("OK")
        else:
            print("NO")
        if StoreId.objects.get(userid=request.POST['userid']).ridibooks_id == request.POST['ridibooks_id']:
            print("OK")
        else:
            print("NO")

        # CSV 포맷 저장
        # f_csv = open("ebooklist/static/ebooklist/temporary/"+request.POST['userid']+"ebook"+str(timezone.now().date())+".csv", 'w+')
        f_csv = open("ebooklist/static/temporary/"+request.POST['userid']+"book.csv", 'w+')
        writer = csv.writer(f_csv)
        writer.writerow(('서점', '제목', '구입일', '링크'))
        for book in context['aladin_list']:
            writer.writerow((book['store'], book['title'], book['buydate'], book['link']))
        f_csv.close()

        context['userid'] = request.POST['userid']
        context['aladin_id'] = request.POST['aladin_id']
        return render(request, 'ebooklist/getlist.html', context)
