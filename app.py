from flask import Flask, request, jsonify
import controllers.customer_controller as customer_controller
import controllers.engineer_controller as engineer_controller
import controllers.complaint_controller as complaint_controller
import controllers.job_controller as job_controller

app = Flask(__name__)


# -------> Customers endpoints routes <-------

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json
        customer_controller.create_customer(data['name'], data['email'], data['phone_number'])
        return jsonify({"Success":"Customer added into the database!!"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

@app.route('/customers', methods=['GET'])
def get_all_customers():
    try:
        customers = customer_controller.get_all_customers()
        if customers:
            return jsonify(customers)
        return jsonify({"Error": "Customers not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400
    
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = customer_controller.get_customer(customer_id)
        if customer:
            return jsonify(customer)
        return jsonify({"Error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        data = request.json
        customer = customer_controller.update_customer(
            customer_id=customer_id,
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number'],
        )
        if customer:
            return jsonify(customer)
        return jsonify({"Error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def api_delete_customer(customer_id):
    try:
        customer_controller.delete_customer(customer_id)
        return jsonify({"Success": "Customer deleted"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


# -------> Engineers endpoints routes <-------

@app.route('/engineers', methods=['POST'])
def create_engineer():
    try:
        data = request.json
        engineer = engineer_controller.create_engineer(data['name'], data['designation'])
        return jsonify(engineer), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/engineers/<int:engineer_id>', methods=['GET'])
def get_engineer(engineer_id):
    try:
        engineer = engineer_controller.get_engineer(engineer_id)
        if engineer:
            return jsonify(engineer)
        return jsonify({"Error": "Engineer not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/engineers/<int:engineer_id>', methods=['PUT'])
def update_engineer(engineer_id):
    try:
        data = request.json
        engineer = engineer_controller.update_engineer(
            engineer_id,
            name=data['name'],
            designation=data['designation'],
        )
        if engineer:
            return jsonify(engineer)
        return jsonify({"Error": "Engineer not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


# -------> Complaints endpoints routes <-------

@app.route('/complaints', methods=['POST'])
def create_complaint():
    try:
        data = request.json
        complaint_controller.create_complaint(
            customer_id=data['customer_id'],
            category=data['category'],
            description=data['description'],
            priority=data['priority'],
            engineer_id=data['engineer_id'],
        )
        return jsonify({"Success":"Complaint added into the database!!"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/complaints', methods=['GET'])
def get_complaints():
    try:
        complaints = complaint_controller.get_all_complaints()
        if complaints:
            return jsonify(complaints)
        return jsonify({"Error": "Complaint not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/complaints/<int:complaint_id>', methods=['GET'])
def get_complaint(complaint_id):
    try:
        complaint = complaint_controller.get_complaint(complaint_id)
        if complaint:
            return jsonify(complaint)
        return jsonify({"Error": "Complaint not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/complaints/<int:complaint_id>', methods=['PUT'])
def update_complaint(complaint_id):
    try:
        data = request.json
        complaint = complaint_controller.update_complaint(
            complaint_id,
            status=data['status'],
            engineer_id=data['engineer_id'],
        )
        if complaint:
            return jsonify(complaint)
        return jsonify({"Error": "Complaint not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint(complaint_id):
    try:
        complaint = complaint_controller.delete_complaint(complaint_id)
        if complaint:
            return jsonify(complaint)
        return jsonify({"Error": "Complaint not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


# -------> Jobs endpoints routes <-------

@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        data = request.json
        job = job_controller.create_job(
            complaint_id=data['complaint_id'],
            engineer_id=data['engineer_id'],
            status=data['status'],
            comment=data['comment'],
        )
        return jsonify(job), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    try:
        job = job_controller.get_job(job_id)
        if job:
            return jsonify(job)
        return jsonify({"Error": "Job not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = job_controller.get_all_jobs()
        if jobs:
            return jsonify(jobs)
        return jsonify({"Error": "Job not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        data = request.json
        job = job_controller.update_job(
            job_id,
            status=data['status'],
            comment=data['comment'],
        )
        if job:
            return jsonify(job)
        return jsonify({"Error": "Job not found"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
