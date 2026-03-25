from django.urls import path
from .import views

urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    path('post/<slug:slug>/',views.post_detail,name='post_detail_url'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail_url'),
    path('search/',views.search,name='search_resaults'),
    path('register/',views.register,name='register')
]