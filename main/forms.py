from django import forms 
from .models import News 

class NewsForm(forms.Form):
	image = forms.ImageField(label="Загрузить фотографию", label_suffix='')
	heading = forms.CharField(max_length=130, label=False, widget = forms.Textarea(attrs={'name':'new_news_heading', 'class':'new_news_heading', 'placeholder':'Заголовок'}))
	main_info = forms.CharField(max_length=300, label=False, widget = forms.Textarea(attrs={'name':'new_news_main-info', 'class':'new_news_main-info', 'placeholder':'Главная информация'}))
	content = forms.CharField(label=False, widget = forms.Textarea(attrs={'name':'new_news_content', 'class':'new_news_content', 'placeholder':'Содержимое'}))
	category = forms.ChoiceField(label='Выберите категорию:', choices=(('different', 'Разное'), ('uzbekistan', 'Узбекистан'), ('world', 'Мир'), ('society', 'Общество'), ('sport', 'Спорт')))
	key = forms.CharField(required=False, max_length = 4, label='Ключ', widget = forms.PasswordInput())
	
	class Meta:
		model = News
		fields = '__all__'