# 📚 **Zendo Application**

## 🚀 **1. Project Overview**

- **Description:** A simple to-do application with basic CRUD functionality (Create, Read, Update, Delete).
- **Purpose:** Help users manage their tasks efficiently.
- **Technologies:** Django (Backend), Django REST Framework (API), PostgreSQL (Database).
- **Core Features (Current State):**
  - Add tasks
  - View tasks

### 📂 **2. Directory Structure**

- **backend/**: Django project files
  - `settings.py`: Django settings
- **zendo_app/**: Main application logic
  - `tests/`: Test cases
  - `models.py`: Database models
  - `serializers.py`: API serializers
  - `urls.py`: URL routing
  - `views.py`: Application logic (GET and POST tasks)
- **utilities/**: Helper functions
- **manage.py**: Django management script

### 📝 **3. API Documentation**

#### **Endpoints (Current State):**

| **Method** | **Endpoint**      | **Description**        | **Status Codes** |
|------------|-------------------|-------------------------|------------------|
| `GET`      | `/tasks/`         | Retrieve all tasks     | `200 OK`, `400 Bad Request` |
| `POST`     | `/tasks/`         | Create a new task      | `201 Created`, `400 Bad Request` |

### 🛠️ **4. Testing Documentation**

- **Framework:** Django's `TestCase` & `APITestCase`
- **Focus Areas (Current State):**
  - `GET` endpoints return correct data and status codes
  - `POST` endpoints validate and create tasks correctly
- **Testing Command:**

```bash
python3 manage.py test
```

### 📊 **5. Database Schema**

- **Task Model (Current State):**
  - `title`: CharField (Required)
  - `completed`: BooleanField (Default: False)

### 📢 **6. Future Improvements**

- Add `PUT` and `DELETE` functionality
- Add user authentication
- Implement pagination for task lists
- Add frontend UI functionality

---

This documentation reflects the **current state** of the application and will be updated as new features are implemented. 🚀
