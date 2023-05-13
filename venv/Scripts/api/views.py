from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def API(request):
    return Response("안녕하세요 HomeTi에 오신것을 환영합니다.")
