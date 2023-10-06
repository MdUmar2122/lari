from django.urls import path
from app import views

urlpatterns = [
    path('',views.umar, name='umar'),
    path('mark/a', views.mark1_detail),
]