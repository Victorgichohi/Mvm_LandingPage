# Register your models here.
from django.contrib import admin
from .models import SignUp

# this allows us to manipulate what we see in the admin section
class SignUpAdmin(admin.ModelAdmin):
    list_display= ["__str__", "timestamp","updated"]
    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)
