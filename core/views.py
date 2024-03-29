import requests
from django.shortcuts import redirect
from django.views.generic import TemplateView
from core.models import UserData, RedirectData
from click_tracker.settings import API_KEY


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def post(self, request, *args, **kwargs):
        ip_address = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT")

        UserData.objects.create(ip=ip_address, browser=user_agent)

        last_redirect = RedirectData.objects.last()
        redirect_link = last_redirect.url if last_redirect else "hi_there"
        return redirect(redirect_link)


class HiTherePageView(TemplateView):
    template_name = "hi_there_page.html"
    api_url = "https://api.api-ninjas.com/v1/quotes?category=life"
    api_key = API_KEY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = {"X-Api-Key": self.api_key}
        response = requests.get(self.api_url, headers=headers)
        if response.ok:
            quotes = response.json()
            if quotes:
                quote = quotes[0]
                context["quote"] = quote["quote"]
                context["author"] = quote["author"]
        return context
