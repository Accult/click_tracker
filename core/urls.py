from django.urls import path
from core.views import StartPageView, HiTherePageView

urlpatterns = [
    path("", StartPageView.as_view(), name="start_page"),
    path("hi_there/", HiTherePageView.as_view(), name="hi_there"),
]
