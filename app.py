from flask import Flask, jsonify, request
from flasgger import Swagger


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'My RESTFul Employee API',
    'description':'This is an Employee API',
    'ui version': 3
}

Swagger(app)

employees = [
{
	'id':1,
	'name': u'Bob colly',
	'email': u'collybob@gmail.com',
	'age': u'45',
	'department':u'operations',
	'reporting_date':u'20170310' 
},

{
	'id':2,
	'name': u'Jay Tim',
	'email': u'jay@gmail.com',
	'age': u'27',
	'department':u'operations',
	'reporting_date':u'3452097'
},

{
  'id':3,
  'name': u'Philip mwangi',
  'email': u'mwangip@gmail.com',
  'age': u'23',
  'department':u'logistics',
  'reporting_date':u'3452097'
}

]



@app.route('/employee', methods=['GET'])
def list_employees():
    """
    This endpoint returns a list of employees
    ---
    tags:
      - EmployeeApi
    responses:
      200:
        description: "Successfully got info"
        schema:
          id: return_test
          properties:
            result:
              type: string
              description: The test
              default: 'employees'

    """

    size = int(request.args.get('size', 1))
    return jsonify({"result": employees })

@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    This endpoint returns a single employee by passing the Id no of an employee
    ---
    paths:
    /employee/{employee_id}:
    get:
    tags:
      - EmployeeApi
    parameters:
      - name: employee_id
        in: path
        type: integer
        description: Get a single user by id
    responses:
      200:
        description: "Successfully got info"
        schema:
          id: user_response
          properties:
            result:
              type: string
              description: The employee
              default: 'employee'
    """
    for employee in employees:
      if employee['id'] == employee_id:
        return jsonify({'result': employee})
      return "Employee Id is not available"

@app.route('/employee', methods=['POST'])
def create_employee():
    """
    Adds an employee
    ---
    paths:
    /employee/:
    post:
    tags:
      - EmployeeApi
    parameters:
      - name: employee_name
        in: body
        required: true
        type: string
        description: Post employlee's name using json format
    responses:
      200:
        description: "Success"
        schema:
          id: user_response
          properties:
            result:
              type: string
              description: The created employee
              default: employee
    """

    if not request.json or not 'name' in request.json:
      abort(400)
    employee = {
      'id': employees[-1]['id'] + 1,
      'name':request.json['name'],
      'email': request.json.get('email', ""),
      'age': request.json.get('age'),
      'department': request.json.get('department'),
      'reporting_date': request.json.get('reporting_date')
    }
    employees.append(employee)
    return jsonify({'employee': employee}), 201

if __name__== '__main__':
  app.run(debug=True)

