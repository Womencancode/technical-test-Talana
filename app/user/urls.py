from django.urls import path

from user import views

app_name = 'users'
urlpatterns = [
    path('', views.UserList.as_view(), name='create'),
    path('my-profile/', views.UserDetail.as_view(), name='my-profile'),
    path('login/', views.CreateTokeView.as_view(), name='login'),
    path('requests/', views.RequestList.as_view(), name='create'),
    path('requests/<int:pk>/', views.RequestDetail.as_view(), name='create'),
]
