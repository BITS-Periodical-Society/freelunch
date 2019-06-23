from django import forms
from .models import Post
from pagedown.widgets import AdminPagedownWidget


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = Post
		fields = '__all__'