from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from .models import Massage


# Create your views here.


class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['neme'],
                  cd['subject'],
                  cd['email'],
                  cd['massage'])
            Massage.objects.create(neme=cd['neme'],
                                   subject=cd['subject'],
                                   email=cd['email'],
                                   massage=cd['massage'],
                                   )
            return redirect('home:home')
        return render(request, 'contact/contact.html', {'form': form})
