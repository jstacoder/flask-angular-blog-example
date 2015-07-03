import os
import json
from htmlmin import minify

BASE_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__),'static','partials')

def get_templates(dirname=None):
    rtn = {}
    dirname = dirname or BASE_TEMPLATE_DIR
    full_dirname = os.path.realpath(dirname)
    if os.path.exists(full_dirname):
        templates = map(lambda x: (os.path.join(dirname,x),open(os.path.join(full_dirname,x),'r').read()),filter(lambda x: os.path.isfile(os.path.join(full_dirname,x)),os.listdir(full_dirname)))
        for t in  templates:
            rtn['/'+'/'.join(t[0].split('/')[1:])] = minify(unicode(t[1].decode('utf-8')),remove_empty_space=True)
    return rtn

def make_cache_file(app_name=None):
    CACHE_FILENAME = 'templates.min.js'
    APP_NAME = app_name or 'app'

    head = "angular.module('{}')"
    js_template = '''
    .run(['$templateCache',function($templateCache){
        var templateData = JSON.parse(%s),
            name = Object.keys(templateData)[0];
        $templateCache.put(name,templateData[name]);        
        }])
    '''
    open(os.path.join(os.path.dirname(__file__),'static','js',CACHE_FILENAME),'w').write(head.format(APP_NAME)+'\n'.join(map(lambda x: js_template % (repr(json.dumps({x:get_templates()[x]}))),get_templates()))+';')

if __name__ == "__main__":
    make_cache_file()
    print 'finished compliling the template cache'
