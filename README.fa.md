# 🗳️ برنامه مدیریت نظرسنجی

یک **سیستم مدیریت نظرسنجی** در خط فرمان ساخته شده با **Python 3** و **PostgreSQL** که به کاربران اجازه می‌دهد نظرسنجی ایجاد کنند، گزینه‌ها اضافه کنند، رأی دهند، نتایج را مشاهده کنند و برنده تصادفی انتخاب کنند.  

---

## 📌 ویژگی‌ها
- ایجاد نظرسنجی جدید با چندین گزینه  
- مشاهده تمام نظرسنجی‌های فعال  
- رأی دادن به گزینه‌های نظرسنجی با نام کاربری دلخواه  
- مشاهده تعداد رأی‌ها با درصد سهم هر گزینه  
- مشاهده لاگ کامل رأی‌ها با زمان دقیق  
- انتخاب تصادفی یک برنده از رأی‌دهندگان یک گزینه  
- پشتیبانی از پایگاه داده PostgreSQL با Connection Pool  

---

## 🗂 ساختار پروژه

    ├── main.py # برنامه اصلی و منوی CLI
    ├── connection_pool.py # مدیریت Connection Pool برای PostgreSQL
    ├── database.py # کوئری‌ها و توابع کمکی پایگاه داده
    ├── models/
    │ ├── poll.py # کلاس Poll
    │ └── option.py # کلاس Option
    └── README.md # مستندات پروژه

---

## ▶️ پیش‌نیازها
- Python 3.8 یا بالاتر  
- اجرای PostgreSQL server  
- بسته‌های پایتون:
    ```bash
    pip install psycopg2-binary python-dotenv pytz

---

## فایل .env برای ذخیره اطلاعات اتصال به دیتابیس (اختیاری، در صورت عدم وجود برنامه از کاربر می‌پرسد):

    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=your_database
    DB_USER=your_username
    DB_PASSWORD=your_password

---

## 🏁 راه‌اندازی و اجرا

1. مطمئن شوید PostgreSQL در حال اجراست و دیتابیس ایجاد شده است:
    ```sql
   CREATE DATABASE poll_db;

2. اجرای برنامه:
    ```bash
   python main.py

3. از منو استفاده کنید تا نظرسنجی ایجاد کنید، رأی دهید، نتایج را مشاهده کنید و برنده تصادفی انتخاب کنید.

---

## 🧑‍💻 نمونه استفاده

    -- Menu --

    1) Create new poll
    2) List open polls
    3) Vote on a poll
    4) Show poll votes
    5) Select a random winner from a poll option
    6) Exit

    Enter your choice: 1
    Enter poll title: زبان برنامه‌نویسی مورد علاقه
    Enter poll owner: عرفان
    Enter new option text (or leave empty to stop adding options): Python
    Enter new option text (or leave empty to stop adding options): JavaScript
    Enter new option text (or leave empty to stop adding options): 

---