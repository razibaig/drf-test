from django.urls import path

from .views import PostsView

urlpatterns = [
    path('list/', PostsView.as_view(), name='posts-list-view'),
    path('list/<int:pk>', PostsView.as_view(), name='posts-create-view'),
]
