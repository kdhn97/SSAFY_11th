from django.urls import path
from . import views


app_name = 'garages'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    # create에 요청이 들어왔을때, create view 함수가 실행
    path('create/', views.create, name='create'),
    path('<int:garage_pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    # path('create/', views.create, name='create'),
    # path('create/', views.create, name='create'),
]
