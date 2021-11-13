from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/',view=views.postCreate.as_view(),name='post-create'),
    path('post/<int:pk>',view=views.postDetail.as_view(),name='post-detail')
]