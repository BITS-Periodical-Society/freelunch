from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

CATEGORY = [
    ('ST', 'Science & Technology'),
    ('EF', 'Economics & Finance'),
    ('WA', 'World Affairs'),
    ('E', 'Editorial'),
    ('BR', 'Book Review'),
]

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    synopsis = models.TextField(blank=False)
    text = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('-published_date',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
