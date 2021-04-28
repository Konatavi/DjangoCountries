from django.shortcuts import render, HttpResponse, Http404
import json

from MainApp.models import Country, Language, LinkCountryLanguage


# Загрузка данных из countries_list в базу данных
def json_into_db():
    with open('MainApp/templates/country-by-abbreviation.json') as f:
        countries_list = json.load(f)
    Country.objects.all().delete()
    Language.objects.all().delete()
    LinkCountryLanguage.objects.all().delete()
    languages_set = set()
    for country_one in countries_list:
        country_for_db = Country(name=country_one["country"])
        country_for_db.save()
        for language_one in country_one["languages"]:
            len_check = len(languages_set)
            languages_set.add(language_one)
            link_for_db = LinkCountryLanguage(name_country=country_one["country"], name_language=language_one)
            link_for_db.save()
            if len_check != len(languages_set):
                language_for_db = Language(name=language_one)
                language_for_db.save()
                # country_from_db = Country.objects.get(name=language_one)

# Create your views here.


def main(request):
    #  json_into_db()
    return render(request, 'index.html', {"page_title": "Home"})


def func_country(request, country_name):

    try:
        link_from_db = LinkCountryLanguage.objects.filter(name_country=country_name)
    except LinkCountryLanguage.DoesNotExist:
        raise Http404

    context = {
        "country_db": country_name,
        "languages_by_country": link_from_db,
        "page_title": f"Country:{country_name}",
        "page": "Country"
    }
    return render(request, 'country.html', context)


def func_countries(request):
    # json_into_db()
    countries_from_db = Country.objects.all()
    context = {
        "countries": countries_from_db,
        "page_title": "Countries"
    }
    return render(request, 'countries.html', context)


def func_languages(request):
    # json_into_db()
    languages_from_db = Language.objects.all()
    context = {
        "languages_list": languages_from_db,
        "page_title": "Languages"
    }
    return render(request, 'languages.html', context)


def func_countries_by_language(request, language_name):
    # json_into_db()
    try:
        link_from_db = LinkCountryLanguage.objects.filter(name_language=language_name)
    except LinkCountryLanguage.DoesNotExist:
        raise Http404
    context = {
        "language": language_name,
        "countries_list_by_language": link_from_db,
        "page": "Language"
    }
    return render(request, 'countries_by_language.html', context)




