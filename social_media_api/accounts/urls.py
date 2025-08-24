from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow_user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('', include(router.urls)),
]
