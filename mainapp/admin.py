from django.contrib import admin
from mainapp.models import Vacancy, Documents

# Register your models here.

admin.site.register(Vacancy)


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'doc_file']
    list_filter = ['title']
