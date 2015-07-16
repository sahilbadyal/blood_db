from django.forms import ModelForm
from api.models import Donor
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _

"""class DonorForm(ModelForm)
	class Meta:
		model = Donor
		fields = '__all__'
		widget = {
            'address': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
		error_messages = {
            'first_name': {
                'max_length': _("This first name is too long."),
            },
            'last_name': {
                'max_length': _("This last name is too long."),
            },
            'phone_no': {
                'max_length': _("This phone number is too long."),
            },
            'address': {
                'max_length': _("This address is too long."),
            },
        }"""