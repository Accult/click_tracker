from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from core.models import UserData


class StartPageView(View):
    template_name = "start_page.html"

    def post(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT")

        UserData.objects.create(ip=ip_address, browser=user_agent)

        return redirect("hi_there")

    def get(self, request, *args, **kwargs):
        return render(request, "start_page.html")


class HiTherePageView(TemplateView):
    template_name = "hi_there_page.html"
