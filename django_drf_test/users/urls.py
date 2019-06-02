from django.urls import path

from .views import UserGetUpdateView, CreateUserView, login

app_name = 'users'

urlpatterns = [
    path('edit/', UserGetUpdateView.as_view(), name='list-edit-view'),
    path('edit/<int:pk>', UserGetUpdateView.as_view(), name='edit-view'),
    path('create/', CreateUserView.as_view(), name='create-user-view'),
    path('login/', login),
]
