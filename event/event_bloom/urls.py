

from django.urls import path

from . import views

app_name='event_bloom'
urlpatterns = [
   path('',views.home,name='home'),
   path('story/',views.story,name='story'),

   path('storydetail/<int:id>',views.storydetail,name='storydetail'),
   path('gallery',views.gallery,name='gallery'),

   path('service/',views.service,name='service'),
   path('servicedetail/<int:id>',views.servicedetail,name='servicedetail'),

   path('destination/',views.dest,name='destination'),
   path('beach',views.beach,name='beach'),

   path('wedding/',views.wedding,name='wedding'),
   path('weddingdetail/<int:id>',views.weddingdetail,name='weddingdetail'),

   # path('booking/',views.booking,name='booking'),
   path('register/',views.register,name='register'),

   path('login/',views.user_login,name='login'),
   path('user_logout/', views.user_logout, name='user_logout'),

   path('add_to_event/<int:ev>',views.add_to_event,name='add_to_event'),
   path('event_view',views.event_view,name='event_view'),

   path('book_event',views.book_event,name='book_event'),
   path('status/<u>',views.payment_status,name='payment_status'),


]
