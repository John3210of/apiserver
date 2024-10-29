# apiserver/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class APIServerView(APIView):
    def get(self, request):
        return Response("I'm apiserver")
