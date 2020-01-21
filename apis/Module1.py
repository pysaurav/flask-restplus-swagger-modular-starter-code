from flask_restplus import Namespace, Resource, fields
from flask import request

api = Namespace('Module1', description='Module1 operations')

module1 = api.model('Module1', {
    'id': fields.Integer(readonly=True, description='Unique identifier'),
    'field': fields.String(required=True, description='String Content'),
})

LIST1 = [
    {'id': 1, 'field': 'YourString'},
]

@api.route('/')
class Module1List(Resource):
    @api.doc('list_partners')
    @api.marshal_list_with(module1)
    def get(self):
        '''List all Items'''
        return LIST1

    @api.expect(module1)
    @api.marshal_with(module1)
    def post(self):
        new_partner = request.get_json()
        new_partner['id']=len(LIST1)+1
        LIST1.append(new_partner)
        return {'result':'Partner Added'}, 201


@api.route('/<id>')
@api.param('id', 'The partner identifier')
@api.response(404, 'Partner not found')
class Partner(Resource):
    @api.doc('get_partner')
    @api.marshal_with(module1)
    def get(self, id):
        '''Partner details by name'''
        for item in LIST1:
            if item['id'] == id:
                return item
        api.abort(404)