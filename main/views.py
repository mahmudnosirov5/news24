from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime 
from .forms import NewsForm
from .models import News
from django.core.files.storage import FileSystemStorage
import math

different = News.objects.filter(category="different", permission = True).order_by("-id")[:5]
uzbekistan = News.objects.filter(category="uzbekistan", permission = True).order_by("-id")[:6]
world = News.objects.filter(category="world", permission = True).order_by("-id")[:5]
society = News.objects.filter(category="society", permission = True).order_by("-id")[:6]
sport = News.objects.filter(category="sport", permission = True).order_by("-id")[:5]
last_news = News.objects.filter(permission = True).order_by("-id")[:5]

def index(request):
	return render(request, 'main/index.html', {
		'different_big': different[:1],
		'different_small': different[1:5],
		'uzbekistan_big': uzbekistan[:2],
		'uzbekistan_small': uzbekistan[2:6],
		'world_big': world[:1],
		'world_small': world[1:5],
		'society_big': society[:2],
		'society_small': society[2:6],
		'sport_big': sport[:1],
		'sport_small': sport[1:5],
		'last_news': last_news
		})

def one_news(request, news_id):
	news = News.objects.get(id = news_id)
	category_title = News.objects.get(id = news_id).category
	category = News.objects.filter(category = category_title, permission = True).order_by("-id")

	return render(request, 'main/one_news.html', {
		'news': news,
		'last_news': News.objects.filter(permission = True).order_by("-id")[:7],
		'recommended_news': News.objects.filter(permission = True).order_by("-id")[8:15],
		'category_small_news': category[:math.floor(len(category)/4)*4]
		})

def category(request, category_title):
	category = News.objects.filter(category = category_title, permission = True).order_by("-id")

	category_title_map = {
		'uzbekistan': 'УЗБЕКИСТАН',
		'world': 'МИР',
		'society': 'ОБЩЕСТВО',
		'sport': 'СПОРТ',
		'different': 'РАЗНОЕ'
	}

	return render(request, 'main/category.html', {
		'category_title': category_title_map[category_title],
		'category_big': category[:1],
		'category_small': category[1:5],
		'category_small_news': category[6: 6 + math.floor(len(category[6:])/4)*4 ],
		'last_news': last_news
		})

def add_news(request):
	data = None
 
	if request.method == 'POST':
		form = NewsForm(request.POST, request.FILES)

		if form.is_valid():
 
			if not form.cleaned_data['heading'] == News.objects.all().order_by('-id')[0].heading:

				image = form.cleaned_data['image']
				heading = form.cleaned_data['heading']
				main_info = form.cleaned_data['main_info']
				content = form.cleaned_data['content']
				category = form.cleaned_data['category']
				date = datetime.now().strftime('%H:%M / %d.%m.%Y')
				key = form.cleaned_data['key']
				permission = False

				if key == '7777':
					permission = True

				added_news = News(permission = permission, image = image, heading = heading, main_info = main_info, content = content, category = category, date = date)
				added_news.save()

				return HttpResponseRedirect(f'../news/{added_news.id}')

		else:
			return render(request, 'main/add_news.html', {'form': form})

	return render(request, 'main/add_news.html', {
		'form': NewsForm(),
		'last_news': News.objects.filter(permission = True).order_by("-id")[:7],
		'recommended_news': News.objects.filter(permission = True).order_by("-id")[8:15],
		})