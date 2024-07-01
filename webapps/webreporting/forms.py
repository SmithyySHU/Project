from django import forms

class BenefitCalculatorForm(forms.Form):
    hours_worked = forms.DecimalField(label='Hours Worked Per Week', max_digits=5, decimal_places=2)
    hourly_rate = forms.DecimalField(label='Hourly Pay Rate (£)', max_digits=10, decimal_places=2)
    get_housing_costs = forms.ChoiceField(label='Do you get help with housing costs?', choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    has_work_allowance = forms.ChoiceField(label='Are you responsible for a child or young person, or living with a disability or health condition that affects your ability to work?', choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    age = forms.IntegerField(label='Age')
    partner_works_more_than_24_hours = forms.ChoiceField(label='Does your partner work more than 24 hours a week?', choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    weeks_on_esa = forms.IntegerField(label='Weeks on ESA (if applicable)', required=False)
    esa_group = forms.ChoiceField(label="If on ESA, are you in the 'work-related activity' group or 'support' group?", choices=[('work-related activity', 'Work-related activity'), ('support', 'Support')], required=False)
    num_children = forms.IntegerField(label='Number of Children', required=False)
