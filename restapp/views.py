from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView
from.serializer import *
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authtoken.models import Token

# without using id
#APIView
class todosview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        a=todoserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        else:
            return Response(a.errors)
    def get(self,request):
        aa=todos.objects.all()
        a=todoserializer(aa,many=True)
        return Response(a.data)

class movieview(APIView):
    def post(self,request):
        a=movieserializer(data=request.data)
        if a.is_valid():
            a.save()
        return Response(a.data)
    def get(self,request):
        bb=moviemodel.objects.all()
        a=movieserializer(bb,many=request.data)
        return Response(a.data)

    #with using id

class tododetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,**kwargs):
        todo = todos.objects.get(id=kwargs.get('pk'))
        a=todoserializer(todo)
        return Response(a.data)


    #update
    def put(self,request,**kwargs):
        todo=todos.objects.get(id=kwargs.get('pk'))
        a=todoserializer(instance=todo,data=request.data)
        if a.is_valid():
            a.save()
        return Response(a.data)
    #delete
    def delete(self,request,**kwargs):
        todo=todos.objects.get(id=kwargs.get('pk'))
        todo.delete()
        return Response({'msg':'Deleted'})

class moviesview(APIView):
    def get(self,request,**kwargs):
        mov = moviemodel.objects.get(id=kwargs.get('pk'))
        a=movieserializer(mov)
        return Response(a.data)
    #update
    def put(self,request,**kwargs):
        movies=moviemodel.objects.get(id=kwargs.get('pk'))
        a=movieserializer(instance=movies,data=request.data)
        if a.is_valid():
            a.save()
        return Response(a.data)
    #delete
    def delete(self,request,**kwargs):
        movie=moviemodel.objects.get(id=kwargs.get('pk'))
        movie.delete()
        return Response({'msg':'Deleted'})

class hotelsview(APIView):
    def post(self,request):
        try:
            a=hotelserializer(data=request.data)
            a.is_valid(raise_exception=True)
            a.save()
            return Response(a.data)
        except UnicodeDecodeError as e:
            return Response({'error':'error'})
    def get(self,request):
        cc=hotelmodel.objects.all()
        dd=hotelserializer(cc,many=True)
        return Response(dd.data)

class hotelview(APIView):
    def get(self,request,**kwargs):
        hotel=hotelmodel.objects.get(id=kwargs.get('pk'))
        a=hotelserializer(hotel)
        return Response(a.data)
    def put(self,request,**kwargs):
        hotel=hotelmodel.objects.get(id=kwargs.get('pk'))
        h=hotelserializer(instance=hotel,data=request.data)
        if h.is_valid():
            h.save()
        return Response(h.data)
    def delete(self,request,**kwargs):
        hot=hotelmodel.objects.get(id=kwargs.get('pk'))
        hot.delete()
        return Response({'msg':'details deleted'})

#GenericAPIView
from rest_framework import generics
from rest_framework import mixins

