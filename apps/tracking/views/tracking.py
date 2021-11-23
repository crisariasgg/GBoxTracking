""" User's Views """

# Django
from django.views.generic import FormView,TemplateView
from django.contrib.auth import get_user_model
from ..forms import TrackingForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import HttpResponseRedirect,render


class TrackingSearchView(FormView):
	form_class = TrackingForm
	template_name = 'tracking_search.html'
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			# tracking_number = form.cleaned_data['tracking_number']
			tracking_results = 'Pending'
			tracking_results = 'OnHand'
			tracking_results = 'InProcess'
			tracking_results = 'InTransit'
			tracking_results = 'AtDestination'
			tracking_results = 'Delivered'
			return render(request, 'tracking_results.html', {'tracking_results':tracking_results })