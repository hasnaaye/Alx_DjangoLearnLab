from django.urls import path
from .views import LoginAPIView   # same app where you created LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', name='register'),
    path('profile/', name='profile'),
]
