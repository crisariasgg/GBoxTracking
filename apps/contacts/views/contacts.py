""" User's Views """

# Django
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


# local Django
User = get_user_model()

class ContactView(TemplateView):
	template_name = 'contact.html'
	paginate_by = 5
				
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(pk=self.request.user.pk)
		context.update({
			'user': user,
		})
		return context
	
	def post(self, request):
		pass