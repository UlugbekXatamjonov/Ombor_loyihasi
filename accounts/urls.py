from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('<int:pk>/', UserDetail.as_view()),
    path('', UserList.as_view()),
]
