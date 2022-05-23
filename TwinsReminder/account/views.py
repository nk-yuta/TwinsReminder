from django.views import generic


'''トップページ'''
class TopView(generic.TemplateView):
    template_name = 'account/top.html'