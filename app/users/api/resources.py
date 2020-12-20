from flask import request, Blueprint
from flask_restful import Api, Resource

from . import USERS_PER_PAGE
from .schemas import ProfileSchema
from ..models import User
from ...common.error_handling import ObjectNotFound, AppErrorBaseClass

profile_v1_0_bp = Blueprint('profile_v1_0_bp', __name__)

profile_schema = ProfileSchema()

api = Api(profile_v1_0_bp)


class ProfileResource(Resource):
    def get(self):
        username = request.args.get('username') if request.args.get('username') is not None else None
        id = int(request.args.get('id')) if request.args.get('id') is not None else None

        if username is None:
            if id is None:
                raise AppErrorBaseClass('Query parameters must have an username or an id')
            else:
                profile = User.get_by_id(id)
                if profile is None:
                    raise ObjectNotFound('The profile not exists!')
                result = profile_schema.dump(profile)
                return result, 200
        else:
            profile = User.get_by_username(username)
            if profile is None:
                raise ObjectNotFound('The profile not exists!')
            result = profile_schema.dump(profile)
            return result, 200


api.add_resource(ProfileResource, '/api/v1/profiles/', endpoint='profile_resource')
