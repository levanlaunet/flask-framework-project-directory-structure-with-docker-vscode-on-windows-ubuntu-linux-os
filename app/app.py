# LAU LE - https://levanlau.net
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!!!'

if __name__ == '__main__':
    app.run(debug=True)

# 
# from flask import Flask
# from database import database

# # blueprint import
# from apps.app1.views import app1
# from apps.app2.views import app2

# def create_app():
#     app = Flask(__name__)
#     # setup with the configuration provided
#     app.config.from_object('config.DevelopmentConfig')
    
#     # setup all our dependencies
#     database.init_app(app)
    
#     # register blueprint
#     app.register_blueprint(app1)
#     app.register_blueprint(app2, url_prefix="/app2")
    
#     return app

# if __name__ == "__main__":
#     create_app().run()
