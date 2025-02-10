from django.urls import path

from . import views


app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('create/', views.student_create, name='create'),
    path('detail/<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.student_detail, name='detail'),
    path('update/<int:pk>/', views.student_update, name='update'),
    path('delete/<int:pk>/', views.student_delete, name='delete'),
]
