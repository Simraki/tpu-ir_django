from django.urls import path, include

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginView.as_view(), name='knox_login'),
    path('logout', LogoutView.as_view(), name='knox_logout')
]