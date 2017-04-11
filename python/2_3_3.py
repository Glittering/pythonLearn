try:
    import json
except ImportError:
    import simplejson

print json.dumps({'python':2.7})
