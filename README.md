# Data Redundancy Removal System

A Flask-based web application designed to detect and prevent duplicate user data before storing it in a SQLite database.

The system validates user input, checks for duplicate email addresses, and stores only valid and unique records.

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* Pytest
* Git & GitHub
* AWS EC2

## Project Structure

```text
CodeAlpha_DataRedundancySystem/
│
├── app.py
├── data.db
│
├── database/
│   └── db.py
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_app.py
│
├── screenshots/
│   ├── application.png
│   ├── application-2.png
│   ├── application-3.png
│   ├── ec2-instance.png
│   ├── flask-terminal.png
│   ├── project-files.png
│   └── security-group.png
│
└── venv/
```

## Features

* Add new user records
* Validate required fields
* Validate email format
* Detect duplicate email addresses
* Prevent duplicate records
* Store valid and unique data in SQLite
* Automated testing using Pytest
* Deployment on AWS EC2

## Testing

The application was tested using Pytest.

All tests passed successfully:

```text
4 passed
```

### Tests Covered

* Adding a unique user
* Rejecting duplicate email addresses
* Rejecting invalid email addresses
* Rejecting empty fields

## AWS EC2 Deployment

The application was successfully deployed on an Ubuntu AWS EC2 instance.

### EC2 Instance

The application was hosted on an Ubuntu EC2 instance.

![EC2 Instance](screenshots/ec2-instance.png)

*Ubuntu EC2 instance used to host the application.*

### Project Files on EC2

The project was cloned from GitHub and configured on the EC2 instance.

![Project Files](screenshots/project-files.png)

*Project files after cloning the repository on the EC2 instance.*

### Flask Application Running

The Flask application was configured to listen on all network interfaces using port `5000`.

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

![Flask Running](screenshots/flask-terminal.png)

*Flask development server running successfully on the EC2 instance.*

### Security Group Configuration

Inbound TCP traffic was allowed on port `5000` through the EC2 Security Group.

![Security Group](screenshots/security-group.png)

*AWS Security Group configur*
