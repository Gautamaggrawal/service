from django.db import models
from .utils import *

class MyURL(models.Model):
	url=models.CharField(max_length=220,)
	shortcode=models.CharField(max_length=15,unique=True)
	updated=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode=="":
			self.shortcode=code_generator()
		super(MyURL,self).save(*args,**kwargs)





	def __str__(self):
		return str(self.url)
	def __unicode__(self):
		return __str__(self.url)