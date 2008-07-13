from django.template import Library, Node
from apps.blog.models import Tag, Entry

register = Library()

def build_tag_list(parser, token):
	"""
	{% get_tag_list %}
	"""
	return TagMenuObject()

class TagMenuObject(Node):
	def render(self, context):
		output = ['']

		for blogtag in Tag.objects.all():
			number = blogtag.entry_set.count()
			if number >= 1:
				output.append(blogtag)

		context['blog_tags'] = output
		return ''

register.tag('get_tag_list', build_tag_list)