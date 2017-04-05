from django import template

register = template.Library()

@register.filter('cut')
def cut(value,arg):
    return value.replace(arg,'')
#register.filter('ccc',cut)

@register.filter('zfill')
def jl(value,arg):
    return value.zfill(arg)

#register.filter('zfill',jl)

@register.filter('px')
def px(value):
    l = list(value)
    l.sort()
    return ''.join(l)


import datetime
import time

@register.tag('current_time1')
def do_current_time1(parser, token):
    #"current_time1 "%Y-%m-%d %I:%M %p""
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    #format_string = "'%Y-%m-%d %I:%M %p'"
    return CurrentTimeNode1(format_string[1:-1])

class CurrentTimeNode1(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        #now = datetime.datetime.now()
        #return now.strftime(self.format_string)
        return time.strftime(self.format_string)

@register.tag('current_time2')
def do_current_time2(parser, token):
    #"current_time2 "%Y-%m-%d %I:%M %p""
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    #format_string = "'%Y-%m-%d %I:%M %p'"
    return CurrentTimeNode2(format_string[1:-1])

class CurrentTimeNode2(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time2'] = now.strftime(self.format_string)
        return ''

import re
@register.tag('current_time3')
def do_current_time3(parser, token):
    #"current_time3 '%Y-%m-%d %I:%M %p' as xiaoli"
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    #arg = "'%Y-%m-%d %I:%M %p' as xiaoli"
    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)
    #fmt = "'%Y-%m-%d %I:%M %p'"
    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode3(fmt[1:-1], var_name)

class CurrentTimeNode3(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''
