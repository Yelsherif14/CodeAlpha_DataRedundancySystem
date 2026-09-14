# Data Redundancy Removal System

A Flask-based web application developed to detect and prevent duplicate user data before storing it in a SQLite database.

The system validates user input, checks for duplicate email addresses, and stores only unique and valid records.

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
├── database/
│   └── db.py
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── screenshots/
│   ├── application.png
│   ├── ec2-instance.png
│   ├── flask-terminal.png
│   ├── security-group.png
│   └── project-files.png
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
* Deployed on AWS EC2

## Testing

The application was tested using Pytest.

All implemented tests passed successfully:

```text
4 passed
```

The tests cover:

* Adding a unique user
* Rejecting duplicate email addresses
* Rejecting invalid email addresses
* Rejecting empty fields

## AWS EC2 Deployment

The application was deployed and tested on an Ubuntu AWS EC2 instance.

### 1. EC2 Instance

An Ubuntu EC2 instance was created and configured to host the Flask application.

![EC2 Instance](screenshots/ec2-instance.png)

*Ubuntu EC2 instance used to deploy the application.*

### 2. Project Files

The project was cloned from GitHub onto the EC2 instance.

![Project Files](screenshots/project-files.png)

*Project files after cloning the GitHub repository on the EC2 instance.*

### 3. Running Flask

The Flask application was configured to listen on all network interfaces using port `5000`.

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

![Flask Running](screenshots/flask-terminal.png)

*Flask development server running successfully on the AWS EC2 instance.*

### 4. Security Group Configuration

Inbound TCP traffic was allowed on port `5000` to make the Flask application accessible from the internet.

![Security Group](screenshots/security-group.png)

*AWS Security Group rule allowing inbound traffic on port 5000.*

### 5. Application Running

The deployed application was successfully accessed through the EC2 public IPv4 address.

![Application Running](screenshots/application.png)

*Data Redundancy Removal System running successfully on AWS EC2.*

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_DataRedundancySystem.git
cd CodeAlpha_DataRedundancySystem
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install flask pytest
```

Run the application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Running Tests

From the project root directory:

```bash
pytest
```

Expected result:

```text
4 passed
```

## Deployment Environment

* Cloud Provider: AWS
* Service: Amazon EC2
* Operating System: Ubuntu Server
* Application Framework: Flask
* Database: SQLite
* Application Port: 5000

## Internship

This project was developed as part of the **CodeAlpha Cloud Computing Internship**.

**Task:** Data Redundancy Removal System

## Author

**Youssef Hisham Ali El-Sherif**
