from django.shortcuts import render
from django.http import HttpResponse



pagos = [
    {
        'monto': '14000',
        'tasa': '20',
        'plazo' : '3',
        'cuota': '520.29',
        'total' : '18730.44'
    }
]

def formulario(request):

    
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12
        n = plazo * 12

        c = (monto*r)/(1-(1+r)**-n)

        total = c*n

        ctx = {
            'pagos' : pagos
        }

        pagos.append({
            'monto': monto,
            'tasa': tasa,
            'plazo' : plazo,
            'cuota': c,
            'total' : total,
        })

        return render(request, 'form/formulario.html', ctx)
    else:
          ctx = {
               'pagos' : pagos
          }
          
          return render(request, 'form/formulario.html', ctx)