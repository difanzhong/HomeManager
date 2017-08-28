from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.template.context_processors import csrf
from .models import House
from datetime import datetime
from .forms import CustomerForm, AddressFrom


# to list all the available houses
def house_index(request):
    latest_question_list = 5
    context = {}
    return render(request, 'Houses/base.html', context)


# retrieve single house refer to its id
def house(request, house_id):
    try:
        house = House.objects.get(pk=house_id)
        amenities = house.amenity
        address = house.address
        context = {
            'house': house,
            'amenities': amenities,
            'address': address,
        }
    except House.DoesNotExist:
        raise Http404("House Not Found")
    return render(request, 'Houses/house_details.html', {'context': context})


# finalise the booking - post
class ConfirmationView(View):
    def get(self, request, *args, **kwargs):
        check_in_date_str = request.GET.get('check_in')
        check_out_date_str = request.GET.get('check_out')
        house_id = request.GET.get('house_id')
        try:
            check_in_date = datetime.strptime(check_in_date_str, '%d-%m-%Y')
            check_out_date = datetime.strptime(check_out_date_str, '%d-%m-%Y')
            days = (check_out_date - check_in_date).days
            the_house = House.objects.get(pk=house_id)
            address = the_house.address
            form_customer = CustomerForm()
            form_addr = AddressFrom()

        except ValueError:
            raise Http404("Check in or Check out Date Error")
        except House.DoesNotExist:
            raise Http404("House Not Found")
        except:
            raise Http404('Error Occurred')
        data = {
            'check_in': check_in_date.strftime('%d %b , %Y'),
            'check_out': check_out_date.strftime('%d %b , %Y'),
            'total_days': days,
            'house': the_house,
            'room_total': the_house.rate * days,
            'address': address,
            'form_customer': form_customer,
            'form_addr': form_addr,
        }
        return render(request, 'Houses/confirmation.html', {'data': data})





