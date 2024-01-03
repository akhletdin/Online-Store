from django.urls import path

from user import views

urlpatterns = [
    path('auth/register/', views.register_view),
    path('auth/login/', views.auth_view),
    path('auth/logout/', views.logout_view),
    path('auth/profile/', views.profile_view),
    path('auth/profile/delete/', views.delete_profile_view),
]
