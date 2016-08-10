from django.conf.urls import url
from .views import Login_view, HomePageView, Register_user, user_logout
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^$', Login_view.as_view(), name="login_url"),
    url(r'^register', Register_user.as_view(), name="register"),
    url(r'^dashboard/', HomePageView.as_view(), name="dashboard"),
    url(r'^logout/$', user_logout, name="logout_url"),
]
