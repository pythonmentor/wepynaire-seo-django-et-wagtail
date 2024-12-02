from django.shortcuts import render, get_object_or_404

from .models import Category
from ..blog.models import Article


def index(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    return render(
        request,
        "categories/index.html",
        {"category": category, "articles": articles},
    )
