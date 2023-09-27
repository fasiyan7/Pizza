import json
from django.http import HttpResponse, JsonResponse
from .models import Pizza
def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        content={
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,   
        }
    #return JsonResponse(content)
    #beelow code ffor maintaining indentation
        json_data = json.dumps(content, indent=4)
        response = HttpResponse(content_type='application/json')
        response.content = json_data
        return response
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Pizza not found'}, status=404)



