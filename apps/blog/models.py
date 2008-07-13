from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

class Tag(models.Model):
	name = models.CharField(maxlength=50, core=True)
	slug = models.SlugField(editable=False)

	class Admin:
		pass

	def __str__(self):
		return self.name

	def save(self):
		if not self.id:
			self.slug = slugify(self.name)
		super(Tag, self).save()

	def get_absolute_url(self):
		return '/blog/tag/%s/' % (self.slug)

	def get_active_entries(self):
		return self.entry_set.all().filter(is_draft=False)

class Entry(models.Model):
	title = models.CharField(maxlength=200)
	slug = models.SlugField(editable=False)
	summary = models.CharField(maxlength=200, help_text="One sentence.")
	body = models.TextField(help_text="Use HTML.")
	tags = models.ManyToManyField(Tag, filter_interface=models.HORIZONTAL)
	author = models.ForeignKey(User)
	is_draft = models.BooleanField("Draft", default=False, help_text="Check if this is a draft.")
	is_comments = models.BooleanField("Comments", default=True, help_text="Check to enable comments.")
	published_on = models.DateTimeField()
	modified_on = models.DateTimeField(editable=False)

	class Admin:
		fields = (
			(None, {'fields': ('title', 'summary', 'is_draft', 'body', 'tags', 'author', 'is_comments')}),
			('Date', {'fields': ('published_on',)}),
		)
		list_display = ('title', 'author', 'is_draft', 'published_on', 'is_comments')
		search_fields = ['title', 'summary', 'body']

	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ('-published_on',)
		get_latest_by = 'published_on'

	def __str__(self):
		return self.title

	def save(self):
		if not self.id:
			self.slug = slugify(self.title)
		self.modified_on = datetime.datetime.now()
		super(Entry, self).save()

	def get_absolute_url(self):
		return '/blog/%s/%s/' % (self.published_on.strftime('%Y/%m/%d').lower(), self.slug)
		
	def get_author_name(self):
		return self.author.first_name
		
	def get_comments_form(self): 
		return self.is_comments and datetime.datetime.today() - datetime.timedelta(30) <= self.published_on		