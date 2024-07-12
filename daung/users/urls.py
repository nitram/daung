from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create_page, name="create"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),
]