from __init__ import *
from views import *


app.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
app.add_url_rule('/<urls>', 'urlf', urlf, methods=['POST', 'GET'])