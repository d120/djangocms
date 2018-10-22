from django.conf import settings

def d120_context_processor(request):
    keys = {
        'site_url': settings.SITE_URL,
        'blog_url': settings.BLOG_URL,
        'forum_url': settings.FORUM_URL,
    }

    return keys
