from django.contrib import admin
from .models import Post, Writer, Editor, Developer, Subscriber, Founder, Comment
from .forms import PostForm


admin.site.register(Post)
admin.site.register(Founder)
admin.site.register(Writer)
admin.site.register(Editor)
admin.site.register(Developer)
admin.site.register(Subscriber)
admin.site.register(Comment)
