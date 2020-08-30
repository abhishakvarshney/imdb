import os
import json
import ast

from django.core.exceptions import PermissionDenied, RequestAborted
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_method
from django.contrib.auth import logout as logout_method

from movie import models
from rest_framework.decorators import api_view, parser_classes
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from utility.log import log
from .forms import UploadJSONFileForm


def login(request):
    msg = []
    if request.user.is_authenticated:
        redirect_url = u'/'
        return redirect(redirect_url)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_method(request, user)
            user_id = request.user.id
            request.session['authenticated'] = True
            request.session['user_id'] = user_id
            request.session['username'] = username
            redirect_url = u'/'
            return HttpResponseRedirect(reverse('movie:view'))
        else:
            log.info("Login failed for ->{}".format(username))
            msg = {'msg': 'Login failed. Authentication error. Please try again.'}
    return render(request, "login_new.html", {'msg': msg})


def logout(request):
    logout_method(request)
    return HttpResponseRedirect(reverse('movie:login'))


@parser_classes([JSONParser, MultiPartParser, FormParser])
def view_movie(request):
    try:
        perm = request.user.has_perm('movie.add_movies') and request.user.has_perm('movie.change_movies') and request.user.has_perm('movie.delete_movies')
        user_active = request.user.is_authenticated
        if request.method == "GET":
            movie_list = models.Movies.view_movie()
            return render(request, "view_movies.html", {'movie_list': movie_list, 'range': range(1, len(movie_list)), 'perm':perm, 'user_active':user_active})
    except Exception as ex:
        raise RequestAborted


@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_movie(request):
    if request.user.has_perm('movie.add_movies'):
        try:
            if request.method == "POST":
                form = UploadJSONFileForm(request.POST, request.FILES)
                json_data = []
                if form.is_valid():
                    file = request.FILES['file']
                    json_data = file.read()
                    json_data = json.loads(json_data)
                    for movie_data in json_data:
                        movie = models.Movies.add_movie(**movie_data)
                return HttpResponseRedirect(reverse('movie:view'))
            form = UploadJSONFileForm()
            return render(request, "add_movies.html", {'form': form})
        except Exception as ex:
            raise RequestAborted
    else:
        raise PermissionDenied()


@parser_classes([JSONParser, MultiPartParser, FormParser])
def update_movie(request, data):
    if request.user.has_perm('movie.change_movies'):
        try:
            if request.method == "GET":
                data = ast.literal_eval(data)
                if len(request.GET) > 0:
                    movie_data = request.GET
                    movie_data._mutable = True
                    if movie_data.get('name') in  ['', None]:
                        movie_data['name'] = data.get('name', '')
                    if movie_data.get('director') in ['', None]:
                        movie_data['director'] = data.get('director', '')
                    if movie_data.get('imdb_score') in ['', None]:
                        movie_data['imdb_score'] = data.get('imdb_score', '')
                    if movie_data.get('popularity') in ['', None]:
                        movie_data['popularity'] = data.get('popularity', '')
                    if movie_data.get('genre') in ['', None]:
                        movie_data['genre'] = data.get('genre', '')
                    movie_update = models.Movies.update_movies(movie_data)
                if isinstance(data, dict):
                    data = [data]
                return render(request, "update_movies.html", {'movie_list': data})
        except Exception as ex:
            raise RequestAborted
    else:
        raise PermissionDenied()


@parser_classes([JSONParser, MultiPartParser, FormParser])
def delete_movie(request, movie_name):
    if request.user.has_perm('movie.delete_movies'):
        try:
            if movie_name is not None:
                is_deleted = models.Movies.delete_movies(movie_name)
            if is_deleted:
                return HttpResponseRedirect(reverse('movie:view'))
            return HttpResponseRedirect(reverse('movie:view'))
        except Exception as ex:
            raise RequestAborted
    else:
        raise PermissionDenied()



@parser_classes([JSONParser, MultiPartParser, FormParser])
def search_movie(request):
    try:
        perm = request.user.has_perm('movie.add_movies') and request.user.has_perm('movie.change_movies') and request.user.has_perm('movie.delete_movies')
        user_active = request.user.is_authenticated
        movie_name = request.GET.get('q', '')
        movie_list = models.Movies.search_movie(movie_name)
        return render(request, "view_movies.html", {'movie_list': movie_list, 'range': range(1, len(movie_list)), 'perm':perm, 'user_active':user_active})
    except Exception as ex:
        raise RequestAborted
