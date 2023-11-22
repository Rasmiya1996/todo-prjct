from django.urls import path

from project_app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("new",views.new,name="new"),
    path("read",views.read,name="read"),
    path("delt/<int:id>/",views.delt,name="delt"),
    path("update/<int:id>/",views.update,name="update")
]