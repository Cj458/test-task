from django.contrib import admin
from .models import Worker, Store, Visit
# Register your models here.


class WorkerModelAdmin(admin.ModelAdmin):
   list_display = ('name',  'number')
   search_fields=('name', '')
   list_per_page = 1
        
        
class StoreModelAdmin(admin.ModelAdmin):
   list_display = ('title',  'worker', 'create_at')
   search_fields=('title', 'worker__name')
   list_per_page = 1

admin.site.register(Worker, WorkerModelAdmin)
admin.site.register(Store, StoreModelAdmin)
admin.site.register(Visit)