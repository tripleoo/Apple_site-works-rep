from django.db import models
from django.urls import reverse

def default_description():
    # Создаем новый объект Description
    default_desc = Description.objects.create(model='Default model', img_1='s.png', img_2='s.png')
    # Возвращаем созданный объект
    return default_desc.id
class Iphone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    memory = models.CharField(default='256gb', max_length=20, verbose_name='Объем памяти')
    color = models.CharField(blank=True, max_length=20, verbose_name='Цвет')
    price = models.CharField(max_length=20, verbose_name='Цена')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение товара')
    slug = models.SlugField(max_length=50, unique=False, blank=True, db_index=True)
    vid = models.ForeignKey('VidTovara', on_delete=models.PROTECT, related_name='vid', verbose_name='Вид товара')
    promo = models.ManyToManyField('Promo', blank=True, related_name='promo', verbose_name='Акции')
    descrip = models.ForeignKey('Description', on_delete=models.PROTECT, related_name='des', default=default_description)

    class Meta:
        verbose_name = 'Товар магазина'
        verbose_name_plural = "Товары магазина"
    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('iphone', kwargs={'devise_slug': self.slug})

class VidTovara(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=False, default='default-slug-value')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vid', kwargs={'vid_id':self.pk})

class Promo(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=True, db_index=True)




    def __str__(self):
        return self.name

class Review(models.Model):
    nikname = models.CharField(max_length=50, verbose_name='Введите ваше имя')
    rev = models.CharField(max_length=500, verbose_name='Оставьте свой комментарий')
    iphone = models.ForeignKey('Iphone', on_delete=models.CASCADE, related_name='reviews', null=True)


class Description(models.Model):
    model = models.CharField(max_length=100, blank=True)
    img_1 = models.ImageField(upload_to='images/', blank=True, default='15blue.jpeg')
    img_2 = models.ImageField(upload_to='images/',blank=True)
