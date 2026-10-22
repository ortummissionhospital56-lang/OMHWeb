from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contact, name="contact"),
    path("careers/", views.careers, name="careers"),
    path("news/", views.news_list, name="news"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("downloads/", views.downloads, name="downloads"),
    path("feedback/", views.feedback, name="feedback"),
]
