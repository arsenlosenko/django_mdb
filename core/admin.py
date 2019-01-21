from django.contrib import admin
from core.models import Movie, Person, Role, MovieImage

# Register your models here.

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(MovieImage)
