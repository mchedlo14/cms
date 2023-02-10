from django.db import models

CURRENCY = [

    ('GEL', 'Georgian Lari'),
    ('USD', 'USD Dolar'),
    ('EUR', 'EURO'),
]

class Web_parametres(models.Model):
    block_name = 'ძირითდი პარამეტრები'
    web_name = models.CharField(max_length=200,blank=True,null=True)
    web_description = models.CharField(max_length=400,blank=True,null=True)
    web_logo = models.ImageField(upload_to='settings/',blank=True,null=True)
    web_number = models.CharField(max_length=200,blank=True,null=True)
    web_email = models.EmailField(default='info@astronaut.ge',blank=True,null=True)
    web_info_adress = models.CharField(max_length=300,blank=True,null=True)
    web_info_adress_city = models.CharField(max_length=300,blank=True,null=True)
    web_currency = models.CharField(max_length=100, choices=CURRENCY)

    def __str__(self):
        return self.block_name

ROBOTS = [
    ('Enable','Allow Robots'),
    ('Disable','DisAllow Robots')
]


class Web_Seo_parametres(models.Model):
    block_name = 'SEO პარამეტრები'
    web_seo_title = models.CharField(max_length=200,blank=True,null=True)
    web_seo_description = models.CharField(max_length=400,blank=True,null=True)
    web_seo_author = models.CharField(max_length=100,blank=True,null=True)
    web_seo_keywords = models.TextField(max_length=800,blank=True,null=True)
    web_seo_robots = models.CharField(max_length=100, choices=ROBOTS)
    web_social_name = models.CharField(max_length=200,blank=True,null=True)
    web_social_description = models.TextField(max_length=800,blank=True,null=True)
    web_social_image = models.ImageField(upload_to='settings/',blank=True,null=True)

    def __str__(self):
        return self.block_name

