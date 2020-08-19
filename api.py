from app import app
from app.models import Contact

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Contact': Contact}
