from django.urls import path
from . import views


urlpatterns = [
    path('user',views.userpage,name='userpage'),
    path('', views.home, name="home"),
    path('register',views.registerpage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name = 'logout'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]