from django.urls import path

from . import views


app_name = 'departments'

urlpatterns = [
    path('list/', views.department_list, name='list'),
    path('create/', views.department_create, name='create'),
    path('detail/<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.department_detail, name='detail'),
    path('update/<int:pk>/', views.department_update, name='update'),
    path('delete/<int:pk>/', views.department_delete, name='delete'),

]
