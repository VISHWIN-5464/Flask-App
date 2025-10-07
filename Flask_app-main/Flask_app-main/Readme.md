# 🧮 Flask Inventory Management Web Application

> A complete Flask-based web application to manage products, locations, and product movements with dynamic inventory balance tracking and a clean, minimal UI.

---

## 🌟 Table of Contents
1. [📖 Introduction](#-introduction)
2. [🧩 Features](#-features)
3. [⚙️ Tech Stack](#️-tech-stack)
4. [🧱 Architecture Overview](#-architecture-overview)
5. [📂 Project Structure](#-project-structure)
6. [🪜 Installation Guide](#-installation-guide)
7. [🚀 Running the Application](#-running-the-application)
8. [🧭 App Navigation](#-app-navigation)
9. [🗃️ Database Schema](#️-database-schema)
10. [🔄 How the App Works](#-how-the-app-works)
11. [🖥️ UI Overview](#️-ui-overview)
12. [📦 Core Functionalities](#-core-functionalities)
13. [📊 Example Workflows](#-example-workflows)
14. [🧠 Business Logic Explained](#-business-logic-explained)
15. [🔧 Configuration Settings](#-configuration-settings)
16. [🧰 Utility Functions](#-utility-functions)
17. [🧪 Testing the Application](#-testing-the-application)
18. [🪄 Styling & Design Philosophy](#-styling--design-philosophy)
19. [💡 Best Practices Followed](#-best-practices-followed)
20. [🪶 Future Enhancements](#-future-enhancements)
21. [🌐 Deployment Guide](#-deployment-guide)
22. [🤝 Contributing Guidelines](#-contributing-guidelines)
23. [📜 License](#-license)
24. [🧑‍💻 Author](#-author)
25. [📸 Screenshots (Optional)](#-screenshots-optional)

---

## 📖 Introduction
The **Flask Inventory Management Web App** is a lightweight web application designed to help users **track products, warehouse locations, and product movements** efficiently.

It provides:
- A clean and simple **web interface**
- A **Flask backend** using **SQLite3**
- Dynamic **inventory balance reports**
- Easy management for small-scale inventory systems

It is ideal for small businesses, students learning Flask, or developers exploring CRUD applications in Flask.

---

## 🧩 Features

✅ Add, view, and manage **Products**  
✅ Add, view, and manage **Locations**  
✅ Record **Product Movements** between locations  
✅ Generate **Real-time Product Balance Reports**  
✅ Simple and clean **Minimal UI**  
✅ Data persisted in **SQLite3**  
✅ **Lightweight, portable**, and runs locally  
✅ **Zero external dependencies** except Flask  
✅ Easy to extend with **authentication or CSV exports**

---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3 |
| **Database** | SQLite3 |
| **Server** | Flask’s built-in development server |
| **Version Control** | Git + GitHub |
| **Deployment Options** | Render, Railway, or Flask CLI |

---

## 🧱 Architecture Overview

The project follows a **Model-View-Controller (MVC)** inspired structure:

- **Model:** Handles SQLite database operations  
- **View:** Templates (HTML/CSS) rendered using Flask’s `render_template()`  
- **Controller:** Routes in `app.py` handling user requests and database logic

---

### 🧭 Data Flow

1. User submits a form (add product, location, or movement).  
2. Flask processes the request and updates the database.  
3. Data is retrieved and displayed on the web interface dynamically.  
4. Report page calculates product balance using SQL queries.

---

## 📂 Project Structure

Flask_app/
│
├── app.py # Main Flask application file
├── static/
│ └── style.css # Custom minimal CSS for all pages
├── templates/
│ ├── base.html # Shared layout (navbar, CSS link)
│ ├── home.html # Dashboard / landing page
│ ├── products.html # Add / View products
│ ├── locations.html # Add / View locations
│ ├── movements.html # Record and list movements
│ └── report.html # Product balance report
├── requirements.txt # Python dependencies (Flask)
└── README.md # Project documentation (this file)
🧭 App Navigation
Page	URL	Description
🏠 Home	/	Main navigation page
📦 Products	/products	Manage product list
🏭 Locations	/locations	Manage warehouse locations
🔄 Movements	/movements	Record product transfers
📊 Report	/report	View stock balance
🗃️ Database Schema

The app uses three main tables:

1. products
Column	Type	Description
id	INTEGER	Primary key
name	TEXT	Product name
2. locations
Column	Type	Description
id	INTEGER	Primary key
name	TEXT	Location name
3. movements
Column	Type	Description
id	INTEGER	Primary key
product_id	INTEGER	Foreign key (products.id)
from_location	INTEGER	Source location
to_location	INTEGER	Destination location
quantity	INTEGER	Number of items moved
timestamp	DATETIME	Movement date and time
🔄 How the App Works

User adds products and locations.

Movements are recorded (each with from/to and quantity).

Report queries the sum of all in/out quantities to display the current balance per location.

🖥️ UI Overview

Base Layout: simple navbar + container + footer

Home Page: quick overview & links

Forms: styled minimally, responsive, no JS dependencies

Report Page: table with dynamic SQL-based values

📦 Core Functionalities
➕ Add Product

Form input → insert into products table.

➕ Add Location

Form input → insert into locations table.

🔁 Add Movement

Form inputs (product, from_location, to_location, qty) → insert into movements.

📊 View Report

SQL query combines movements → calculates per-location balance.
