from django.http import JsonResponse

def homePage(request):
    data={
        'Status':'Success...Website Is Live.',
        'Message':'Welcome To ProjectTree Website...!!!'
    }
    return JsonResponse(data)

