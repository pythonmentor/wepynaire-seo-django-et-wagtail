from django.contrib.sitemaps import Sitemap

from . import models


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
