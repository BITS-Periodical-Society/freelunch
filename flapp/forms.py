from django import forms
from .models import Post, Comment
from pagedown.widgets import AdminPagedownWidget


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget(show_preview=False))

	class Meta:
		model = Post
		fields = '__all__'

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['author'].widget.attrs.update({'class': 'form-control'})
		self.fields['text'].widget.attrs.update({'class': 'form-control'})
  