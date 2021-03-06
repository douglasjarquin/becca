from django.conf.urls.defaults import *
from models import Entry, Tag

entry_dict = {
	'queryset': Entry.objects.filter(is_draft=False),
	'date_field': 'published_on',
}

tag_dict = {
	'queryset': Tag.objects.all(),
}

urlpatterns = patterns('django.views.generic',
	(r'^/?$', 'date_based.archive_index', entry_dict),
	(r'^(?P<year>\d{4})/$', 'date_based.archive_year', entry_dict),
	(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'date_based.archive_month', dict(entry_dict, month_format='%m')),
	(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'date_based.archive_day', dict(entry_dict, month_format='%m')),
	(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[0-9A-Za-z-]+)/$', 'date_based.object_detail', dict(entry_dict, slug_field='slug', month_format='%m')),
	(r'^tag/(?P<slug>[0-9A-Za-z-]+)/$', 'list_detail.object_detail', dict(tag_dict, slug_field='slug')),
)

