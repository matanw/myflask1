# This file contains an example Flask-User application.
# To keep the example simple, we are applying some unusual techniques:
# - Placing everything in one file
# - Using class-based configuration (instead of file-based configuration)
# - Using string-based templates (instead of file-based templates)

import datetime
import os
from flask import Flask, request, render_template_string
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

from sqlalchemy.orm import sessionmaker, scoped_session, exc


def create_app():
    """ Flask application factory """

    print()
    # Create Flask app load app.config
    app = Flask(__name__)
    #app.config.from_object(__name__ + '.ConfigClass')
    app.config.from_mapping(
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'msa.db'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'msa1.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # 'sqlite:///basic_app.sqlite',  # todo: delete 1, get app.instance_path
        RESTPLUS_SWAGGER_UI_DOC_EXPANSION='list',
        RESTPLUS_VALIDATE=True,
        RESTPLUS_MASK_SWAGGER=False,
        RESTPLUS_ERROR_404_HELP=False,
        DEBUG=True,
        SECRET_KEY='H@s@mb@H@s@mb@H@s@mb@'
    )
    print('sqlite:///' + os.path.join(app.instance_path, 'msa1.db'))
    # Initialize Flask-BabelEx
    babel = Babel(app)
    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    class ConfigurationEntity(db.Model):
        """Persistent entity representing a configuration property"""
        __tablename__ = 'configuration'
        key = db.Column(db.String(25), primary_key=True)
        value = db.Column(db.String(250), nullable=False)

        def __init__(self, key, value):
            self.key = key
            self.value = value
    # Create all database tables
    db.create_all()

    # The Members page is only accessible to authenticated users
    @app.route('/add')
    def add_conf():
        UPLOAD_CHUNK_SIZE_MB_PROP = "key"
        DEFAULTS= ConfigurationEntity(UPLOAD_CHUNK_SIZE_MB_PROP, "128")

        #get

        entity=""
        try:
            entity = ConfigurationEntity.query.filter( ConfigurationEntity.key == "key").one()
        except exc.NoResultFound:
            entity=DEFAULTS

        #put
        print (entity.value)

        entity.value ="new" +str(datetime.datetime.now())


        db.session.add(entity)
        db.session.commit()
        return render_template_string("abcd")


    return app


# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)