from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("service/", views.service, name='service'),
    path("menu/", views.menu, name='menu'),
    path("booking/", views.booking, name='booking'),
    path("our team/", views.team, name='team'),
    path("testimonial/", views.testimonial, name='testimonial'),
    path("contact/", views.contact, name='contact'),
]


