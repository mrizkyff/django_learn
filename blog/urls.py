from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slug:slugInput>/', views.detailPost, name="detail"),
    path('category/<slug:categoryInput>/', views.categoryPost, name="category"),
]

app_name = 'blog'