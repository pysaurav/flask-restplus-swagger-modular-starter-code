from flask_restplus import Namespace, Resource, fields
from flask import request

api = Namespace('Module2', description='Module2 operations')

Module2 = api.model('Module2', {
    'id': fields.Integer(readonly=True, description='Unique identifier'),
    'field': fields.String(required=True, description='String Content'),
})

LIST2 = [
    {'id': 1, 'field': 'YourStringfromList2'},
]

@api.route('/')
class Module2List(Resource):
    @api.doc('list_partners')
    @api.marshal_list_with(Module2)
    def get(self):
        '''List all Items'''
        return LIST2

    @api.expect(Module2)
    @api.marshal_with(Module2)
    def post(self):
        new_partner = request.get_json()
        new_partner['id']=len(LIST2)+1
        LIST2.append(new_partner)
        return {'result':'Partner Added'}, 201


@api.route('/<id>')
@api.param('id', 'The partner identifier')
@api.response(404, 'Partner not found')
class Partner(Resource):
    @api.doc('get_partner')
    @api.marshal_with(Module2)
    def get(self, id):
        '''Partner details by name'''
        for item in LIST2:
            if item['id'] == id:
                return item
        api.abort(404)