from distutils.command.upload import upload
from django.db import models


class project(models.Model):
    project_num = models.CharField(max_length=3) #課題番号に意味はないのでIntegerではなくCharfieldを使った
    wall_name = models.CharField(max_length=10) #壁の名前
    setter_name = models.CharField(max_length=20) #セッターの名前
    #image = models.ImageField(null=True, blank=True) #課題の写真

    def __str__(self):
        return self.setter_name