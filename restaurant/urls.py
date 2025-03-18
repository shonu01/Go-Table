from django.urls import path
from . import views

urlpatterns = [
    # Core Views
    path('', views.home, name='home'),  # Home Page
    path('profile/', views.profile_update, name='profile_update'),  # Profile Update
    path('register/', views.register, name='register'),  # Registration
    
    # Authentication Views
    path('login/', views.login_view, name='login'),  # Custom Login View
    path('logout/', views.logout_view, name='logout'),  # Custom Logout View
    
    # Catalog Page
    path('catalog/', views.catalog_view, name='catalog'),  # Ensure catalog.html exists
]
