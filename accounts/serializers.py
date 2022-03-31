
from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','username', 'first_name','last_name','email','photo','birth_date','position') # 'id','username', 'first_name', 'last_name','email',    


