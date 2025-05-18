# 🧠 WAGMI Test API

A simple Django REST API with a single route: `POST /wagmi`, which intelligently responds based on input.

## 📌 Features

-   `POST /wagmi` endpoint:
    -   **Addition mode**: Accepts JSON with `a` and `b` values, returns their sum if valid.
    -   **Ping mode**: Returns a timestamp and message if no body is provided.
-   Input validation: Ensures `a` and `b` are non-negative numbers and their sum ≤ 100.
-   Deployed on [Railway](https://railway.app/).

---

## 🚀 Getting Started

### 🔧 Prerequisites

-   Python 3.9+
-   pip
-   virtualenv (optional but recommended)

---

### 🛠️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/roshankhanxox/wagmi_test_api.git
cd wagmi_test_api

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📁 Setup Environment

Create a `.env` file in the project root:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

## 🧪 Run the Server

python manage.py migrate
python manage.py runserver

## 🧾 Example Requests

### ✅ Addition

**Request:**

json
{
"a": 40,
"b": 55
}

response

{
"result": 95,
"a": 40,
"b": 55,
"status": "success"
}

```

```
