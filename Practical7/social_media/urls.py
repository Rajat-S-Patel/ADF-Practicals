from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/',view=views.postCreate.as_view(),name='post-create'),
    path('post/<int:pk>',view=views.postDetail.as_view(),name='post-detail'),
    path('post/<int:pk>/delete',view=views.postDelete.as_view(),name='post-delete'),
    path('post/<int:pk>/update',view=views.postUpdate.as_view(),name='post-update'),
]