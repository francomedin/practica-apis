from django.contrib import admin

from .models import Person, Hobby, Reunion


class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name')


admin.site.register(Person, PersonAdmin)
admin.site.register(Hobby)
admin.site.register(Reunion)
