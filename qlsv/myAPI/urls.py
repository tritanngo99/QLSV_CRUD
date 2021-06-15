from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Login.as_view(),name='login'),
    path('home',views.Home.as_view(),name='home'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('insert',views.Add.as_view(),name='add'),
    path('edit/<str:id>',views.Edit.as_view(),name='edit'),
    path('delete/<str:id>',views.Delete.as_view(),name='delete')
]   
