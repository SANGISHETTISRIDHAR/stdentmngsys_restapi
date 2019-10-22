from django.db import models

# Create your models here.
class School(models.Model):
    school_id=models.AutoField(primary_key=True)
    school_name=models.CharField(max_length=100)
    school_pwd=models.CharField(max_length=25, default=False)
    school_place=models.CharField(max_length=100)
    def __str__(self):
        return self.school_name

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=50)
    student_pwd=models.CharField(max_length=25,default=False)
    student_age=models.IntegerField()
    student_cno=models.IntegerField(default=False)
    student_gen=models.CharField(max_length=25,default=False)
    student_is_adult=models.BooleanField(default=False)
    school_id=models.ForeignKey(School,on_delete=models.CASCADE)


class loginModel (models.Model):
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
