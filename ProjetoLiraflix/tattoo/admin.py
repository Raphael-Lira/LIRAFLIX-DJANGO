from django.contrib import admin
from .models import Tattoo, Episodio
# Register your models here.
# É aqui que registramos aplicativos nos admins
admin.site.register(Tattoo)
admin.site.register(Episodio)