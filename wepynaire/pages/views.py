from django.shortcuts import render
from django.views.generic import TemplateView

from ..blog import models as articles_models


def home(request):
    articles = articles_models.Article.objects.all()
    return render(
        request,
        "pages/home.html",
        {
            "articles": articles,
        },
    )


def about(request):
    return render(request, "pages/about.html")


class RobotsView(TemplateView):
    content_type = "text/plain"
    template_name = "robots.txt"
