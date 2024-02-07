from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def health(request):
    return render(request, 'main/health.html')


def doctors(request):
    return render(request, 'main/doctors.html')


def therapist(request):
    return render(request, 'main/therapist.html')


def gastroenterologist(request):
    return render(request, 'main/gastroenterologist.html')


def ophthalmologist(request):
    return render(request, 'main/ophthalmologist.html')


def obstetriciangynecologist(request):
    return render(request, 'main/obstetriciangynecologist.html')


def infectious(request):
    return render(request, 'main/infectious.html')


def neurologist(request):
    return render(request, 'main/Neurologist.html')


def Endocrinologist(request):
    return render(request, 'main/Endocrinologist.html')


def cardiologist(request):
    return render(request, 'main/cardiologist.html')


def surgeon(request):
    return render(request, 'main/surgeon.html')


def otorhinolaryngologist(request):
    return render(request, 'main/otorhinolaryngologist.html')


def traumatologist(request):
    return render(request, 'main/traumatologist.html')


def urologist(request):
    return render(request, 'main/urologist.html')


def oncologist(request):
    return render(request, 'main/oncologist.html')


def psychiatrist(request):
    return render(request, 'main/psychiatrist.html')


def pediatrician(request):
    return render(request, 'main/pediatrician.html')