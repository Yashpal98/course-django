from django.contrib import admin

# Register your models here.
from .models import Document, Student, Python, C, Html, Java, Javascript, Css, Django

admin.site.register(Document)
admin.site.register(Student)
admin.site.register(Python)
admin.site.register(C)
admin.site.register(Css)
admin.site.register(Html)
admin.site.register(Java)
admin.site.register(Javascript)
admin.site.register(Django)