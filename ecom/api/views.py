from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({
        'success': True, 'message': 'hello world'
    })
