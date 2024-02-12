from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.


def say_hello(request):
    return HttpResponse("<h1>Hello Fleur</h1>")

def get_profile(req):
    user_profile = {
        "name" : "Sylvia Mwitumi",
        "email": "sylvia.mwitumi@meltwater.org",
        "phone number" : "0700042818"
    }
    return JsonResponse(user_profile)

def filter_queries(request, query_id):
    # query = get_object_or_404(Query, id=query_id)

    data = {
        "id": query_id,
        "name": "Sylvia Mwitumi",
        "description": "EIT",
        "status": "Training",
        "submitted_by": "Lucy",
    }
    return JsonResponse(data),

class QueryView(View):
   
    queries = [
            {"id": 1, "title": "Adama declined Val shote"},
            {"id":2, "title": "Samson declined Val shots"}]
            
    def get(self, request):
             
        return JsonResponse({"results": self.queries})