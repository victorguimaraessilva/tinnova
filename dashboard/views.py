from django.shortcuts import render
from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from culture.models import Culture
from producer.models import Producer


def dashboard(request):
    
    total_farms = Producer.objects.count()
    total_cultures = Culture.objects.count()
    total_farms_area = Producer.objects.aggregate(Sum('total_area'))
    
    context = {
        'totals' : { 
            'farms': total_farms,
            'cultures': total_cultures,
            'farms_area': total_farms_area['total_area__sum'] or 0
        },
    }
    
    return render(request, 'dashboard.html', context)


class DashboardView(APIView):
  
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        
        total_farms = Producer.objects.count()
        total_cultures = Culture.objects.count()
        total_farms_area = Producer.objects.aggregate(Sum('total_area'))
        total_farms_arable = Producer.objects.aggregate(Sum('arable_area'))
        total_farms_vegetation = Producer.objects.aggregate(Sum('vegetation_area'))
        
        farmxstate = Producer.objects.values('state').annotate(total=Count('state')).order_by().values('state', 'total')
        farmxculture = Producer.objects.values('cultures').annotate(total=Count('cultures')).order_by().values('cultures__name', 'total')

        context = {
            'totals': { 
                'farms': total_farms,
                'cultures': total_cultures,
                'farms_area': total_farms_area['total_area__sum'] or 0,
                'farms_arable': total_farms_arable['arable_area__sum'] or 0,
                'farms_vegetation': total_farms_vegetation['vegetation_area__sum'] or 0,
            },
            'charts': {
                'farmxstate': farmxstate,
                'farmxculture': farmxculture
            }
        }
        
        return Response(context)