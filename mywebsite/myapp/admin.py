# from turtle import title
from django.contrib import admin
from .models import Post, Category
# Register your models here.

# we are making sure that our slug field is been prepopulated when ever we are typing in our title field in our admin panel
class PostAdmin(admin.ModelAdmin):
    # {'slug' : (title)}  since we are filling our title field
    # ===> when ever we are filling out out title the slug field should get updated
    prepopulated_fields = {'slug' : ["title"]}
    
    
class CategoryAdmin(admin.ModelAdmin):
    # {'slug' : (title)}  since we are filling our title field
    # ===> when ever we are filling out out title the slug field should get updated
    prepopulated_fields = {'slug' : ["title"]}
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)