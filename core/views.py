import requests
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from core.models import UserData, RedirectData


class StartPageView(View):
    template_name = "start_page.html"

    def post(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT")

        UserData.objects.create(ip=ip_address, browser=user_agent)

        last_redirect = RedirectData.objects.last()
        if last_redirect:
            return redirect(last_redirect.url)
        else:
            return redirect("hi_there")

    def get(self, request, *args, **kwargs):
        return render(request, "start_page.html")


class HiTherePageView(TemplateView):
    template_name = "hi_there_page.html"
    api_url = "https://api.api-ninjas.com/v1/quotes?category=life"
    api_key = "13Tk+3CNA6xWEgzTjJhK1A==smXxx6lYODJKCD8p"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = {"X-Api-Key": self.api_key}
        response = requests.get(self.api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            quotes = response.json()
            if quotes:
                quote = quotes[0]
                context["quote"] = quote["quote"]
                context["author"] = quote["author"]
        return context
