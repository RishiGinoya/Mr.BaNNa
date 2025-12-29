#  BaNNa - TradingView Indicators Platform

A professional Django-based web platform for selling TradingView indicators.

##  Quick Start

1. Activate virtual environment: .\bannaenv\Scripts\Activate.ps1
2. Install dependencies: cd BaNNa; pip install -r requirements.txt
3. Setup database: python manage.py migrate
4. Create admin: python manage.py createsuperuser
5. Add indicators: python manage.py create_dummy_indicators
6. Run server: python manage.py runserver

Visit: http://127.0.0.1:8000/

##  Features

- Modern responsive UI with Tailwind CSS
- User authentication
- Dynamic indicator marketplace
- Stripe payment processing
- Telegram channel promotion
- Privacy policy page
- User dashboard with statistics

##  Structure

BaNNa/ - Main Django project
 banna_platform/ - Configuration
 main/ - App logic
 static/ - CSS, JS, images
 templates/ - HTML files

 2025 BaNNa Platform
