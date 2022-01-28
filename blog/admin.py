from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created_on','updated_on','status')
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','content']
