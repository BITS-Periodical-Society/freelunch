from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatewords
from markdown_deux import markdown

Section = [
	('EF', 'Economics & Finance'),
	('E', 'Editorial'),
	('ST', 'Science & Technology'),
	('WA', 'World Affairs'),
]

Developer_Designation = [
	('D', 'Developer'),
	('HD', 'Head of Web Development'),
]

Writer_Designation = [
    ('A', 'Author'),
    ('GA', 'Guest Author'),
    ('FO', 'Founder')
]

Editor_Designation = [
	('EC', 'Editor-in-Chief'),
	('STE', 'Section Editor: Science & Technology Editor'),
	('EFE', 'Section Editor: Economics & Finance Editor'),
	('WAE', 'Section Editor: World Affairs Editor'),
	('EE', 'Section Editor: Editorial Editor'),
]


class Post(models.Model):
	author = models.ManyToManyField('Writer', blank=False)
	post_editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	synopsis = models.CharField(max_length=640, blank=True)
	content = models.TextField()
	section = models.CharField(max_length=2, choices=Section)
	tag = models.ManyToManyField('Tag', blank=True)
	created_date = models.DateTimeField(default=timezone.now)
	cover_image = models.ImageField(editable=True, upload_to = 'post_cover/', default='default_cover.jpeg')
	published_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=150, unique=True, blank=True)

	class Meta:
		ordering = ('-published_date',)

	def get_markdown(self):
		content = self.content
		return mark_safe(markdown(content))

	def get_synopsis(self):
		if self.synopsis == "":
			s = self.content.split("\n")
			while (s[0][0:2] == '![' or s[0] == '\r'):
				s.pop(0)
			s = s[0]
			return s
		else:
			return self.synopsis

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def delete_img(self, *args, **kwargs):
		storage, path = self.cover_image.storage, self.cover_image.path
		super(ImageModel, self).delete(*args, **kwargs)
		storage.delete(path)

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug': self.slug})

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Tag(models.Model):
	name = models.CharField(max_length=20, unique=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


class Developer(models.Model):
	name = models.CharField(max_length=30)
	pic = models.ImageField(upload_to='developer/', default='default.png')
	designation = models.CharField(max_length=2, choices=Developer_Designation, default=Developer_Designation[0][0])
	github_url = models.URLField(blank=True)
	linkedin_url = models.URLField(blank=True)
	email = models.EmailField(blank=True)
	bio = models.CharField(max_length=600)
	slug = models.SlugField(max_length=30, unique=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Developer, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('developer_info', kwargs={'slug': self.slug})


class Editor(models.Model):
	name = models.CharField(max_length=30)
	pic = models.ImageField(upload_to='editor/', default='default.png')
	designation = models.CharField(max_length=3, choices=Editor_Designation, default=Editor_Designation[0][0])
	linkedin_url = models.URLField(blank=True)
	email = models.EmailField(blank=True)
	bio = models.CharField(max_length=600)
	edited_posts = models.ManyToManyField(Post, blank=True)
	slug = models.SlugField(max_length=30, unique=True, blank=True)

	class Meta:
		ordering = ('name',)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Editor, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('editor_info', kwargs={'slug': self.slug})


class Writer(models.Model):
	name = models.CharField(max_length=30)
	pic = models.ImageField(upload_to='author/', default='default.png')
	designation = models.CharField(max_length=2, choices=Writer_Designation, default=Writer_Designation[0][0])
	linkedin_url = models.URLField(blank=True)
	email = models.EmailField(blank=True)
	bio = models.CharField(max_length=600)
	posts = models.ManyToManyField(Post, blank=True)
	slug = models.SlugField(max_length=30, unique=True, blank=True)

	class Meta:
		ordering = ('name',)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Writer, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('writer_info', kwargs={'slug': self.slug})


class Subscriber(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()

    def __str__(self):
        return self.name
