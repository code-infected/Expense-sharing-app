# Expense Sharing App (Backend)

A FastAPI-based backend service for managing users and expenses, allowing users to split expenses and track balances.

## Features

- **User Management:** Create and retrieve user details.
- **Expense Management:** Add and track expenses, split them among users using different methods.
- **Data Validation:** Ensures input data integrity, like checking if percentages add up correctly.
- **Download Balance Sheet:** Provides a CSV download of the balance sheet.

## Requirements

- Python 3.10+
- Firebase Admin SDK
- FastAPI
- Uvicorn (ASGI server)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/expense-sharing-api.git
cd expense-sharing-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Firebase Setup

1. Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
2. Download the `credentials.json` file for your project and place it in the root directory.
3. Create a `.env` file in the root directory with the following content:

```
FIREBASE_CREDENTIALS_PATH=./credentials.json
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### User Endpoints

#### 1. Create User

- **URL:** `/api/v1/users`
- **Method:** `POST`
- **Body:**
  ```json
  {
      "email": "johndoe@example.com",
      "name": "John Doe",
      "mobile_number": "1234567890"
  }
  ```
- **Response:**
  ```json
  {
      "message": "User created successfully"
  }
  ```

#### 2. Retrieve User Details

- **URL:** `/api/v1/users/{email}`
- **Method:** `GET`
- **Response:**
  ```json
  {
      "email": "johndoe@example.com",
      "name": "John Doe",
      "mobile_number": "1234567890"
  }
  ```

### Expense Endpoints

#### 1. Add Expense

- **URL:** `/api/v1/expenses`
- **Method:** `POST`
- **Body:**
  ```json
  {
      "description": "Dinner",
      "total_amount": 3000,
      "split_method": "equal",
      "payer": "johndoe@example.com",
      "participants": [
          "johndoe@example.com",
          "janedoe@example.com",
          "alex@example.com"
      ]
  }
  ```
- **Response:**
  ```json
  {
      "message": "Expense added successfully"
  }
  ```

#### 2. Retrieve Individual User Expenses

- **URL:** `/api/v1/expenses/{email}`
- **Method:** `GET`
- **Response:**
  ```json
  [
      {
          "description": "Dinner",
          "total_amount": 3000,
          "split_method": "equal",
          "payer": "johndoe@example.com",
          "participants": [
              "johndoe@example.com",
              "janedoe@example.com",
              "alex@example.com"
          ],
          "amount_due": {
              "johndoe@example.com": 1000,
              "janedoe@example.com": 1000,
              "alex@example.com": 1000
          }
      }
  ]
  ```

#### 3. Retrieve Overall Expenses

- **URL:** `/api/v1/expenses`
- **Method:** `GET`
- **Response:**
  ```json
  [
      {
          "description": "Dinner",
          "total_amount": 3000,
          "split_method": "equal",
          "payer": "johndoe@example.com",
          "participants": [
              "johndoe@example.com",
              "janedoe@example.com",
              "alex@example.com"
          ],
          "amount_due": {
              "johndoe@example.com": 1000,
              "janedoe@example.com": 1000,
              "alex@example.com": 1000
          }
      },
      {
          "description": "Shopping",
          "total_amount": 5000,
          "split_method": "exact",
          "payer": "janedoe@example.com",
          "participants": [
              "janedoe@example.com",
              "alex@example.com"
          ],
          "amount_due": {
              "janedoe@example.com": 3000,
              "alex@example.com": 2000
          }
      }
  ]
  ```

#### 4. Download Balance Sheet

- **URL:** `/api/v1/expenses/download`
- **Method:** `GET`
- **Response:**
  - A CSV file download containing the details of all expenses and the amounts owed by each user.

## API Testing with Postman

1. **Open Postman:**
   - You can use the [web-based version](https://web.postman.co/) or the desktop app.

2. **Create a New Request:**
   - Click on the **New** button and select **HTTP Request**.

3. **Set Up the Request:**
   - **Method:** Choose the appropriate method (GET, POST).
   - **URL:** Enter the endpoint URL (e.g., `http://127.0.0.1:8000/api/v1/users`).

4. **Headers:**
   - Add `Content-Type: application/json` if your request includes a body.

5. **Body:**
   - For POST requests, select **raw** and **JSON** format, then enter your JSON data.

6. **Send Request:**
   - Click the **Send** button to execute the request.
   - View the response in the bottom panel.

7. **Save Requests:**
   - Save your requests in a Postman collection for easy access.

## Project Structure

```
expense-sharing-app/
│
├── app/
│   ├── main.py              # Main application entry point
│   ├── models/
│   │   ├── user_model.py    # User model
│   │   └── expense_model.py # Expense model
│   ├── controllers/
│   │   ├── user_controller.py   # User controller
│   │   └── expense_controller.py# Expense controller
│   ├── utils/
│       ├── firebase.py      # Firebase configuration and setup
│
├── credentials.json         # Firebase credentials
├── .env                     # Environment variables
├── README.md                # Documentation
├── requirements.txt         # Python dependencies
└── .venv/                   # Virtual environment
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
