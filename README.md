# 🇮🇷 Iranian SMS Bobber

## ⚠️ سلب مسئولیت (Disclaimer - FA)

این پروژه صرفاً برای اهداف **آموزشی** و **بررسی APIهای ارسال کد یک‌بارمصرف (OTP)** توسعه داده شده است. همچنین به منظور **شناخت آسیب‌پذیری‌هایی** طراحی شده که ممکن است باعث ارسال بیش از حد پیامک توسط سرویس‌دهنده‌ها شود.

**تحت هیچ شرایطی بنده هیچ‌گونه مسئولیتی در قبال خراب‌کاری، سوءاستفاده، یا هرگونه استفاده‌ی نادرست از این ابزار را نمی‌پذیرم.** استفاده از این ابزار بدون رضایت و مجوز فرد یا سیستم هدف، غیرقانونی و غیراخلاقی است و تمام عواقب آن بر عهده‌ی کاربر است.

---

## ⚠️ Disclaimer (EN)

This project is created **solely for educational purposes** and to analyze how **OTP APIs** from Iranian providers function. It also aims to identify **vulnerabilities** that might cause providers to send more messages than expected.

**Under no circumstances do I accept any responsibility for damage, abuse, or misuse of this tool.** Any unauthorized use of this tool against individuals or systems is strictly prohibited, illegal, and unethical. Users bear all consequences.

---

## 📌 معرفی (Introduction - FA)

ابزار `iranian-sms-bobber` یک اسکریپت پایتونی برای ارسال پیامک‌های انبوه (SMS Bombing) به شماره‌های ایرانی است. این ابزار با استفاده از APIهای عمومی سامانه‌های پیامکی ایرانی طراحی شده تا آسیب‌پذیری‌های موجود را نشان دهد.

---

## 📌 Introduction (EN)

`iranian-sms-bobber` is a Python-based tool designed to send mass SMS messages to Iranian phone numbers using public OTP APIs. Its primary purpose is to highlight potential vulnerabilities in SMS providers.

---

## 🧰 امکانات (Features - FA)

- پشتیبانی از چند سرویس پیامک OTP ایرانی  
- قابلیت تنظیم تعداد پیامک‌ها  
- رابط خط فرمان  
- معماری ماژولار

---

## 🧰 Features (EN)

- Supports multiple Iranian OTP gateways  
- Configurable SMS count  
- Simple command-line interface  
- Modular and extensible design

---

## 📦 نصب (Installation - FA)

### پیش‌نیازها:

- Python 3.6 یا بالاتر  
- pip

### مراحل نصب:

```bash
git clone https://github.com/Antinet-ir/iranian-sms-bobber.git
cd iranian-sms-bobber
pip install -r requirements.txt
```

---

## 📦 Installation (EN)

### Requirements:

- Python 3.6 or higher  
- pip

### Steps:

```bash
git clone https://github.com/Antinet-ir/iranian-sms-bobber.git
cd iranian-sms-bobber
pip install -r requirements.txt
```

---

## 🚀 استفاده (Usage - FA)

```bash
python sms_bobber.py --phone <شماره_موبایل> --count <تعداد_پیامک>
```

مثال:

```bash
python sms_bobber.py --phone +989123456789 --count 10
```

---

## 🚀 Usage (EN)

```bash
python sms_bobber.py --phone <phone_number> --count <number_of_messages>
```

Example:

```bash
python sms_bobber.py --phone +989123456789 --count 10
```

---

## 🔌 سرویس‌های پشتیبانی‌شده (Supported Services - FA)

- SMS.ir  
- Ghasedak.io  
- Kavenegar.com

🔑 برای استفاده، کلیدهای API را باید در فایل `config.py` وارد کنید:

```python
SMS_IR_API_KEY = 'your_sms_ir_api_key'
GHASEDAK_API_KEY = 'your_ghasedak_api_key'
KAVENEGAR_API_KEY = 'your_kavenegar_api_key'
```

---

## 🔌 Supported SMS Services (EN)

- SMS.ir  
- Ghasedak.io  
- Kavenegar.com

🔑 API keys must be placed in the `config.py` file:

```python
SMS_IR_API_KEY = 'your_sms_ir_api_key'
GHASEDAK_API_KEY = 'your_ghasedak_api_key'
KAVENEGAR_API_KEY = 'your_kavenegar_api_key'
```

---

## 🤝 مشارکت (Contributing - FA)

اگر باگی پیدا کردید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم که با Pull Request یا باز کردن Issue مشارکت کنید.

---

## 🤝 Contributing (EN)

Feel free to contribute by submitting pull requests or opening issues if you find bugs or have suggestions.

---

## 📄 لایسنس (License - FA)

این پروژه تحت لایسنس MIT منتشر شده است. برای اطلاعات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

---

## 📄 License (EN)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

اگه خواستی اینو به فایل `README.md` تبدیل کنم یا مستقیم برات آپلود کنم، کافیه بگی 👌
