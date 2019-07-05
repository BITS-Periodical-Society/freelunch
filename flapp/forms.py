from django import forms
from .models import Post, Comment, Subscriber
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())

	class Meta:
		model = Post
		fields = '__all__'
		exclude = ('published_date', 'created_date', 'slug',)
		help_texts = {
			'cover_image': 'Please upload a cover image.<br>Otherwise default image will be added to this article',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class': 'form-control'})
		self.fields['author'].widget.attrs.update({'class': 'form-control'})
		self.fields['synopsis'].widget.attrs.update({'class': 'form-control'})
		self.fields['post_editor'].widget.attrs.update({'class': 'form-control'})
		self.fields['section'].widget.attrs.update({'class': 'form-control'})
		self.fields['content'].widget.attrs.update({'class': 'form-control'})
		self.fields['cover_image'].widget.attrs.update({'class': 'form-control-file'})

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['author'].widget.attrs.update({'class': 'form-control'})
		self.fields['text'].widget.attrs.update({'class': 'form-control'})

class SubscribeForm(forms.ModelForm):

	class Meta:
		model = Subscriber
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control'})
		self.fields['email'].widget.attrs.update({'class': 'form-control'})