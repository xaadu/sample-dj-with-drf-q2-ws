from django.http import JsonResponse


def home(request):
    return JsonResponse(
        {
            "info": "Hello, World!",
            "status": "success",
            "message": "Welcome to the API Demo",
        },
        status=200,
    )
