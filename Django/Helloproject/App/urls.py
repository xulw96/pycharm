from django.urls import path

from App import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('editblog/', views.edit_blog, name='edit_blog')
]