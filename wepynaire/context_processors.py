from django.contrib.sites.models import Site


def site_url(request):
    current_site = Site.objects.get_current()
    return {
        "SITE_URL": f"https://{current_site.domain}",
    }
