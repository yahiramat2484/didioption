from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate

# Database
db = SQLAlchemy(session_options={"autoflush": False,})

# Login
login_manager = LoginManager()

# Mail
mail = Mail()

# Migrations
migrate = Migrate()
