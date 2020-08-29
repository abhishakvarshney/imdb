import sys
sys.path.append("..")
import os
import ast
import uuid
import json
from django.db import models
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU
from django.http import JsonResponse
from django.core import serializers


# Create your models here.
__all__ = ["Movies"]

GENDER_MALE = "Male"
GENDER_FEMALE = "Female"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
)


class Movies(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """
        db_table = "Movies"

    movie_id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    imdb_score = models.TextField(null=True, blank=True)
    popularity = models.TextField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}".format(self.realname)

    @staticmethod
    def view_movie():
        """
        @return:
        """
        response_dict = Movies.objects.filter(isActive=True)
        data_list = []
        for data in response_dict:
            movie_data = {}
            movie_data['name'] = data.name
            movie_data['director'] = data.director
            movie_data['imdb_score'] = data.imdb_score
            movie_data['popularity'] = data.popularity
            if isinstance(data.genre, str):
                try:
                    movie_data['genre'] = ', '.join(ast.literal_eval(data.genre))
                except:
                    movie_data['genre'] = data.genre
            else:
                movie_data['genre'] = ', '.join(data.genre)
            data_list.append(movie_data)
        return data_list

    @classmethod
    def add_movie(cls, **data):
        """

        @param data:
        @return:
        """
        movies = cls.objects.create(
        name = data.get("name", ""),
        director = data.get("director", ""),
        imdb_score = data.get("imdb_score", ""),
        popularity = data.get('99popularity', ''),
        genre = data.get('genre', ''))
        return True

    @staticmethod
    def delete_movies(movie_name):
        """

        @param movie_name:
        @return:
        """
        movies_data = Movies.objects.filter(name=movie_name, isActive=True)
        count=0
        for movie in movies_data:
            if count == 0:
                movie.isActive = False
                movie.save()
                count+=1
        return True

    @staticmethod
    def update_movies(data):
        """

        @param movie_data:
        @return:
        """
        movies_data = Movies.objects.filter(name=data.get('name'), isActive=True)
        for movie_data in movies_data:
            movie_data.name = data.get('name', movie_data.name)
            movie_data.director = data.get('director', movie_data.director)
            movie_data.imdb_score = data.get('imdb_score', movie_data.imdb_score)
            movie_data.popularity = data.get('popularity', movie_data.popularity)
            movie_data.genre = data.get('genre', movie_data.genre)
            movie_data.save()
        return True

    @staticmethod
    def search_movie(movie_name):
        """

        @param movie_data:
        @return:
        """
        response_dict = Movies.objects.filter(name__contains=movie_name, isActive=True)
        data_list = []
        for data in response_dict:
            movie_data = {}
            movie_data['name'] = data.name
            movie_data['director'] = data.director
            movie_data['imdb_score'] = data.imdb_score
            movie_data['popularity'] = data.popularity
            if isinstance(data.genre, str):
                try:
                    movie_data['genre'] = ', '.join(ast.literal_eval(data.genre))
                except:
                    movie_data['genre'] = data.genre
            else:
                movie_data['genre'] = ', '.join(data.genre)
            data_list.append(movie_data)
        return data_list



# class Users(models.Model):
#     """
#     @return:
#     """

#     class Meta:
#         """
#         @return:
#         """
#         db_table = "User"

#     user_id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.TextField(null=True, blank=True)
#     isActive = models.BooleanField(default=True)
#     gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Male")
#     createdOn = models.DateTimeField(auto_now_add=True)
#     updatedOn = models.DateTimeField(auto_now=True)
    