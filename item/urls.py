from django.urls import path
from .import views as v

app_name='item'

urlpatterns=[
    path('',v.items,name='items'),
    path('new/',v.new,name='new'),
    path('<int:pk>/',v.detail,name='detail'),
    path('<int:pk>/delete',v.delete,name='delete'),
    path('<int:pk>/edit/', v.edit, name='edit'),
]

