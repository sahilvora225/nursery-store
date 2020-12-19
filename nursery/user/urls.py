from django.urls import path

from .views import CreateUserView, LoginView


app_name = 'user'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
