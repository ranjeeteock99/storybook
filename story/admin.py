from django.contrib import admin
from .models import Story,Category
# Register your models here.

#admin.site.register(Story)
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
 list_display=['name','slug']
 
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
 list_display=['title','publish']
 search_fields=['title']
 class Media:
     js=('tiny.js',)