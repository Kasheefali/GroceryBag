from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerpage, name ='register'),
	path('login/', views.loginpage, name ='login'),
	path('logout/', views.logoutUser, name ='logout'),

    path('', views.homepage, name = 'home'),
    path('product_detail/<str:product_id>', views.detail, name = 'detail'),
    path('add_item/', views.add, name = 'add'),
    path('update/<str:product_id>', views.update, name= 'update'),
    path('delete/<str:product_id>', views.delete, name= 'delete'),
]
