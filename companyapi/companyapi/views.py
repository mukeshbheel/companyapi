from django.http import HttpResponse,JsonResponse

def home_page(request):
    print('home page is requested')
    
    numbers = [1,2,3]
    
    return JsonResponse(numbers, safe=False)
    # return HttpResponse('this is home page')

