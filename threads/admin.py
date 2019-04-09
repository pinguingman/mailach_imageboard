from django.contrib import admin

from .models import Thread, Message, Section

admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Section)
