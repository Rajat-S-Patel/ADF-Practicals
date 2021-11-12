from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('signout', views.signout,name='signout'),
    path('home',view=views.home,name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('personalInfo/<int:pk>',view=views.PersonalInfo.as_view(),name='personalinfo'),
    path('personalInfo/<int:pk>/update', view=views.PersonalInfoUpdate.as_view(), name='personalinfo-update')
]
