from .models import *
from rest_framework import serializers

class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = '__all__'

class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = moviemodel
        fields ='__all__'

class hotelserializer(serializers.ModelSerializer):
    class Meta:
        model = hotelmodel
        fields ='__all__'

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = productmodel
        fields ='__all__'

class fileupserializer(serializers.ModelSerializer):
    class Meta:
        model = fileupmodel
        fields ='__all__'

class filesupserializer(serializers.ModelSerializer):
    class Meta:
        model = filesupmodel
        fields ='__all__'

class viewserializer(serializers.ModelSerializer):
    class Meta:
        model = viewmodel
        fields ='__all__'

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = studentmodel
        fields ='__all__'

class personserializer(serializers.ModelSerializer):
    class Meta:
        model = personmodel
        fields ='__all__'

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employeemodel
        fields ='__all__'

#API registration and login ***important interview

from django.contrib.auth.models import User

#register
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password']

    def create(self, validated_data):
        a=User.objects.create(username=validated_data['username'],email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        a.set_password(validated_data['password'])
        a.save()
        return a

#login
class loginserializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)

#API using unauthenticated user
#register
class userregserializer(serializers.ModelSerializer):
    class Meta:
        model = userregmodel
        fields =['username','password','email','phone']

    def create(self,validated_data):
        a=userregmodel.objects.create(username=validated_data['username'],password=validated_data['password'],email=validated_data['email'],phone=validated_data['phone'])
        a.save()
        return a

#login
class logserializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)

#validators

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = customermodel
        fields ='__all__'

#user model

class Usertokenserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password']

        def create(self, validated_data):
            a = User.objects.create(username=validated_data['username'], email=validated_data['email'],
                                    first_name=validated_data['first_name'], last_name=validated_data['last_name'])
            a.set_password(validated_data['password'])
            a.save()
            return a




