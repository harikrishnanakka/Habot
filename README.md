# Habot Project

## Overview

The Habot Project is a Django-based application designed for employee management. This project provides a robust backend for managing employee data, including authentication features, CRUD operations for employee records, and token-based authentication using JWT (JSON Web Tokens). 

The application allows for the creation, retrieval, updating, and deletion of employee records, making it suitable for companies looking to streamline their HR processes.

### Key Features
- User registration and authentication
- Employee management with role-based access
- Secure JWT token authentication
- Pagination and filtering for employee lists

## Requirements

This project requires Python 3.8 or higher. The dependencies are managed using a virtual environment. 

### Dependencies
- Django
- Django REST Framework
- djangorestframework-simplejwt
- Other packages as specified in `requirements.txt`

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
 bash
 
       git clone https://github.com/harikrishnanakka/Habot_Presentation.git
   
       cd Habot_Presentation

### 2. Create a Virtual Environment

It is recommended to create a virtual environment for your project to manage dependencies separately.

       python -m venv myenv

### 3. Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system.

On Windows:

           myenv\Scripts\activate

On macOS/Linux:

           source myenv/bin/activate


### 4. Install Dependencies


Once the virtual environment is activated, install the required packages using the following command:

            pip install -r requirements.txt


### 5. Run Migrations

Before starting the server, make sure to run migrations to set up your database:

           python manage.py migrate

### 6. Start the Development Server

You can now start the Django development server:

            python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/

### API Endpoints


The following are the main API endpoints available in the application:

## Authentication

POST /api/token/: Obtain JWT token using username and password.

POST /api/register/: Register a new user.

POST /api/token/refresh/: Refresh Token.

## Employee Management

GET /api/employees/: Retrieve a list of employees with pagination and filtering options.

POST /api/employees/: Create a new employee record.

GET /api/employees/{id}/: Retrieve a specific employee record by ID.

PUT /api/employees/{id}/: Update an existing employee record.

DELETE /api/employees/{id}/: Delete an employee record.

## Usage Example

You can use tools like Postman or cURL to interact with the API. For example, to create an employee, you need to include the JWT token in the Authorization header:

### 1.Obtain Token:

POST /api/token/

Content-Type: application/json

        {

          "username": "your_username",
    
          "password": "your_password"
    
        }

### 2.Create Employee:

POST /api/employees/

Authorization: Bearer YOUR_ACCESS_TOKEN

Content-Type: application/json

{

    "name": "John Doe",
    
    "department": "HR",
    
    "role": "Manager"
    
}

### 3. Deleting an Employee

To delete an employee record, send a DELETE request with the employee's ID:

       DELETE /api/employees/{id}/
       
       Authorization: Bearer YOUR_ACCESS_TOKEN

### 4. Modifying an Employee

To modify an existing employee record, send a PUT request with the employee's ID:

       PUT /api/employees/{id}/
       
       Authorization: Bearer YOUR_ACCESS_TOKEN
       
       Content-Type: application/json

       {
       
     "name": "Jane Doe",
     
     "department": "Finance",
     
     "role": "Senior Manager"
     
     }

### 5. Filtering Employees

You can filter the list of employees by specific fields using query parameters:

      GET /api/employees/?department=HR&role=Manager
      
      Authorization: Bearer YOUR_ACCESS_TOKEN

### 6. Pagination

To paginate the list of employees, you can use query parameters for page number and page size:

       GET /api/employees/?page=1&page_size=10
       
       Authorization: Bearer YOUR_ACCESS_TOKEN


## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1.Fork the repository.

2.Create a new branch for your feature or bug fix.

3.Make your changes and commit them with clear messages.

4.Push your changes to your fork.

5.Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

1.Django

2.Django REST Framework

3.djangorestframework-simplejwt


### Instructions to Use
- Make sure to replace `<your-repository-url>` with the actual URL of your Git repository.
  
- Feel free to modify any section to better suit your project specifics.

This `README.md` now provides a clear overview of your project along with the necessary details for setup and usage. Let me know if you need any further changes!












