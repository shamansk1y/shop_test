from django.shortcuts import render
from main_page.context_data import get_page_context


def handle_post_request(request):
    pass

    # fast_booking = FastBookingForm(request.POST)
    #
    #
    # if fast_booking.is_valid():
    #     fast_booking.save()
    #     return redirect('/')



def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'index.html', context=data)