from rest_framework import viewsets
from .serializers import Student_serializer,School_serializer
from stms_app.models import Student,School
from rest_framework.pagination import PageNumberPagination
class Authtoken(viewsets.ModelViewSet):
    serializer_class = Student_serializer
    queryset = Student.objects.all()
    pagination_class = PageNumberPagination


class Authtoken1(viewsets.ModelViewSet):
     serializer_class = School_serializer
     queryset = School.objects.all()


class loginView(viewsets.ModelViewSet):
    queryset = loginModel.objects.all()
    serializer_class = loginSerializers