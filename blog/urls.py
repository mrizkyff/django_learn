from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slug:slugInput>/', views.detailPost, name="detail"),
    path('category/<slug:categoryInput>/', views.categoryPost, name="category"),
    path('contact/', views.kontak, name="contact"),
]

app_name = 'blog'