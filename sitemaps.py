from django.contrib.sitemaps import Sitemap
from apps.blog.models import Entry
import datetime

class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.4

    def items(self):
        return Entry.objects.filter(is_draft=False, published_on__lte=datetime.datetime.now())

    # lastmod is not implemented, because the blog contains comments.
    # We'd rather not look up the date of the latest comment -- not worth the overhead.