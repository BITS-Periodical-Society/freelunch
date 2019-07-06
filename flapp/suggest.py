from .models import Post, Tag
from itertools import chain

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
	return suggestions

def suggest_by_editor(post):
	"""LEVEL 3 SEARCH"""
	editor = post.post_editor
	suggestions = Post.objects.filter(post_editor=editor)
	return suggestions

def recommend(post):
	__0 = suggest_by_tag(post)
	__1 = suggest_by_section(post)
	__2 = suggest_by_author(post)
	__3 = suggest_by_editor(post)
	__4 = Post.objects.all()
	result = list(chain(__0, __1, __2, __3, __4))
	seen = set()
	result =  [x for x in result if not (x in seen or seen.add(x))]
	return result