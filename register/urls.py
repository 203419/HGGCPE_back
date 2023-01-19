
from django.urls import re_path

from register.views import UserRegister, RegisterViewNew

urlpatterns = [
    re_path(r'^v1/register', UserRegister.as_view()),
    re_path(r'^v2/register', RegisterViewNew.as_view())
]