from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('addpost/', views.addPostView, name='addpost_url'),
    path('post/<postId>/', views.postView, name='post_url'),
]