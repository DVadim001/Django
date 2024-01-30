from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about-us', views.about),
    path('contact-us', views.contacts),
    path('search', views.search_article),
    path('article-news', views.article),
    path('article-not-found', views.article_not_found),


]
