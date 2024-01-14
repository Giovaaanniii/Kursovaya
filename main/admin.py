from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','short_disc', 'brief_info','image_preview')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_filter = ['id','cena']
    ordering = ['time_create' ,'time_update', 'id']
    readonly_fields = ['image_preview']


        
    def short_disc(self, obj):
        return obj.short_task
    short_disc.short_discription = 'Краткое описание'
    

    @admin.display(description="Краткое описание")
    def brief_info(self, women: open):
        return f"Описание {len(women.task)} символов."



class CategoryContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','short_disc', 'brief_info','image_preview')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_filter = ['id']
    ordering = ['id']
    readonly_fields = ['image_preview']

        
    def short_disc(self, obj):
        return obj.short_task
    short_disc.short_discription = 'Краткое описание'
    

    @admin.display(description="Краткое описание")
    def brief_info(self, women: open):
        return f"Описание {len(women.task)} символов."



admin.site.register(Task,CategoryAdmin)
admin.site.register(Graduation,CategoryAdmin)
admin.site.register(Events,CategoryAdmin)
admin.site.register(Excursions,CategoryAdmin)
admin.site.register(Master,CategoryAdmin)
admin.site.register(Contacts,CategoryContactsAdmin)

