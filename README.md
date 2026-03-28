# 📝 TextUtils - Text Analysis Web App

TextUtils is a simple and powerful web application built using **Django** that allows users to perform various text transformations and analysis operations easily.

---

## 🚀 Features

* 🔠 Convert text to **UPPERCASE**
* 🔡 Convert text to **lowercase**
* 🔄 **Swap case** of characters
* 🏷️ Convert text to **Title Case**
* 📏 Calculate **Length of text**
* ⚡ Fast and easy-to-use interface

---

## 🖥️ Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Django (Python)
* **Server:** Django Development Server

---

## 📂 Project Structure

```
TextUtils/
│── templates/
│   └── index.html
│── views.py
│── urls.py
│── settings.py
│── manage.py
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/textutils.git
cd textutils
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run the server

```bash
python manage.py runserver
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

1. User enters text in the textarea
2. Selects required operations (uppercase, lowercase, etc.)
3. Clicks **Submit**
4. Django processes the request and returns the result

---

## 🔐 Security

* CSRF protection is enabled using:

```html
{% csrf_token %}
```

---

## 🎯 Future Improvements

* Add remove punctuation feature
* Add word/character count separately
* Improve UI/UX
* Add API support

---

## 🤝 Contributing

Feel free to fork this repo and improve it 🚀

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

**Your Name**
