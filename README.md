# REST API Data Explorer

A Python-based REST API project demonstrating how applications retrieve data from external services using HTTP GET requests. The application consumes JSON data from a public REST API, extracts selected information, processes it, and stores the result locally.

## Project Objective

The goal is to understand the REST API integration workflow:

**Python Application → GET Request → REST API → JSON Response → Data Extraction → Processing → Local JSON Storage**

## Learning Outcomes

- Understand REST APIs and external services
- Send HTTP GET requests using Python
- Use the `requests` library
- Handle HTTP response status codes
- Receive and parse JSON responses
- Extract values from nested JSON structures
- Build a reusable API client class
- Handle connection, timeout, HTTP, and JSON errors
- Transform API data into a simplified structure
- Search and filter retrieved data
- Retrieve a specific resource by ID
- Save processed data to a JSON file
- Manage project dependencies with `requirements.txt`

## Features

- Connects to the JSONPlaceholder REST API
- Retrieves a collection of users
- Retrieves an individual user by ID
- Extracts ID, name, username, email, city, and company
- Handles common API request failures
- Provides user search/filter functionality
- Displays basic API data statistics
- Saves processed API data to `data/users.json`
- Uses a reusable `APIClient` class

## Technologies Used

- Python
- Requests
- REST API
- JSON
- HTTP
- Git & GitHub

## API Used

This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free fake REST API for testing and learning.

Main endpoint:

```text
https://jsonplaceholder.typicode.com/users
```

Individual user endpoint:

```text
https://jsonplaceholder.typicode.com/users/{id}
```

## Project Structure

```text
REST_API_Data_Explorer/
│
├── api_client.py
├── main.py
├── requirements.txt
├── README.md
│
└── data/
    └── users.json
```

| File | Purpose |
|---|---|
| `api_client.py` | Reusable `APIClient` class for API communication |
| `main.py` | Runs the application and processes API data |
| `requirements.txt` | Project dependency |
| `data/users.json` | Processed API response |
| `README.md` | Project documentation |

## API Client

API communication is separated into a reusable `APIClient` class.

The client builds API URLs, sends GET requests, supports query parameters, uses request timeouts, checks HTTP errors, and handles connection and JSON failures.

Example:

```python
client = APIClient("https://jsonplaceholder.typicode.com")
users = client.get("/users")
```

## Data Extraction

The API returns detailed user objects. The application extracts only the required information:

```text
ID
Name
Username
Email
City
Company
```

Nested JSON data is accessed with:

```python
user["address"]["city"]
user["company"]["name"]
```

## Error Handling

The application handles common API failures including:

- Request timeout
- Connection error
- HTTP error
- Invalid JSON response

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/REST_API_Data_Explorer.git
cd REST_API_Data_Explorer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Current dependency:

```text
requests==2.34.2
```

### 3. Run the application

```bash
python main.py
```

## Example Output

```text
===== REST API DATA EXPLORER =====

ID       : 1
Name     : Leanne Graham
Username : Bret
Email    : Sincere@april.biz
City     : Gwenborough
Company  : Romaguera-Crona
----------------------------------------
```

The application retrieves and processes 10 user records and saves the selected information to:

```text
data/users.json
```

## REST API Workflow

```text
1. Application starts
        ↓
2. APIClient is initialized
        ↓
3. GET request is sent
        ↓
4. REST API returns HTTP response
        ↓
5. JSON response is parsed
        ↓
6. Required fields are extracted
        ↓
7. Data is processed
        ↓
8. Results are displayed
        ↓
9. Processed data is saved locally
```

## Real-World Applications

The same REST API concepts can be applied to:

- Weather APIs
- Maps and location services
- Payment services
- Social media APIs
- AI and machine learning APIs
- E-commerce services
- Government data services
- Business and analytics platforms

## Key Takeaway

This project demonstrates how a Python application can retrieve structured information from an external service, process the response, extract useful data, and store the result for further use.

## Project Status

**Completed Successfully**
