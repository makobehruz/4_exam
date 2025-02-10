from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update-profile/', views.update_profile, name='update_profile'),

]

