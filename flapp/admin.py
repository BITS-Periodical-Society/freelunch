from django.contrib import admin
from .models import Post, Section, Writer, Editor, Developer, Subscriber


admin.site.register(Post)
admin.site.register(Writer)
admin.site.register(Editor)
admin.site.register(Developer)
admin.site.register(Section)
admin.site.register(Subscriber)