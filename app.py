from flask import Flask
from flask_restful import  Api
from resources.campos import Campos, Campo
from views import views
from auth import auth


app = Flask(__name__)
api = Api(app)


api.add_resource(Campos, '/campos')
api.add_resource(Campo, '/campos/<string:nm_var>')
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')




if __name__ == '__main__':
    app.run(debug=True)

