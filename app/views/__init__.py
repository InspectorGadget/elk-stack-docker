import json

from flask import Blueprint, request

from app import db, es
from app.models.student import Student

blueprint = Blueprint('views', __name__)

@blueprint.route('/')
def index():
    return 'Hello, World!'

@blueprint.route('/students')
def students():
    _students = es.search(
        index="students", 
        body={}
    )
    _students = [
        {
            'id': int(student['_id']),
            'name': student['_source']['name'],
            'is_deleted': student['_source']['is_deleted']
        }
        for student in _students['hits']['hits']
        if (
            student['_source']['is_deleted'] == False
        )
    ][::-1]

    return _students

@blueprint.route('/students', methods=['POST'])
def create_student():
    def validate(request):
        if 'name' not in request:
            return False
        return True
    
    if not request.json:
        return 'Request must be JSON', 400
    if not validate(request.json):
        return 'Invalid request', 400
    
    new_student = Student(
        name=request.json['name'].upper()
    )
    db.session.add(new_student)
    db.session.commit()

    return new_student.serialize(), 201


@blueprint.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    def validate(request):
        if 'name' not in request:
            return False
        return True
    
    if not request.json:
        return 'Request must be JSON', 400
    if not validate(request.json):
        return 'Invalid request', 400
    
    student = Student.query.get(student_id)
    if not student:
        return 'Student not found', 404
    
    student.name = request.json['name'].upper()
    db.session.commit()

    return student.serialize(), 200

@blueprint.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return 'Student not found', 404
    
    student.is_deleted = True
    db.session.add(student)
    db.session.commit()

    return 'Set as Deleted.', 200
