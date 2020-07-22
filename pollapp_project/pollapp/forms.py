from django.forms import ModelForm,TextInput
from .models import Poll

class PollForm(ModelForm):
    class Meta :
        model = Poll
        fields = ['question','option_one','option_two','option_three','option_four']
        widgets = {
        'question' : TextInput(attrs = {'class' : 'input','placeholder' : 'Enter the Question'}),
        'option_one' : TextInput(attrs = {'class' : 'input','placeholder' : 'Enter first option'}),
        'option_two' : TextInput(attrs = {'class' : 'input','placeholder' : 'Enter second option'}),
        'option_three' : TextInput(attrs = {'class' : 'input','placeholder' : 'Enter third option'}),
        'option_four' : TextInput(attrs = {'class' : 'input','placeholder' : 'Enter fourth option'})
        }
