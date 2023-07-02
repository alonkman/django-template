
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get_all_images', views.getImages),
    path('upload_image',views.APIViews.as_view()),
]
