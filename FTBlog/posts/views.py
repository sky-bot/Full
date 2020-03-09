from django.shortcuts import render
from rest_framework.views import APIView


from rest_framework.response import Response


class posts(APIView):
    pass
    
def index(request):
    return render(request, 'index.html')