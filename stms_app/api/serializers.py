from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from stms_app.models import Student,School

class Student_serializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class School_serializer(ModelSerializer):
    school=Student_serializer(read_only=True,many=True)
    class Meta:
        model=School
        fields='__all__'
        #read_only_fields = ('school_id')
class loginSerializers(serializers.ModelSerializer):
    class Meta:
        model = loginModel
        fields = ('id', 'phone', 'password')