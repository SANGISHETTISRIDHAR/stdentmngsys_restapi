# Generated by Django 2.2.4 on 2019-10-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stms_app', '0002_auto_20191001_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_cno',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='student_gen',
            field=models.CharField(default=False, max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]