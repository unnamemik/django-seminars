from django.contrib import admin

from seminar2.models import *
from seminar3.models import Author, Post, Comment


@admin.action(description='Обнулить показы')
def reset_quant(modeladmin, request, queryset):
    queryset.update(showed=0)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'showed']
    ordering = ['-showed']
    search_fields = ['content']
    list_filter = ['showed']
    list_per_page = 5
    actions = [reset_quant]
    fieldsets = [
        ('Общие параметры',
         {'classes': ['wide'],
          'description': 'Тут общие параметры',
          'fields': ['title', 'author', 'content']}),
        ('Дополнительные параметры',
         {'classes': ['collapse'],
          'description': 'Тут общие параметры',
          'fields': ['showed', 'published']})
    ]


admin.site.register(HeadsTails)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
