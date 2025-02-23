# football-blog

## نصب
1. مخزن را کلون کنید:
    ```bash
    git clone https://github.com/AbolfazlMohammady/football-blog
    ```
2. به دایرکتوری پروژه بروید:
    ```bash
    cd football-blog
    ```
3. یک محیط مجازی ایجاد کنید:
    ```bash
    python -m venv venv
    ```
4. محیط مجازی را فعال کنید:
    - در ویندوز:
        ```bash
        venv\Scripts\activate
        ```
    - در macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. بسته‌های مورد نیاز را نصب کنید:
    ```bash
    pip install -r requirements.txt
    ```
6. مایگریشن‌ها را اعمال کنید:
    ```bash
    python manage.py migrate
    ```
7. یک سوپر یوزر ایجاد کنید:
    ```bash
    python manage.py createsuperuser
    ```
8. سرور توسعه را اجرا کنید:
    ```bash
    python manage.py runserver
    ```

## استفاده
- به وبسایت در `http://127.0.0.1:8000/` دسترسی پیدا کنید
- به پنل ادمین در `http://127.0.0.1:8000/admin/` دسترسی پیدا کنید

## مسیرهای پروژه (URLs)

| مسیر | توضیح | ویو مربوطه |
|-------|----------|--------------|
| `/blog/` | لیست بلاگ ها | `ProjectListView` |
| `/blog/<int:pk>/` | جزئیات بلاگ ها | `ProjectDetailView` |
| `/search/` | جستجوی بلاگ ها | `search` |
| `/bloge/chart/` | نمودار بلاگ ها بر اساس سال ساخت | `project_chart_view` |

## مشارکت
1. مخزن را فورک کنید
2. یک شاخه جدید ایجاد کنید (`git checkout -b feature-branch`)
3. تغییرات خود را کامیت کنید (`git commit -am 'Add new feature'`)
4. به شاخه خود پوش کنید (`git push origin feature-branch`)
5. یک پول ریکوئست جدید ایجاد کنید

## مجوز
این پروژه تحت مجوز MIT منتشر شده است.

## تماس
برای هرگونه پرسش، لطفاً با [09339796368] تماس بگیرید.

