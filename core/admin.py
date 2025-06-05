from django.contrib import admin
from django.contrib import admin
from .models import Education, Experience, Project, Skill, About, ContactMessage

# Register your models here.

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(About)
admin.site.register(ContactMessage)
