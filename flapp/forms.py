from django import forms
from .models import Post, Comment
from pagedown.widgets import AdminPagedownWidget


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget())
	
	class Meta:
		model = Post
		fields = '__all__'

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)

  