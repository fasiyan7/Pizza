import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Pizza
from django.contrib.auth.decorators import login_required

def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        content={
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,   
        }
    #return JsonResponse(content)
    #below code ffor maintaining indentation
        json_data = json.dumps(content, indent=4)
        response = HttpResponse(content_type='application/json')
        response.content = json_data
        return response
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Pizza not found'}, status=404)
    


@login_required
def protected_index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(
            title=data['title'], description=data['description'],
            creator=request.user,
        )
        new_pizza.save()
        return HttpResponse(
            content={
                'id': new_pizza.id,
                'title': new_pizza.title,
                'description': new_pizza.description,
            },
        )
    elif request.method == 'GET':
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(
            content={
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description,
            },
        )
    elif request.method == 'DELETE':
        if 'can_delete' in request.user.user_permissions:
            pizza = Pizza.objects.get(id=pid)
            pizza.delete()
            return HttpResponse(
                content={
                    'id': pizza.id,
                }
            )
        else:
            return HttpResponse(status_code=404)


class GetTenPizzasView(View):
    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})



