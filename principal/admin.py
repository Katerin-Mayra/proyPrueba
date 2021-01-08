from django.contrib import admin
from .models import Profile


# Register your models here.
admin.site.register(Profile)


#configuraciondel panel de administrador
title = "Proyecto Django"
subtitle = "Panel de Gestion"

admin.site.site_header = title

admin.site.site_title = title
admin.site.index_title = subtitle