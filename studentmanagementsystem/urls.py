"""studentmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView
from rest_framework.authtoken import views
from stms_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/',views.welcome),
    path('saveschool/',views.saveschool),
    path('schoolcheck/', views.schoolcheck),
    path('signupstudent/',views.signupstudent),
    path('studenctcheck/',views.studenctcheck),
    path('api/',include('stms_app.api.url')),
    path('login/',TemplateView.as_view(template_name='login.html')),
    path('login1/',views.loggincheck),
    path('gettoken/', views.obtain_auth_token),
    path('searchid/',views.Searchid.as_view()),
    path('search/',TemplateView.as_view(template_name='search.html')),
    path('searchfilter/',views.Studenfilter.as_view()),
    path('ordfilter/', views.Studentord.as_view())
    #path('generic/',views.Generic_view.as_view()),
#    path('category/<int:pk>/', views.CategoryDetail.as_view(), name="category_detail")

]
