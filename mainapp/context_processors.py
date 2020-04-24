from mainapp.models import Vacancy


def vacancy(request):
    vac = Vacancy.objects.all()
    return {'vacancy': vac}
