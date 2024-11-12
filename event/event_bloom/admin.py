from django.contrib import admin
from .models import Story, Service, Inform, Wedding, Weddingdetail, Booking, Event, Book_event, Payment

# Register your models here.
admin.site.register(Story)
admin.site.register(Service)
admin.site.register(Inform)
admin.site.register(Wedding)
admin.site.register(Weddingdetail)
# admin.site.register(Booking)
admin.site.register(Event)
admin.site.register(Book_event)
admin.site.register(Payment)
