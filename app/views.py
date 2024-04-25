from django.shortcuts import render
from .tasks import add, generate_image
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import GeneratedImage

# Call the add task asynchronously
def test(request):
    add.delay()
    return HttpResponse("Hello this is celery")

@csrf_exempt
def generate_image_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', None)
        if text:
            try:
                result = generate_image.delay(text)
                result_data = result.get()
                if result_data.get('status') == 'success':
                    image_path = result_data.get('image_url')
                    try:
                        generated_image = GeneratedImage.objects.create(text=text, image_url=image_path)
                    except Exception as e:
                        print(e)
                    return JsonResponse({'status': 'success', 'image_url': result_data.get('image_url')})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Image generation failed.'}, status=500)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Text is not present'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)