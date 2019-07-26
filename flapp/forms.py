from django import forms
from .models import Post, Subscriber, Tag
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
		self.fields['tag'].widget.attrs.update({'class': 'form-control'})
		self.fields['content'].widget.attrs.update({'class': 'form-control'})
		self.fields['cover_image'].widget.attrs.update({'class': 'form-control-file'})


class SubscribeForm(forms.ModelForm):

	class Meta:
		model = Subscriber
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control'})
		self.fields['email'].widget.attrs.update({'class': 'form-control'})


class TagForm(forms.ModelForm):

	class Meta(object):
		model = Tag
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control'})


def email_for_subscribers(self):
	subscribers = [s.email for s in Subscriber.objects.all()]
	from_email = settings.EMAIL_HOST_USER
	to_email = subscribers
	msg = f"{self.title}\nNew Post is uploaded."
	sub = "New Article"
	print("added")
	message = Mail(
		from_email=from_email,
		to_emails=to_email,
		subject=sub,
		html_content=msg)
	try:
		sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e)