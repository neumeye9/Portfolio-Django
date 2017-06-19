from django.shortcuts import render

# Create your views here.

def index(request):
    print "Home"
    return render(request, 'portfolio_app/index.html')

def portfolio(request):
    print "Portfolio"
    return render(request, 'portfolio_app/portfolio.html')