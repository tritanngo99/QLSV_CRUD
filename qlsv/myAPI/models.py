from django.db import models
from django.utils.translation import check_for_language

# Create your models here.
class Student(models.Model):
    GT = [('Nam','Nam'),('Nữ','Nữ')]
    masv = models.CharField(max_length=15)
    hoten = models.CharField(max_length=50)
    khoa = models.CharField(max_length=50)
    gioitinh = models.CharField(max_length=3,choices=GT)

    def __str__(self):
        return self.hoten