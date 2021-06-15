from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View 
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

class Login(View):
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
class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            student = Student.objects.all()
            return render(request,'home/index.html',{"content":student})
            
        else:
            redirect('/')
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
class Add(View):
    def get(self,request):
        if not request.user.is_superuser:
            return redirect('login')
        return render(request,'insert/add.html')
    def post(self,request):
        student = Student()
        student.masv = request.POST.get('mssv')
        student.hoten = request.POST.get('hoten')
        student.khoa = request.POST.get('khoa')
        student.gioitinh = request.POST.get('gt')
        student.save()
        return redirect('home') 
class Edit(View):
    def get(self,request,id):
        if not request.user.is_superuser:
            return redirect('login')
        student = Student.objects.get(id=id)
        return render(request,'edit/edit.html',{'content':student})
    def post(self,request,id):
        student = Student.objects.get(id=id)
        student.masv = request.POST.get('mssv')
        student.hoten = request.POST.get('hoten')
        student.khoa = request.POST.get('khoa')
        student.gioitinh = request.POST.get('gt')
        student.save()
        return redirect('home') 
class Delete(View):
    def get(self,request,id):
        if not request.user.is_superuser:
            return redirect('login')
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('home')