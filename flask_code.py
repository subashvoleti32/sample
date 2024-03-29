# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# schemas.py
from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String()
    user_id = fields.Integer(required=True)



# schemas.py
from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String()
    user_id = fields.Integer(required=True)


# Create a task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], user_id=data['user_id'])
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task), 201

# Read all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return task_schema.jsonify(tasks, many=True)

# Read a single task
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return task_schema.jsonify(task)

# Update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.user_id = data['user_id']
    db.session.commit()
    return task_schema.jsonify(task)

# Delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204  # No content
python
from app import db
db.create_all()
exit()



Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
    engine = self.engines[key]
             ^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 687, in engines
    app = current_app._get_current_object()  # type: ignore[attr-defined]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
>>> db.create_all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
    engine = self.engines[key]
             ^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 687, in engines
    app = current_app._get_current_object()  # type: ignore[attr-defined]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
>>> db.create_all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
    engine = self.engines[key]
             ^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_sqlalchemy\extension.py", line 687, in engines
    app = current_app._get_current_object()  # type: ignore[attr-defined]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\10722751\AppData\Local\Programs\Python\Python311\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information










 curl -X POST -H "Content-Type: application/json" -d '{"title": "Sample Task", "description": "This is a sample task.", "user_id": 1}' http://127.0.0.1:5000/tasks



                                             curl -X POST -H "Content-Type: application/json" -d '{"title": "Sample Task", "description": "This is a sample task.", "user_id": 1}' http://127.0.0.1:5000/tasks

