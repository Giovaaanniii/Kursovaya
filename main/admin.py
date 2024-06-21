from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .resources import ContactsResource
from .models import Task, Graduation, Events, Excursions, Master, Contacts
from import_export.admin import ImportExportModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_disc', 'brief_info', 'image_preview',)
    list_display_links = ('id', 'title')
    search_fields = ['id', 'title']
    ordering = ['id']
    readonly_fields = ['image_preview']

    def short_disc(self, obj):
        return obj.short_task
    short_disc.short_description = 'Краткое описание'

    @admin.display(description="Краткое описание")
    def brief_info(self, women: open):
        return f"Описание {len(women.task)} символов."



@admin.register(Contacts)
class ContactsAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    resource_class = ContactsResource
    list_display = ('id', 'title', 'short_disc', 'brief_info')
    list_display_links = ('id', 'title')
    search_fields = ['id', 'title']
    ordering = ['id']

    def short_disc(self, obj):
        return obj.short_task
    short_disc.short_description = 'Краткое описание'

    @admin.display(description='Краткое описание')
    def brief_info(self, obj):
        return f'Описание: {len(obj.task)} символов.'

# Удалите эту строку, поскольку модель уже зарегистрирована выше
# admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Task, CategoryAdmin)
admin.site.register(Graduation, CategoryAdmin)
admin.site.register(Events, CategoryAdmin)  
admin.site.register(Excursions, CategoryAdmin)
admin.site.register(Master, CategoryAdmin)
