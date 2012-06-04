from django.shortcuts import render, get_object_or_404
from easyblog.image.models import Gallery, Image

import json

def gallery(request, slug=None):
    gallery = get_object_or_404(Gallery, slug=slug)
    images = map(lambda x: x.src.url_256x256, gallery.images.all())
    return render(request, 'gallery.js', {
            'images': json.dumps(images),
            'gallery': gallery
        },
        content_type='text/javascript')

