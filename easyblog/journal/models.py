from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    STYLES = [
        ('default', 'Default style')
    ]
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, unique=True,
        help_text='Identifier for URLs')
    style = models.CharField(max_length=16, choices=STYLES,
        default='default', help_text='Formatting style')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('category', (), {
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'categories'

class Entry(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True,
        help_text='Identifier for URLs')
    excerpt = models.CharField(max_length=256,
        help_text='Excerpt on the table of contents')
    body = models.TextField(help_text='<a href="http://www.textism.com/tools/textile/">Formatting help</a>')
    date = models.DateField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    published = models.BooleanField()

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('entry', (), {
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'entries'

