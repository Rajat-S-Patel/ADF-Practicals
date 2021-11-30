from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('signout', views.signout,name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('user/<int:pk>/update', view=views.PersonalInfoUpdate.as_view(), name='user-update')
]
