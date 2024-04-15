from django.urls import path, include
from Tea.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie_list/', movie_list),
    path('movie_detail/<int:movie_id>/', movie_detail),
    path('genres_list/', genres_list),
    path('genres_detail/<int:genres_id>/', genres_detail),
    path('director_list/', director_list),
    path('director_detail/<int:director_id>/', director_detail),
    path('actor_list/', actor_list),
    path('actor_detail/<int:actor_id>/', actor_detail),
    path('producer_list/', producer_list),
    path('producer_detail/<int:producer_id>/', producer_detail),

]
