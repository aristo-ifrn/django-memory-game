from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Plays
import json

def index(request): 
  return render(request, "index.html")

def ranking(request):
  plays = Plays.objects.all().order_by("-has_completed", "flips_quantity", "-used_time", "date")
  return render(request, "ranking.html", {"plays": plays})

def game(request):
  if request.user.is_authenticated:
    return render(request, "game.html")
  else:
    return redirect("/admin/login/?next=/game")

def get(request):
  if request.method == 'GET':
    plays = Plays.objects.all().order_by("-has_completed", "flips_quantity", "-used_time", "date").values()
    return JsonResponse(list(plays), safe=False)
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def add(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      date = parse_datetime(data.get('date'))
      if not date:
        return JsonResponse({'status': 'error', 'message': 'Data inválida'}, status=400)
      
      play = Plays(
        username=data['username'],
        flips_quantity=data['flips_quantity'],
        used_time=data['used_time'],
        date=date,
        has_completed=data['has_completed'],
        user=request.user
      )
      play.save()
      return JsonResponse({'status': 'success'}, status=201)
    except Exception as e:
      print(f"Erro: {e}")  # Log do erro
      return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
  return JsonResponse({'status': 'error', 'message': 'Método inválido'}, status=405)
