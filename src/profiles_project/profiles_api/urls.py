from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^start-view/', views.StartApiView.as_view())
]

