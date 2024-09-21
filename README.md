# SwiftComp-API

**SwiftComp-API** is a FastAPI-based backend designed to perform calculations related to composite laminate materials. It exposes various endpoints for computing engineering constants, plate properties, 3D laminate properties, and more. This API is suitable for researchers, engineers, and developers working in composite materials and structural analysis.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Versioned API:** Support for multiple versions of the API, with versioning (v1, v2) for backward compatibility.
- **Material Property Calculations:** Endpoints to calculate various laminate engineering constants and composite properties.
- **Lightweight & Fast:** Built using FastAPI, ensuring high performance and minimal latency.
- **Modular Architecture:** Separation of concerns using routers, services, and utility functions for better maintainability.
- **Extensible:** Easy to add new endpoints and services for additional material computations.

---

## Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python-type hints.
- **Python 3.7**: Programming language used to implement the logic.
- **Pytest**: A robust testing framework for Python.
- **Uvicorn**: ASGI server used for serving FastAPI applications.
- **Virtual Environment (venv)**: For dependency isolation.

---

## Installation

To set up the project locally, follow these steps:

### Prerequisites
- Python 3.7 or higher.
- Git installed on your system.

### Step-by-Step Guide

1. **Clone the repository**:
```bash
git clone https://github.com/wenbinyugroup/swiftcomp-api.git
cd swiftcomp-api
```

2. **Create and activate a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the FastAPI application locally**:
```bash
uvicorn app.main:app --reload
```

This will start the SwiftComp API server at http://127.0.0.1:8000.

## API Documentation
FastAPI automatically generates interactive API documentation using **Swagger** and **Redoc**. Once the server is running, you can access the documentation at:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Sample Endpoints
* **GET /**: Root endpoint, returns a welcome message.
* **POST /api/v1/lamina_engineering_constants**: Calculates the lamina engineering constants based on the provided material properties.
* **POST /api/v1/laminate_plate_properties**: Calculates the laminate plate properties.
* **POST /api/v1/laminate_3d_properties**: Computes the 3D properties of laminate.
* **POST /api/v1/udfrc_properties**: Calculates UDFRC properties.

## Testing
The repository includes unit tests using `pytest`. To run the tests:

1. Ensure you are in the virtual environment.
2. Run the following command:
```bash
PYTHONPATH=./ pytest
```

## Contributing
We welcome contributions to **SwiftComp-API**! Here's how you can help:

1. **Fork the repository**.
2. **Create a new feature branch**:
```bash
git checkout -b feature/your-feature-name
```
3. **Commit your changes**:
```bash
git commit -m "Add your message"
```
4. **Push to the branch**:
```bash
git push origin feature/your-feature-name
```
5. **Create a pull request**: Describe the changes you’ve made.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.