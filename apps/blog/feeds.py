import datetime
from django.contrib.syndication.feeds import Feed
from models import Entry

class BlogEntryFeed(Feed):
	title = "A Becca Blog"
	link = "http://www.douglasjarquin.com/becca/"
	description = "The blog next door"

	def items(self):
		return Entry.objects.filter(is_draft=False, published_on__lte=datetime.datetime.now())[:10]