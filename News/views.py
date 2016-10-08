from django.http import HttpResponse
import json
import urllib2
from django.template import loader
# Create your views here.


def home(self):
    template = loader.get_template('News/index.html')
    dic = data()
    context = {
        'dico': dic,
    }
    #html = ''
    #for foo in dic['items']:
    #    html += '<a href = #>' + foo['title'] +</a><br>''
    return HttpResponse(template.render(context))


def data():
    json_ob = json.load(urllib2.urlopen(
        'http://flyingkites.herokuapp.com/query/tech'))
    return json_ob
