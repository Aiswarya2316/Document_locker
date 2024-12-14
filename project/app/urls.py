from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view'),
    path('edit',views.edit,name='edit')


]
