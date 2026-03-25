from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField('Sarlavha',max_length=255,db_index=True)
    slug = models.SlugField('manzil',unique=True)
    date = models.DateTimeField('Vaqt',default=timezone.now)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
         return reverse('category_detail_url',kwargs={'slug':self.slug})
    
class Post(models.Model):
    title = models.CharField('Sarlavha', max_length=255,db_index=True)
    image = models.ImageField('Rasm')
    info = models.TextField('Izoh')
    slug = models.SlugField('manzil',unique=True)
    popular = models.IntegerField('ko\'rganlar soni',default=0)
    date = models.DateTimeField('Vaqt',default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='category_set')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    def __str__(self):
            return self.title
        
    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})

