from django.contrib import admin
from .models import UserProfile,UserPost,Interest

# Register your models here.
#class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user','phone_number','dob')#these fields will be displayed there inside userprofile
    #list_filter = ('user','phone_number')#filter can be done using these fields
   # search_fields = ('user__username','user__first_name','user__last_name','dob','bio')#these fields are used in search bars to search
   # readonly_fields = ('image',)#these field ca only view cant edit
    #fieldsets =(('User info',{'fields':('user','bio')}),
#  ('More info', {'fields': ('phone_number', 'dob','image')}),)#these fields display inside list display

admin.site.register(UserProfile)
admin.site.register(UserPost)
admin.site.register(Interest)