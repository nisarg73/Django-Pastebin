from django.urls import path
from pasteapp import views
urlpatterns = [
        path('', views.index),
        path('paste/<str:paste_url>/', views.ret_objects)
        ]

