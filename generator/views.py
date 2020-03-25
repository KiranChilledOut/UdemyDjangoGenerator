from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.
def home(request):
   return render(request,'generator/home.html')

def password(request):

    password_length = int(request.GET.get('length', 12))

    characters=characters_lower=list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters_upper=list(string.ascii_uppercase)
        characters.extend(characters_upper)

    if request.GET.get('specialcharaters'):
        characters_special=list('!@#$%^&*()_')
        characters.extend(characters_special)

    if request.GET.get('numbers'):
        characters_number=list('0123456789')
        characters.extend(characters_number)

    generated_password=""
    # while ([char for char in characters_special if char in generated_password] and
    #        [char for char in characters_upper if char in generated_password] and
    #        [char for char in characters_lower if char in generated_password]):
    for l in range(password_length):
        generated_password += random.choice(characters_lower)

    return render(request,'generator/password.html',{"password":generated_password})

def about(request):
    return render(request,'generator/about.html')
