from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse
from datetime import datetime
import barcode
from barcode.writer import ImageWriter 

# Create your models here.

RANG = (
    ('qora','Qora'),
    ('oq','Oq'),
    ('qizil','Qizil'),
    ('sariq','Sariq'),
    ('kulrang','Kulrang'),
    ('moviy','Moviy'),
    ('yashil','Yashil'),
    ('jigarang','Jigarang'),
    ('pushti','Pushti'),
    ('boshqa','Boshqa'),
)

TUR = (
    ('smartfon','Smartfon'),
    ('telefon','Telefon'),
    ('computer','Copmuter'),
    ('planshet','Planshet'),
    ('noutbook','Noutbook'),
    ('smartwatch','SmartWatch'),
)

TEKSHIR = (
    ('ha','Ha'),
    ('yoq',"Yo'q"),
)

# ---------------------- Product Model -----------------------
class Product(models.Model):
    tur = models.CharField(max_length=150, choices=TUR, verbose_name='Mahsulot turi')
    nom = models.CharField(max_length=150, verbose_name='Mahsulot nomi')
    rang = models.CharField(max_length=50, choices= RANG, verbose_name='Mahsulot rangi', null=True, blank=True)
    rasm = models.ImageField(upload_to='mahsulotlar/%Y/%m/%d/', verbose_name='Mahsulot rasmi', null=True, blank=True)
    narx = models.IntegerField(default=0, verbose_name='Mahsulot natxi($)', null=True, blank=True)
    son = models.IntegerField(default=0, verbose_name='Mahsulot soni')
    kompania = models.CharField(max_length=300, verbose_name='Ishlab chiqaruvchi nomi ', null=True, blank=True ) # Ishlab chiqaruvchi nomi
    mudat  = models.CharField(max_length=150, verbose_name='Yaroqlilik mudati', null=True, blank=True)
    kg = models.IntegerField(default=0, verbose_name="Mahsulot og'irligi(gr)", null=True, blank=True)
    qr_code = models.ImageField(upload_to='QR_codes/%Y/%m/%d/', verbose_name='Mahsulot QR codi', null=True, blank=True)
    barcode = models.ImageField(upload_to='Shtrx_codes/%Y/%m/%d/', verbose_name='Mahsulot Shtrx codi', null=True, blank=True)
    izoh = models.CharField(max_length=300, null=True, blank=True, verbose_name="Qo'shimcha izoh")
    sana = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Omborga kelgan sana')
    yangilanish = models.DateTimeField(auto_now=True, verbose_name="O'zgartirish kiritilgan sana")
    
    def __str__(self): 
        return self.nom
    
    def get_absolute_url(self):
        return reverse('products:detail',
                       args=[self.sana.year,
                             self.sana.month,
                             self.sana.day,
                             self.pk])

    def avatar(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.rasm) ) # default='<img src="/media/default_pictures/"'

    avatar.short_description = 'Mahsulot rasmi'

    # QR-code save funciation
    def save(self, *args):
        data = f"Turi: {self.get_tur_display()} \nNomi: {self.nom} \nRangi: {self.get_rang_display()} \
            \nNarxi: {self.narx}$ \nSoni: {self.son} dona \nIshlab chiqaruvchi: {self.kompania} \
            \nMuddati: {self.mudat} \nOg'irligi: {self.kg} kg \
            \nIshlab chiqarilgan vaqti: {self.sana}"

        data2 = f"\nUrl: {self.get_absolute_url()}"
        qrcode_img = qrcode.make(data + data2)
        canvas = Image.new('RGB', (1000, 1000), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.nom}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        # ------ Barcode -------------------------- 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.nom}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'ID {self.id} \n{self.nom}.png', File(rv), save=False)
        return super().save(*args)


# ---------------------- Report Model -----------------------

class Report(models.Model):
    tur = models.CharField(max_length=150, choices=TUR, verbose_name='Mahsulot turi')
    nom = models.CharField(max_length=150, verbose_name='Mahsulot nomi')
    rang = models.CharField(max_length=50, choices= RANG, verbose_name='Mahsulot rangi', null=True, blank=True)
    rasm = models.ImageField(upload_to='repo_mahsulotlar/%Y/%m/%d/', verbose_name='Mahsulot rasmi', null=True, blank=True)
    # narx = models.IntegerField(default=0, verbose_name='Mahsulot natxi($)', null=True, blank=True)
    son = models.IntegerField(default=0, verbose_name='Mahsulot soni')
    kompania = models.CharField(max_length=300, verbose_name='Ishlab chiqaruvchi nomi ', null=True, blank=True ) # Ishlab chiqaruvchi nomi
    mudat  = models.CharField(max_length=150, verbose_name='Yaroqlilik mudati', null=True, blank=True)
    kg = models.IntegerField(default=0, verbose_name="Mahsulot og'irligi(gr)", null=True, blank=True)
    # qr_code = models.ImageField(upload_to='QR_codes/%Y/%m/%d/', verbose_name='Mahsulot QR codi', null=True, blank=True)
    # barcode = models.ImageField(upload_to='Shtrx_codes/%Y/%m/%d/', verbose_name='Mahsulot Shtrx codi', null=True, blank=True)
    izoh = models.CharField(max_length=300, null=True, blank=True, verbose_name="Qo'shimcha izoh")
    sana = models.DateField(auto_now=True, verbose_name='Hisobot vaqti')
    tekshir = models.CharField(max_length=100, verbose_name="Ha/Yo'q", choices=TEKSHIR, default='yoq')
    yangilanish = models.DateTimeField(auto_now=True, verbose_name="O'zgartirish kiritilgan sana")
    
    def __str__(self): 
        return self.nom
    
    def get_absolute_url(self):
        return reverse('products:detail',
                       args=[self.sana.year,
                             self.sana.month,
                             self.sana.day,
                             self.pk])

    def avatar(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.rasm) ) # default='<img src="/media/default_pictures/"'

    avatar.short_description = 'Mahsulot rasmi'


