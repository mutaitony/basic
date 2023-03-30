from __init__ import *
from views import *


app.add_url_rule('/', 'index', index, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/login', 'login', login, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/logout', 'logout', logout, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/register', 'register', register, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/dashboard', 'dashboard', dashboard, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/settings', 'settings', settings, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/logs', 'logs', logs, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/<urls>', 'urlf', urlf, methods=['POST', 'GET'], strict_slashes=False)