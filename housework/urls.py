from django.contrib import admin
from django.urls import path
from .views import listview, CreateClass, detailview,DeleteClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', listview, name= 'list'),
    path('create/', CreateClass.as_view(),name= 'create'),
    path('detail/<str:ck>/', detailview, name= 'detail'),
    path('delete/<int:pk>/', DeleteClass.as_view(), name= 'delete'),
    
]

