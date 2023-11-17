from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

#viewset url

router=DefaultRouter()

router.register("viewseturl",todoviewsets,basename='todoviewsets'),
router.register("studenturl",studentview,basename='studentview'),
router.register("personurl",personview,basename='personview')

urlpatterns=[
     path('todos/',todosview.as_view(),name='todos'),
     path('movies/',movieview.as_view(),name='movies'),
     path('todosid/<pk>',tododetails.as_view(),name='todosid'),
     path('movieid/<pk>',moviesview.as_view(),name='movieid'),
     path('hotel/',hotelsview.as_view(),name='hotel'),
     path('hotelsid/<pk>',hotelview.as_view(),name='hotelsid'),
     path('product/',productview.as_view(),name='product'),
     path('productid/<int:id>',productdetails.as_view(),name='productid'),
     path('fileup/',fileupview.as_view(),name='fileup'),
     path('fileupid/<int:id>',fileupdetails.as_view(),name='fileupid'),
     path('filesupload/',filesupview.as_view(),name='filesupload'),
     path('filesuploadid/<int:id>',filesupdetails.as_view(),name='filesuploadid'),
     path('employee/',employeeview),
     path('employeedetails/<int:id>',employeedetails),
     path('userreg/',usercreationview.as_view(),name='userreg'),
     path('userlogin/',signinview.as_view(),name='userlogin'),
     path('userlogout/',logoutview.as_view(),name='userlogout'),
     path('userregister/',userregistration.as_view(),name='userregister'),
     path('login/',loginview.as_view(),name='login'),
     path('customer/',customerview.as_view(),name='customer'),
     path('registeruser/',Registeruser.as_view(),name='registeruser'),
     # path('registerdetails/',Userdetails.as_view(),name='registerdetails')
]+(router.urls)
