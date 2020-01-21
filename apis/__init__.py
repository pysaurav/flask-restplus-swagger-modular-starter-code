from flask_restplus import Api

from .Module1 import api as mod1
from .Module2 import api as mod2

api = Api(
    title='My Apis',
    version='1.0',
    description='Documentation of routes',
    #doc = False
)

api.add_namespace(mod1, path='/mod1')
api.add_namespace(mod2, path='/mod2')
