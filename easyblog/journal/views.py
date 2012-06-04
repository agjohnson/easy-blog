from django.shortcuts import render_to_response, get_object_or_404
from easyblog.journal.models import Category, Entry

def index(request, category_slug=None):
    if category_slug is not None:
        category = get_object_or_404(
            Category,
            slug=category_slug
        )
        toc = Entry.objects.filter(
            category=category,
            published=True
        )
    else:
        toc = Entry.objects.filter(
            published=True
        )
    
    return render_to_response(
        'index.html',
        {'toc': toc}
    )

def show(request, slug=None):
    entry = get_object_or_404(Entry, slug=slug, published=True)
    return render_to_response(
        'show.html',
        {'entry': entry}
    )

