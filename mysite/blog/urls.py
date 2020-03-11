from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
        path('', views.post_list, name = 'post_list'),
        path('login/', views.login_data, name = 'login_data')
        ]
#%%