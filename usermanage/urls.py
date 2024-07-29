# usermanage/urls.py
from django.urls import path
from usermanage import views

urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name='hello-world'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('admin/', views.UserListView.as_view(), name='admin-user-list'),
    path('admin/<int:pk>/', views.UserDetailView.as_view(), name='admin-user-detail'),

]

