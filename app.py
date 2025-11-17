from flask import Flask,render_template, session, redirect,url_for
from config import Config
from model import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints (route modules)
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.manager import manager_bp
    from routes.emp import employee_bp
    
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(admin_bp)
    # app.register_blueprint(manager_bp)
    # app.register_blueprint(employee_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
    
    return app

# Create app instance
app = create_app()

@app.route('/')
def index():

    if 'username' in session:
        role = session.get('role')
        if role == 'admin':
            return redirect('/dashboard')
        elif role == 'manager':
            return redirect('/dashboard')
        else:
            return redirect('/dashboard')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)