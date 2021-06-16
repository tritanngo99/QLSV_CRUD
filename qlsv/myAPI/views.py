from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.serializers import Serializer 
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login,logout
from .serializers import Studentserializer
from rest_framework.response import Response
class Login(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'login/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username +"--"+ password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login/login.html')
class Home(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            student = Student.objects.all()
            serializer = Studentserializer(student,many=True)
            if(serializer.is_valid):
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        #     return render(request,'home/index.html',{"content":student})
            
        # else:
        #     redirect('/')

class Logout(APIView):
    def get(self,request):
        logout(request)
        return redirect('login')

class Add(APIView):
    # def get(self,request):
    #     if not request.user.is_superuser:
    #         return redirect('login')
    #     return render(request,'insert/add.html')

    def post(self,request):
        student = Student()
        # student.masv = request.POST.get('mssv')
        # student.hoten = request.POST.get('hoten')
        # student.khoa = request.POST.get('khoa')
        # student.gioitinh = request.POST.get('gt')
        # student.save()
        # return redirect('home') 
        serializer = Studentserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class Edit(APIView):
    def get(self,request,id):
        if not request.user.is_superuser:
            return redirect('login')
        student = Student.objects.get(id=id)
        # return render(request,'edit/edit.html',{'content':student})
        serializer = Studentserializer(student)
        # print(serializer.data['hoten'])
        return Response(serializer.data)
    def put(self,request,id):
        student = Student.objects.get(id=id)
        # student.masv = request.POST.get('mssv')
        # student.hoten = request.POST.get('hoten')
        # student.khoa = request.POST.get('khoa')
        # student.gioitinh = request.POST.get('gt')
        # student.save()
        
        serializer = Studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)  
      

class Delete(APIView):
    def get(self,request,id):
        if not request.user.is_superuser:
            return redirect('login')
        student = Student.objects.get(id=id)
        serializer = Studentserializer(student)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,id):
        if not request.user.is_superuser:
            return redirect('login')
        student = Student.objects.get(id=id)
        serializer = Studentserializer(student,data=request.data)
        if serializer.is_valid:
            student.delete()
            return Response("Da xoa")
        else:
            return Response(serializer.errors)
