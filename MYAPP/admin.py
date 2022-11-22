from django.contrib import admin
from MYAPP.models import APP


# Register your models here.
class DataAdmin(admin.ModelAdmin):
    LIST=('ID','FIRST_NAME','LAST_NAME','EMAIL','NUMBER','AGE','GENDER')

admin.site.register(APP,DataAdmin)

def _str_(self):
    return self.admin
