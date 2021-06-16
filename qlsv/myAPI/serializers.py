from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Student
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        # fields = ('masv','hoten','khoa','gioitinh') 
        fields = '__all__'
from django.contrib.auth.models import User 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['username','password']

