from django.urls import path

from . import views



urlpatterns = [
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
	
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('form_submission', views.form_submission, name='form_submission'),

    path('item_1', views.item_1, name="item_1"),
    path('item_2', views.item_2, name="item_2"),
    path('item_3', views.item_3, name="item_3"),
    path('item_4', views.item_4, name="item_4"),
    path('item_5', views.item_5, name="item_5"),
    path('item_6', views.item_6, name="item_6"),
    path('item_s', views.item_s, name="item_s"),
     path('product', views.product, name="product"),
   
    
   
    

    
]