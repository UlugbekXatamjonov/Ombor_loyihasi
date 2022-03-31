from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import MyUser
from .serializers import UserSerializer

from django.http import HttpResponse

def empty_view(request):
    return HttpResponse('')

class UserList(ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


