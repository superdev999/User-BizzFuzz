from django.contrib import admin
from user_bizz.models import Book

# class MyModelAdmin(admin.Admin):
#     actions = [export_csv, export_xls, export_xlsx]
# admin.site.register(Book, MyModelAdmin)
admin.site.register(Book)