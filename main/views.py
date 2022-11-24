from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def test(request):
    return render(request, 'test.html')

def play(request):
    return render(request, 'play.html')
def mbti(request):
    return render(request, 'mbti.html')
def review(request):
    return render(request, 'review.html')
