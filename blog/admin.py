from django.contrib import admin
from blog.models import Tag, Post, Comment
# Register your models here.
admin.site.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'published_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)