from celery import shared_task
import base64
import os
import requests
from t2img.local import API_KEY

@shared_task
def add():
    return "image1 generated"

@shared_task
def generate_image(text):
    if not os.path.exists('out'):
        os.makedirs('out')

    engine_id = "stable-diffusion-v1-6"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = API_KEY

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # Assuming only one image is generated
    image_data = data["artifacts"][0]
    image_base64 = image_data["base64"]

    # Save the image to a file
    image_path = f"./out/generated_image.png"
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    # try:
    #     generated_image = GeneratedImage.objects.create(text=text, image_url=image_path)
    # except Exception as e:
    #     print(e)

    return {'status': 'success', 'image_url': image_path}
