from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('',views.getRoutes),
    path('getProjects/',views.getProjects),
    path('getProjects/<str:pk>/',views.getProject),
    path('getProjects/<str:pk>/vote/',views.getProject),
    
    
]