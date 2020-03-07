from django.shortcuts import render
from rest_framework.views import APIView


from rest_framework.response import Response

# Create your views here.

# client_id
# 634927901266-mth9mku4id3ie7ic762fokovcakp98as.apps.googleusercontent.com

# client_secret
# 5snJH5yxfeMejCOUJyIRssbP

class posts(APIView):
    pass
    
def index(request):
    return render(request, 'index.html')