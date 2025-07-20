# 📚 PageTurn – 2nd Hand Book Selling Platform

**PageTurn** is an online platform built to facilitate the buying and selling of second-hand books. It connects students and readers who want to sell their old books with those who need them, promoting reuse, reducing waste, and saving money. The platform integrates Django for robust web backend operations and incorporates a simple Machine Learning algorithm to optimize search and book recommendations.

---

## 📌 Features

- 🛍️ **Post and Purchase Books Online**
- 🔎 **Smart Book Search Engine** with ML-based relevance sorting
- 🗃️ **Category-wise Listings** (Academic, Fiction, Non-fiction, etc.)
- 💬 **Seller Contact and Book Details View**
- 📸 **Image Upload** using Pillow
- 🧠 **Personalized Suggestions** based on search behavior

---

## 🧱 Tech Stack
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="80"/>
  <img width="80" alt="icons8-django-120" src="https://github.com/user-attachments/assets/e2cab2a3-12a0-4020-a0bc-ee324266a3ae" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bootstrap/bootstrap-original-wordmark.svg" width="80"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg" width="80"/>
</p>

### Backend
- **Django** – Web framework for backend logic, user handling, and database operations.
- **MySQL** – Relational database for user and book data.
- **ML Algorithm** – Used to sort books based on keyword relevance and previous interactions.

### Frontend
- **Django Templates** (HTML/CSS)
- Basic **JavaScript** for interactivity

### Libraries & Tools
- **Pillow** – Image handling and book cover uploads
- **Pandas** – Data manipulation for sorting and analysis
- **mysqlclient** – MySQL-Python connector

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Install **Python 3.10.11** from the `dependency` folder
- Install the required Python modules using `pip`:

```bash
pip install django
pip install Pillow
pip install pandas
pip install mysqlclient
```

## 🛠️ Steps to Run
- Open the project folder in VS Code or your preferred IDE.
- Open a new terminal inside the project directory.
- Run the Django development server:

```bash
python manage.py runserver
```
- Copy the local server URL from the terminal (e.g., http://127.0.0.1:8000).
- Visit: http://127.0.0.1:8000/PageTurn to access the homepage.

Home page
![image](https://github.com/user-attachments/assets/11e1036f-5111-4516-818b-f39538147c34)
Search page
![image](https://github.com/user-attachments/assets/450b6067-0680-45f0-a083-e6e90f793085)
