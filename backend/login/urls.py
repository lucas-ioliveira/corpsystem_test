from django.urls import path
from .views import LoginAuthToken, CreateUserView

urlpatterns = [
    path('', LoginAuthToken.as_view()),
    path('criar/', CreateUserView.as_view()),
]
