# Social Media API  
**Project:** Building and Deploying a Django API  
**Repository:** `Alx_DjangoLearnLab`  
**Directory:** `social_media_api`  
**Phase:** Step 0 – Project Setup & User Authentication  

---

## 📘 Project Overview
This project is part of the **ALX Django LearnLab** curriculum.  
It focuses on developing a **Social Media REST API** using **Django** and **Django REST Framework (DRF)**.  

In this first phase, we establish the project foundation — setting up the Django environment, configuring the REST framework, and implementing a **robust user authentication system**.  
By the end of this phase, you’ll have working registration and login endpoints that return authentication tokens.

---

## 🎯 Objectives
- Set up a new Django project and app.  
- Configure Django REST Framework.  
- Implement a **custom user model** extending `AbstractUser`.  
- Create authentication endpoints for **user registration** and **login** using **Token Authentication**.

---

## ⚙️ Tech Stack
| Component | Technology |
|------------|-------------|
| Backend Framework | Django 5 + Django REST Framework |
| Authentication | Token Authentication (`rest_framework.authtoken`) |
| Database | SQLite 3 (default, for development) |
| Language | Python 3.10+ |
| Media Handling | Pillow |

---

## 🧩 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
---

### 2️⃣ Create Virtual Environment & Activate
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

