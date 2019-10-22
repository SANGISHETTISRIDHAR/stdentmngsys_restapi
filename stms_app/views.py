from django.shortcuts import render,redirect
from stms_app.models import Student,School
from stms_app.api.serializers import  School_serializer,Student_serializer
# Create your views here.
def welcome(request):
    qs=School.objects.all()
    return render(request,'welcomepage.html',{"data":qs})


def saveschool(request):
    sn=request.POST.get('sn')
    slocation=request.POST.get('sl')
    spwd=request.POST.get('pwd')
    School(school_name=sn,school_place=slocation,school_pwd=spwd).save()
    qs=School.objects.all()
    qs1=Student.objects.all()
    return render(request,'welcomepage.html',{"data":qs,"data1":qs1})


def schoolcheck(request):
    s_id=request.POST.get('sid')
    s_pwd= request.POST.get('spwd')
    qs=School.objects.filter(school_id=s_id,school_pwd=s_pwd)
    if qs:
        return render(request,'schoolwelcome.html',{"data":qs})
    else:
        return redirect('/1/')

def signupstudent(request):
    sname=request.POST.get('sname')
    spwd=request.POST.get('spwd')
    sage=request.POST.get('sage')
    scno=request.POST.get('scno')
    sgen=request.POST.get('sgen')
    sschool=request.POST.get('sid')
    if int(sage)>18:
        s=True
    else:
        s=False
    Student(student_name=sname,student_age=sage,student_cno=scno,student_gen=sgen,student_is_adult=s,school_id_id=sschool,student_pwd=spwd).save()
    return render(request,'studentwelcomepage.html')


def studenctcheck(request):
    sname=request.POST.get('sname')
    spwd=request.POST.get('spwd')
    sclname=request.POST.get('sclname')
    qs=Student.objects.filter(student_name=sname,student_pwd=spwd,school_id_id=sclname)
    if qs:
        return render(request,'studentwelcomepage.html',{"data":qs})
    else:
        return redirect('/1/')
from django.contrib.auth import authenticate


def loggincheck(request):
    sname=request.POST['sname']
    spwd=request.POST['spwd']
    user=authenticate(username=sname, password=spwd)
    if user!=None:
        return redirect('/api/')
    else:
        return redirect('/login/')


def obtain_auth_token(request):

    return None

from rest_framework.views import APIView,Response
from rest_framework import mixins
from django.http import HttpResponse
from rest_framework import generics

class Searchid(generics.ListAPIView):
    serializer_class = School_serializer
    def get_queryset(self):
        queryset=School.objects.all()
        id=self.request.query_params.get('id',None)
        if id!= None:
            queryset=queryset.filter(school_id=id)
        return queryset
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
class Studenfilter(generics.ListAPIView):
    serializer_class = Student_serializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields=['=student_age','=student_name']
    pagination_class = PageNumberPagination

class Studentord(generics.ListAPIView):
    serializer_class = Student_serializer
    queryset = Student.objects.all()
    filter_backends =[filters.OrderingFilter]
    ordering_fileds=['student_name']
    ordering=['student_name']
