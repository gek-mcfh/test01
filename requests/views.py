from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from requests.models import Request


@csrf_exempt
def extract_content(request):

    if request.method == 'POST':
        Request.objects.create(
            headers=request.headers,
            body=request.body
        )
    return HttpResponse(content='200')
