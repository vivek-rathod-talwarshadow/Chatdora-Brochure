from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('chat/', views.chat_redirect, name='chat'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_use, name='terms_of_use'),
    path(
        'demo-websites/restaurant/',
        views.demo_placeholder,
        {"demo_name": "Restaurant Website"},
        name='demo_website_restaurant_1',
    ),
    path(
        'demo-websites/real-estate/',
        views.demo_placeholder,
        {"demo_name": "Real Estate Website"},
        name='demo_website_realstate_1',
    ),
    path(
        'demo-websites/gym/',
        views.demo_placeholder,
        {"demo_name": "Gym Website"},
        name='demo_website_gym_1',
    ),
]
