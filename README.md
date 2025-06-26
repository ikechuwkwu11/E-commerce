# 🛒 Django E-commerce REST API

This is a full-featured **E-commerce backend API** built using **Django and Django REST Framework (DRF)**. It supports product listings, user accounts, order processing, vendor management, and customer reviews.
Tested thoroughly using **Postman**.

---

## 📁 Project Structure

ecommerce/
- products/ # Handles product creation, listing, updating, and stock control
├── orders/ # Order creation, item validation, and inventory updates
├── vendors/ # Vendor registration and store management
├── users/ # User registration, login, authentication
├── reviews/ # Customer reviews and ratings for products
├── manage.py


---

## 🔧 Features

### ✅ Users
- Register and login using Token Authentication
- View user profile

### ✅ Products
- Vendor-based product creation
- Price, stock, and description management
- Only vendors can manage their own products

### ✅ Orders
- Place orders for one or multiple products
- Stock validation before order processing
- Atomic transaction for consistency

### ✅ Vendors
- Vendors are linked to registered users
- Each vendor manages their own store/products

### ✅ Reviews
- Authenticated users can leave product reviews
- Ratings and text feedback supported

---

## 🧪 Testing with Postman

All endpoints were tested and validated using **Postman**:

- `POST /api/users/register/` – Create user
- `POST /api/users/login/` – Login and get token
- `POST /api/products/add/` – Add new product (vendor only)
- `POST /api/orders/add/` – Place a new order
- `GET /api/products/` – List all products
- `POST /api/reviews/add/` – Submit a product review

You can import the Postman collection via a provided JSON file (if included).

---

## 📂 API Endpoints Overview
| Module   | Endpoint Example         | Method | Description         |
| -------- | ------------------------ | ------ | ------------------- |
| Users    | `/api/users/register/`   | POST   | Register new user   |
| Products | `/api/products/`         | GET    | List all products   |
| Products | `/api/products/add/`     | POST   | Vendor adds product |
| Orders   | `/api/orders/add/`       | POST   | Place new order     |
| Vendors  | `/api/vendors/register/` | POST   | Register vendor     |
| Reviews  | `/api/reviews/add/`      | POST   | Submit a review     |
