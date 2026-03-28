# I have Created this File Rutwik Patil

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')
    # return HttpResponse("Hello World")

def about(request):
    return HttpResponse("Hello Rutwik Patil")

# def detailinfo(request):
#     # print(request.GET.get('text','default'))
#     text=request.GET.get('text','default')
#     rpunc=""
#     for x in text:
#         if x!='!':
#             rpunc+=x
#     data={
#         'original':text,
#         'title':rpunc.title(),
#         'upper':rpunc.upper(),
#         'lower':rpunc.lower(),
#         'len':len(rpunc),
#         'swapcase':rpunc.swapcase(),
#         'removepunc':rpunc
#     }
#     return render(request,'details.html',data)
#     # return HttpResponse("detailinfo")


# def detailinfo(request):
    text=request.GET.get('text','default')
    uppercase=request.GET.get('uppercase','off')
    lowercase=request.GET.get('lowercase','off')
    swapcase=request.GET.get('swapcase','off')
    title=request.GET.get('title','off')
    le=request.GET.get('len','off')
    data={}
    if(uppercase=='on'):
        data['upper']=text.upper()
    if(lowercase=='on'):
        data['lower']=text.lower()
    if(swapcase=='on'):
        data['swap']=text.swapcase()
    if(title=='on'):
        data['title']=text.title()
    if(le=='on'):
        data['le']=len(text)
    data['text']=text
    return render(request,'details2.html',data)

def detailinfo(request):
    text=request.POST.get('text','default')
    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    swapcase=request.POST.get('swapcase','off')
    title=request.POST.get('title','off')
    le=request.POST.get('len','off')
    data={}
    if(uppercase=='on'):
        data['upper']=text.upper()
    if(lowercase=='on'):
        data['lower']=text.lower()
    if(swapcase=='on'):
        data['swap']=text.swapcase()
    if(title=='on'):
        data['title']=text.title()
    if(le=='on'):
        data['le']=len(text)
    data['text']=text
    return render(request,'details2.html',data)
