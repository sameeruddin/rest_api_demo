## Environment set-up
```
conda create -n env_restapi_test python=3.9
pip install Flask
pip install psycopg2-binary
pip install requests
pip install jsonify
```

## Usecase
Complaint management system - Complaints are registered from the customers and the jobs are assigned to skilled engineers. Engineers process the jobs and updates the job status based on the work needed to be done. Complaints also have a priority schedule such as high, low, medium based on its emergency.

### 1 - Resources

Customers
    Entity: Customer
    Attributes: customer_id, name, phone_number


Engineers
    Entity: Engineer
    Attributes: engineer_id, name, designation


Complaints
    Entity: Complaint
    Attributes: complaint_id, customer_id, engineer_id, category, description, priority, status


Jobs
    Entity: Job
    Attribute: job_id, complaint_id, engineer_id, status, comment


### 2 - Data models

Customer model:
    {
        "customer_id": "integer",
        "name": "string",
        "phone_number": "integer",
        "created_at": "datetime",
        "updated_at": "datetime"
    }


Engineer model:
    {
        "engineer_id": "integer",
        "name": "string",
        "designation": "string",
        "created_at": "datetime",
        "updated_at": "datetime"
    }

Complaint model:
    {
        "complaint_id": "integer",
        "customer_id": "integer",
        "engineer_id": "integer",
        "category": "string",
        "description": "string",
        "priority": "string",
        "status": "string",
        "created_at": "datetime",
        "updated_at": "datetime"
    }

Job model:
    {
        "job_id": "integer",
        "complaint_id": "integer",
        "engineer_id": "integer",
        "status": "string",
        "comment": "string",
        "created_at": "datetime",
        "updated_at": "datetime"
    }


### DB schema (PostgreSQL database)

```
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE engineers (
    engineer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    designation VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE complaints (
    complaint_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    engineer_id INT REFERENCES engineers(engineer_id) ON DELETE SET NULL,
    category VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    priority VARCHAR(10) NOT NULL CHECK (priority IN ('High', 'Medium', 'Low')),
    status VARCHAR(20) NOT NULL DEFAULT 'Open' CHECK (status IN ('Open', 'In Progress', 'Closed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    complaint_id INT NOT NULL REFERENCES complaints(complaint_id) ON DELETE CASCADE,
    engineer_id INT NOT NULL REFERENCES engineers(engineer_id) ON DELETE CASCADE,
    status VARCHAR(20) NOT NULL DEFAULT 'Assigned' CHECK (status IN ('Assigned', 'In Progress', 'Resolved')),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger and Functions for auto-updatethe timestamp

CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_customer_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_engineer_timestamp
BEFORE UPDATE ON engineers
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_complaint_timestamp
BEFORE UPDATE ON complaints
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_job_timestamp
BEFORE UPDATE ON jobs
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Replace 'customers_customer_id_seq' with the actual sequence name if different
SELECT setval('customers_customer_id_seq', (SELECT MAX(customer_id) FROM customers) + 1);
--- use the above code only, when you have issues with records insertion

```

### 3 - API endpoints

``` POST \customers ```


``` GET \customers ```


``` GET \customers\<customer_id> ```


``` PUT \customers\<customer_id> ```


``` DELETE \customers\<customer_id> ```