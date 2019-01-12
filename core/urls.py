from django.urls import path

from core.views import (MovieListView, MovieDetailView,
                        PersonDetailView, PersonListView,
                        CreateVoteView, UpdateVoteView, MovieUploadImageView)

app_name = 'core'

urlpatterns = [
    path('movies',
         MovieListView.as_view(),
         name='movie-list'),

    path('movies/<int:pk>',
         MovieDetailView.as_view(),
         name='movie-detail'),

    path('movies/<int:movie_id>/image/upload',
         MovieUploadImageView.as_view(),
         name='movie-image-upload'),

    path('movies/<int:movie_id>/vote',
         CreateVoteView.as_view(),
         name='create-vote'),

    path('movies/<int:movie_id>/vote/<int:pk>',
         UpdateVoteView.as_view(),
         name='update-vote'),

    path('people',
         PersonListView.as_view(),
         name='person-list'),

    path('people/<int:pk>',
         PersonDetailView.as_view(),
         name='person-detail'),
]
