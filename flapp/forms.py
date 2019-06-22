from django import forms
from django.contrib.flatpages.models import FlatPage
from .models import Post
from tinymce.widgets import TinyMCE

class FlatPageForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

	class Meta:
		model = FlatPage


class PostForm(forms.ModelForm):
	content = forms.CharField(
		widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
	)

	class Meta:
		model = Post
		fields = ('title', 'text', 'content',)