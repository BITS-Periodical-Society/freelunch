from .models import Post, Tag


def suggest_by_tag(post):
	"""LEVEL 0 SEARCH"""
	tags = post.tag.all()
	suggestions = Post.objects.filter(tag__in=tags)
	return suggestions

def suggest_by_section(post):
	"""LEVEL 1 SEARCH"""
	section = post.section
	suggestions = Post.objects.filter(section=section)
	return suggestions

def suggest_by_author(post):
	"""LEVEL 2 SEARCH"""
	authors = post.author.all()
	suggestions = Post.objects.filter(author__in=authors)

def suggest_by_editor(post):
	"""LEVEL 3 SEARCH"""
	editor = post.post_editor
	suggestions = Post.objects.filter(post_editor=editor)
	return suggestions

def recommend(post):

	try:
		result = suggest_by_tag(post)
	except:
		pass
	try:
		result = result | suggest_by_section(post)
	except:
		pass
	try:
		result = result | suggest_by_author(post)
	except:
		pass
	try:
		result = result | suggest_by_editor(post)
	except:
		pass
	try:
		result = result | Post.objects.all()
	except:
		pass

	return result.distinct()