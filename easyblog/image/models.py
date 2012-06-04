from django.db import models
from django_thumbs.db.models import ImageWithThumbsField

class Image(models.Model):
    '''Image class for uploaded images'''
    name = models.CharField(max_length=64)
    src = ImageWithThumbsField(upload_to='images',
        sizes=((72,72),(256,256),(512,512)))
    desc = models.CharField(max_length=256,
        help_text='Image description')

    def __unicode__(self):
        return self.name

    def thumbnail(self):
        return '<img src="{src}" />'.format(
            src=self.src.url_72x72
        )
    thumbnail.allow_tags = True

class Gallery(models.Model):
    '''Gallery collection'''
    STYLES = [
        ('one-wide', 'One wide across'),
        ('two-wide', 'Two wide across, even'),
        ('two-wide-asym', 'Two wide across, assymetrical'),
        ('three-wide', 'Three wide across')
    ]
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True,
        help_text='Identified for URLs')
    images = models.ManyToManyField(Image)
    style = models.CharField(max_length=16, choices=STYLES,
        help_text='Gallery layout and style')
    
    def __unicode__(self):
        return self.name
    
    def inline_script(self):
        return '''<pre>&lt;div class="gallery-{slug}"&gt;&lt;script src="{src}"&gt;&lt;/script&gt;&lt;/div&gt;</pre>
<p>
    Embedded HTML script for gallery. Copy this into the entry where the gallery
    should be displayed.
</p>'''.format(
            slug=self.slug,
            src=self.get_absolute_url()
        )
    inline_script.allow_tags = True

    @models.permalink
    def get_absolute_url(self):
        return ('gallery', (), {
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'galleries'

