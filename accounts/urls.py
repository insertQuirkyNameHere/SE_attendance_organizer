from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/',views.logout_view, name='logout'),
    path('', views.LandingPage.as_view(),name = 'home'),
    path('delete/',views.DeleteUsers.as_view(), name='del_user'),
]