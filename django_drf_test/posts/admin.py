from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    model = Post
    list_display = ('id', 'owner', 'text', 'tag', )
    readonly_fields = ('id',)


admin.site.register(Post, PostAdmin)

