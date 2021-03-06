from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('StartViewSet',views.StartViewSet, base_name='StartViewSet')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet, base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    url(r'^start-view/', views.StartApiView.as_view()),
    url(r'', include(router.urls))
]

