from django.shortcuts import render
from .models import Image
from .color_ascii_image import *
from random import randint
from django.http import FileResponse, HttpResponse


def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        allowed_formats = ('jpg', 'jpeg', 'png')
        upload_format = file.name.split('.')[-1]

        if upload_format not in allowed_formats:
            return HttpResponse('Wrong format image, allowed formats: jpg, jpeg, png')
        
        file.name = str(randint(0, 999999999999)) + '.jpg'
        font_size = int(request.POST.get('font_size'))
        color_level = int(request.POST.get('color_level'))

        path_to_source = 'media/source/' + file.name
        path_to_save = 'media/ascii_arts/'

        document = Image.objects.create(image=file)
        document.save()

        app = ArtConverter(path_to_source, path_to_save, font_size, color_level)
        image_name = app.run()
        file = 'media/ascii_arts/' + image_name
        response = FileResponse(open(file, 'rb'))
        return response



    return render(request, 'templates/to_ascii.html')


def download_file(request):
   filename = os.path.basename(the_file)
   chunk_size = 8192
   response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                           content_type=mimetypes.guess_type(the_file)[0])
   response['Content-Length'] = os.path.getsize(the_file)    
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   return response