class productview(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = productserializer
    queryset = productmodel.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class productdetails(generics.GenericAPIView,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = productmodel.objects.all()
    serializer_class = productserializer
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class fileupview(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin):
    queryset = fileupmodel.objects.all()
    serializer_class = fileupserializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class fileupdetails(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = fileupmodel.objects.all()
    serializer_class = fileupserializer
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    # using media
class filesupview(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin):
    queryset = filesupmodel.objects.all()
    serializer_class = filesupserializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class filesupdetails(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = filesupmodel.objects.all()
    serializer_class = filesupserializer
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



#Viewset
from rest_framework import viewsets
from rest_framework import status

class todoviewsets(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = viewserializer
    model = viewmodel
    def list(self,request):
        a=self.model.objects.all()
        b=self.serializer_class(a,many=True)
        return Response(b.data,status=status.HTTP_200_OK)

    def create(self,request):
        a=self.serializer_class(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))  #pk-keyword argument
        b=self.serializer_class(data=request.data,instance=a)
        if b.is_valid():
            b.save()
            return Response(b.data,status=status.HTTP_201_CREATED)
        else:
            return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(a)
        return Response(b.data,status=status.HTTP_200_OK)

    def destroy(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        a.delete()
        return Response({'msg':'Deleted'},status=status.HTTP_200_OK)


class studentview(viewsets.ViewSet):
    serializer_class = studentserializer
    model = studentmodel
    def list(self,request):
        a=self.model.objects.all()
        b=self.serializer_class(a,many=True)
        return Response(b.data,status=status.HTTP_200_OK)

    def create(self,request):
        a=self.serializer_class(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(data=request.data,instance=a)
        if b.is_valid():
            b.save()
            return Response(b.data,status=status.HTTP_201_CREATED)
        else:
            return Response(b.data,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(a)
        return Response(b.data,status=status.HTTP_200_OK)

    def destroy(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        a.delete()
        return Response({'msg':'Deleted'},status=status.HTTP_200_OK)

#ModelViewSet
#using class
class personview(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = personserializer
    queryset = personmodel.objects.all()

# API Creation using function based view

from rest_framework.decorators import api_view,permission_classes,authentication_classes

@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def employeeview(request):
    if(request.method=='GET'):
        a=employeemodel.objects.all()
        b=employeeserializer(a,many=True)
        return Response(b.data,status=status.HTTP_200_OK)
    if(request.method=='POST'):
        a=employeeserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def employeedetails(request,id):
    if(request.method=='GET'):
        a=employeemodel.objects.get(id=id)
        b=employeeserializer(a)
        return Response(b.data,status=status.HTTP_200_OK)
    if(request.method=='PUT'):
        a=employeemodel.objects.get(id=id)
        b=employeeserializer(instance=a,data=request.data)
        if b.is_valid():
            b.save()
            return Response(b.data,status=status.HTTP_201_CREATED)
        else:
            return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
    if(request.method=='DELETE'):
        a=employeemodel.objects.get(id=id)
        a.delete()
        return Response({'msg':'data deleted'})

#API registration and login using User

 #register
class usercreationview(APIView):
    def post(self,request):
        a = userserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response({"msg":"Registered successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        qs=User.objects.all()
        a=userserializer(qs,many=True)
        return Response(a.data)

#login
from django.contrib.auth import authenticate,login

class signinview(APIView):
    def post(self,request):
        serializer = loginserializer(data=request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user = authenticate(request,username=uname,password=password)
            if user:
                login(request,user)
                return Response({'msg':'Logged in successfully'})
            else:
                return Response({'msg':'Login failed'})

#logout
from django.contrib.auth import logout

class logoutview(APIView):
    def post(self,request):
        #log the user out by clearing the session cookies
        logout(request)
        return Response({'msg':'Logged out successfully'})

#API using unauthenticated user
#register
class userregistration(APIView):
    def post(self, request):
        a = userregserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response({"msg": "Registered successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        qs = userregmodel.objects.all()
        a = userregserializer(qs, many=True)
        return Response(a.data)

#login
class loginview(APIView):
    def post(self,request):
        serializer = logserializer(data=request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            a=userregmodel.objects.all()
            for i in a:
                if uname==i.username and password==i.password:
                    return Response({'msg':'Login success'})
            else:
                return Response({'msg':'login failed'})

#validators

class customerview(APIView):
    def post(self,request):
        a=customerserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        else:
            return Response(a.errors)
    def get(self,request):
        aa=customermodel.objects.all()
        a=customerserializer(aa,many=True)
        return Response(a.data)

# user model

class Registeruser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        a=Usertokenserializer(data=request.data)
        if a.is_valid():
            a.save()
            user=User.objects.get(username=a.data['username'])
            token_obj ,_=Token.objects.get_or_create(user=user)
            return Response({'data':a.data,'token':str(token_obj)})
        else:
            return Response(a.errors)

    def get(self,request):
        b=User.objects.all()
        c=Usertokenserializer(b,many=True)
        return Response(c.data)


# class Userdetails(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, **kwargs):
#         user = User.objects.get(id=kwargs.get('pk'))
#         a = Usertokenserializer(user)
#         return Response(a.data)
#
#     # update
#     def put(self, request, **kwargs):
#         user = User.objects.get(id=kwargs.get('pk'))
#         a = Usertokenserializer(instance=todo, data=request.data)
#         if a.is_valid():
#             a.save()
#         return Response(a.data)
#
#     # delete
#     def delete(self, request, **kwargs):
#         user = Usertokenserializer.objects.get(id=kwargs.get('pk'))
#         user.delete()
#         return Response({'msg': 'Deleted'})


















