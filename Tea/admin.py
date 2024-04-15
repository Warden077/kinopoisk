from django.contrib import admin
from .models import Movie
from .models import MoviePerson
from .models import Genre
from .models import MovieReview


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'rating',
    )
@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'birth_date',
        'photo',
        'role',
    )
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=(
        'name',
    )
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display=(
        'author',
        'movie',
        'likes',
        'created_at',
    )