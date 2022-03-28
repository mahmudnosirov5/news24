from django.db import models

class News(models.Model):
	image = models.ImageField(upload_to='images/')
	heading = models.CharField(max_length = 500)
	main_info = models.CharField(max_length = 2000)
	content = models.CharField(max_length = 10000)
	category = models.CharField(max_length = 100, default='different')
	date = models.CharField(max_length = 20)
	permission = models.BooleanField(default=1)
	
	def __str__(self):
		return f'{self.id} - {self.heading}'

	class Meta:
		db_table = "News"
