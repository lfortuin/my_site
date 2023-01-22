from django.urls import path
from . import views

app_name = 'cv_build'
urlpatterns = [
    path('info/', views.info, name="info"),
    path('<int:id>/', views.build_cv, name="build_cv"),
    path('list_of_users/', views.list_of_users, name='list_of_users')
]