from flask import Blueprint
cliente = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates' )

from . import routes