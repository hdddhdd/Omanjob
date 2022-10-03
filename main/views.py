from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def test(request):
    return render(request, 'test.html')

def play(request):
    return render(request, 'play.html')
