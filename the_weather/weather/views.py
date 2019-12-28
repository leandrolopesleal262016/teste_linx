from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForms

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},BR&lang=pt&units=metric&APPID=dd7227b5df6988b8ba34bffd5b6e3450'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForms(request.POST)

        if form.is_valid(): # Evita cidades duplicadas
            
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'Esta cidade não existe no mundo!'
            else:
                err_msg = "Está Cidade já está no Banco de Dados!"

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'Cidade adicionada com sucesso!'
            message_class = 'is-success'
                
           
    form = CityForms()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

##    print(weather_data)

    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class 
        }
    
    return render(request,'weather/weather.html',context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')
    
