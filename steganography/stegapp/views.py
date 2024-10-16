from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io

def index(request):
    return render(request, 'stegapp/index.html')

# Encrypt text into an image
@csrf_exempt
def encrypt_text(request):
    if request.method == 'POST':
        if 'image' not in request.FILES or 'text' not in request.POST:
            return JsonResponse({'message': 'Image or text not provided'}, status=400)

        image_file = request.FILES['image']
        text = request.POST['text']

        # Load the image and insert the text into the pixel data
        try:
            image = Image.open(image_file)
            pixels = image.load()

            # Check if text fits in the image
            if len(text) > image.width * image.height:
                return JsonResponse({'message': 'Text is too long for this image'}, status=400)

            for i, char in enumerate(text):
                x = i % image.width
                y = i // image.width
                r, g, b = pixels[x, y]
                pixels[x, y] = (ord(char), g, b)  # Encrypt in red channel

            # Save the image to a byte stream
            byte_io = io.BytesIO()
            image.save(byte_io, format='PNG')
            byte_io.seek(0)

            # Return the encrypted image as a downloadable response
            return FileResponse(byte_io, as_attachment=True, filename='encrypted_image.png')

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

# Decrypt text from the image
@csrf_exempt
def decrypt_text(request):
    if request.method == 'POST':
        if 'image' not in request.FILES or 'text_length' not in request.POST:
            return JsonResponse({'message': 'Image or text length not provided'}, status=400)

        image_file = request.FILES['image']
        text_length = int(request.POST['text_length'])

        try:
            # Load the image and extract the text from the pixel data
            image = Image.open(image_file)
            pixels = image.load()

            decrypted_text = ""
            for i in range(text_length):
                x = i % image.width
                y = i // image.width
                decrypted_text += chr(pixels[x, y][0])  # Extract from red channel

            return JsonResponse({'decrypted_text': decrypted_text})

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
