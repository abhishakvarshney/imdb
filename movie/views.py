import os
import json
import ast
import base64

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_method
from django.contrib.auth import logout as logout_method

from movie import models
from rest_framework.decorators import api_view, parser_classes
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU
from .validator import *
from .forms import UploadJSONFileForm
from django.core.files.storage import FileSystemStorage


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
            return HttpResponseRedirect(redirect_url)
        else:
            print("Login failed for ->", username)
            msg = {'msg': 'Login failed. Authentication error. Please try again.'}

    return render(request, "login_new.html", {'msg': msg})

def logout(request):
    logout_method(request)
    # return redirect(reverse('login') + request.GET.get('next', ''))



# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def view_movie(request):
    if request.method == "GET":
        movie_list = models.Movies.view_movie()
        return render(request, "view_movies.html", {'movie_list': movie_list, 'range': range(1, len(movie_list))})


@parser_classes([JSONParser, MultiPartParser, FormParser])
# @permission_required('auth.admin')
def add_movie(request):
    if request.method == "POST":
        form = UploadJSONFileForm(request.POST, request.FILES)
        json_data = []
        if form.is_valid():
            file = request.FILES['file']
            json_data = file.read()
            json_data = json.loads(json_data)
            for movie_data in json_data:
                movie = models.Movies.add_movie(**movie_data)
    form = UploadJSONFileForm()
    return render(request, "add_movies.html", {'form': form})


# @api_view(["GET"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
# @permission_required('auth.admin')
def update_movie(request, data):
    if request.method == "GET":
        # data = json.loads(request.body.decode("utf-8"))
        data = ast.literal_eval(data)
        movie_update = models.Movies.update_movies(data)
        print("get movie_activity response = " + str(data), type(data))
        if isinstance(data, dict):
            data = [data]
        return render(request, "update_movies.html", {'movie_list': data})


# @api_view(["POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
# @permission_required('auth.admin')
def delete_movie(request, movie_name):
    # data = json.loads(request.body.decode("utf-8"))
    # validate_request, error_msg = validate_add_movie_activity(request)
    # if not validate_request:
        # log.error(error_msg)
        # return JsonResponse(error_msg)
    # movie_name = data.get('name')
    if movie_name is not None:
        is_deleted = models.Movies.delete_movies(movie_name)
    if is_deleted:
        return HttpResponseRedirect(reverse('movie:view'))
    return HttpResponseRedirect(reverse('movie:view'))


# @parser_classes([JSONParser, MultiPartParser, FormParser])
# def search_movie(request, movie_name):
    # movie_list = models.Movies.search_movie(movie_name)
    # return render(request, "view_movies.html", {'movie_list': movie_list, 'range': range(1, len(movie_list))})