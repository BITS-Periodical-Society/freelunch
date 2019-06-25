from django.contrib import admin
from .models import Post, Writer, Editor, Developer, Subscriber, Comment
from .forms import PostForm

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
	form = PostForm

	class Meta:
		fields = '__all__'


admin.site.register(Writer)
admin.site.register(Editor)
admin.site.register(Developer)
admin.site.register(Subscriber)
admin.site.register(Comment)
