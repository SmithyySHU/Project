from django.shortcuts import render, redirect
from .models import Job
from django.views.generic import ListView, DetailView
from .forms import BenefitCalculatorForm
from decimal import Decimal
from django.db.models import Q


# Create your views here.
def home(request) :
    return render (request, 'webreporting/home.html', {'title': 'Welcome to JobFinders'})


def contact(request) :
    return render (request, 'webreporting/contact.html', {'title': 'Contact JobFinders'})


def job(request) :
    search_query = request.GET.get('search', '')
    sort_option = request.GET.get('sort', '')

    jobs = Job.objects.all()

    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(category__icontains=search_query)
        )
        print(f"Search Query: {search_query}")  # Debugging
        print(f"Sort Option: {sort_option}")    # Debugging

    if sort_option:
        jobs = jobs.order_by(sort_option)

    context = {
        'jobs' : Job,
        'title' : 'Jobs',
        'search_query': search_query,
        'sort_option': sort_option,
    }
    return render (request, 'webreporting/job.html', context)

class JobListView(ListView):
    model = Job
    template_name = 'webreporting/job.html'
    context_object_name = 'jobs'
    ordering = ['-posting_date']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        sort_option = self.request.GET.get('sort', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(company__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(category__icontains=search_query)
            )

        if sort_option:
            queryset = queryset.order_by(sort_option)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_option'] = self.request.GET.get('sort', '')
        return context
class JobDetailView(DetailView) :
    model = Job

def calculate_universal_credit(hours_worked, hourly_rate, get_housing_costs, has_work_allowance):
    work_allowance_with_housing = Decimal('404')
    work_allowance_without_housing = Decimal('673')
    reduction_rate = Decimal('0.55')
    weekly_income = hours_worked * hourly_rate
    monthly_income = weekly_income * Decimal('4.33')
    work_allowance = work_allowance_with_housing if get_housing_costs == 'yes' else work_allowance_without_housing
    benefits_lost = max(Decimal('0'), (monthly_income - work_allowance) * reduction_rate) if has_work_allowance == 'yes' else monthly_income * reduction_rate
    return benefits_lost

def calculate_income_support_or_jsa(hours_worked, age, partner_works_more_than_24_hours):
    if hours_worked >= 16 or partner_works_more_than_24_hours == 'yes':
        return Decimal('0')
    return Decimal('57.90') if age < 25 else Decimal('73.10')

def calculate_esa(hours_worked, age, weeks_on_esa, esa_group):
    if hours_worked > 16:
        return Decimal('0')
    if weeks_on_esa <= 13:
        return Decimal('57.90') if age < 25 else Decimal('73.10')
    return Decimal('102.15') if esa_group == 'work-related activity' else Decimal('109.30')

def calculate_working_tax_credit(hours_worked, num_children):
    if hours_worked < 16:
        return Decimal('0')
    yearly_credit = Decimal('1960')
    if num_children:
        yearly_credit += Decimal('122.50') * Decimal('52') * min(num_children, 1) + Decimal('210') * Decimal('52') * max(0, num_children - 1)
    return yearly_credit / Decimal('12')

def benefit_calculator(request):
    if request.method == 'POST':
        form = BenefitCalculatorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            benefits_lost_universal_credit = calculate_universal_credit(Decimal(cd['hours_worked']), Decimal(cd['hourly_rate']), cd['get_housing_costs'], cd['has_work_allowance'])
            income_support_or_jsa = calculate_income_support_or_jsa(Decimal(cd['hours_worked']), cd['age'], cd['partner_works_more_than_24_hours'])
            esa = calculate_esa(Decimal(cd['hours_worked']), cd['age'], cd['weeks_on_esa'], cd['esa_group'])
            working_tax_credit = calculate_working_tax_credit(Decimal(cd['hours_worked']), cd['num_children'])
            return render(request, 'webreporting/result.html', {
                'benefits_lost_universal_credit': benefits_lost_universal_credit,
                'income_support_or_jsa': income_support_or_jsa,
                'esa': esa,
                'working_tax_credit': working_tax_credit
            })
    else:
        form = BenefitCalculatorForm()
    return render(request, 'webreporting/calculator.html', {'form': form})