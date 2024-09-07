from django.urls import path
from webpage.views import about, service, index, menu, booking, team, testimonial, contact

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("service/", service, name='service'),
    path("menu/", menu, name='menu'),
    path("booking/", booking, name='booking'),
    path("our team/", team, name='team'),
    path("testimonial/", testimonial, name='testimonial'),
    path("contact/", contact, name='contact'),
]
