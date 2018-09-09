from options.app import app, create_app
from options.extensions import db
from options.Configuration.development import Development

app = create_app(app, Development())

application = app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)