from __init__ import *
from views import *


app.add_url_rule('/', 'index', index, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/login', 'login', login, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/logout', 'logout', logout, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/register', 'register', register, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/admin', 'admin', dashboard, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/dashboard', 'dashboard', dashboard, methods=['POST', 'GET'], strict_slashes=False)


app.add_url_rule('/ndc/settings', 'settings', settings, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/logs', 'logs', logs, methods=['POST', 'GET'], strict_slashes=False)

app.add_url_rule('/ndc/dc_white_space', 'dc_white_space', dc_white_space, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/containment_data', 'containment_data', containment_data, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/comments', 'comments', comments, methods=['POST', 'GET'], strict_slashes=False)

app.add_url_rule('/ndc/power_rooms', 'power_rooms', power_rooms, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/power_rooms_data', 'power_rooms_data', power_rooms_data, methods=['POST', 'GET'], strict_slashes=False)

app.add_url_rule('/ndc/generators', 'generators', generators, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/generators_data', 'generators_data', generators_data, methods=['POST', 'GET'], strict_slashes=False)

app.add_url_rule('/ndc/new', 'new', new, methods=['POST', 'GET'], strict_slashes=False)



app.add_url_rule('/<urls>', 'urlf', urlf, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/generate_pdf', 'generate_pdf', generate_pdf, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/change_email', 'change_email', change_email, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/change_password', 'change_password', change_password, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/change_name', 'change_name', change_name, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/change_username', 'change_username', change_username, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/delete_account', 'delete_account', delete_account, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/download_comments/<int:logs>', 'download_comments', download_comments, methods=['POST', 'GET'], strict_slashes=False)
app.add_url_rule('/ndc/priview_logs', 'priview_logs', priview_logs, methods=['POST', 'GET'], strict_slashes=False)