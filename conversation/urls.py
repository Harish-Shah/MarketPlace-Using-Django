from django.urls import path
from .import views as v

app_name='conversation'

urlpatterns=[
    path('',v.inbox,name='inbox'),
    path('<int:pk>/',v.detail,name='detail'),
    path('new/<int:item_pk>/', v.new_conversation, name='new'),

]