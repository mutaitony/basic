from __init__ import app, db
import url

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=app.config.get('PORT'), debug=True, host="0.0.0.0")