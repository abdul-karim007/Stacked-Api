# from django.conf.urls import url
from django.urls import path, include
from .views import (
    ApiAppListApiView,
)

urlpatterns = [
    path('api', ApiAppListApiView.as_view()),
    path('api/<int:todo_id>/', ApiAppListApiView.as_view()),

]