from django.shortcuts import render
from django.http import HttpResponse, Http404
from comp.models import ratings
import comp.review_summary
from django.template import RequestContext, loader


def index(request):
    rating_list = ratings.objects.order_by('id')
    context = {'rating_list' : rating_list}
    return render(request, 'comp/index.html', context)

def detail(request, company_id):
    try:
        # chose to call id as company_id because id is unique to the company, not necessarily to the rating
        # however, the return object is called rating because it includes all the detailed ratings of the company
        rating = ratings.objects.get(pk = company_id)
    except ratings.DoesNotExist:
        raise Http404("Company does not exist")
    return render(request, 'comp/detail.html', {'rating' : rating})

def review_summary(request, company):
    common_nouns = comp.review_summary.common_nouns(company)
    common_adjs = comp.review_summary.common_adjs(company)
    common_tags = comp.review_summary.common_tags(company)
    print(common_adjs)
    return render(request, 'comp/review_summary.html', {'common_adjs' : common_adjs})
# The review summary for this company is not available.

if __name__ == '__main__':
    review_summary('Walmart')