from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.MyCustomUsers, UserAdmin)

admin.site.register(models.Sing)

admin.site.register(models.Contact)

admin.site.register(models.Log)

admin.site.register(models.FoundItem)

admin.site.register(models.LostItem1)

admin.site.register(models.PostNews)
 
admin.site.register(models.Category)

admin.site.register(models.Item)
admin.site.register(models.Bid)
admin.site.register(models.BiddingItem)