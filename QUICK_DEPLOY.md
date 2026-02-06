# 🚀 Quick Deployment Guide - InfinityFree

## Prerequisites
- InfinityFree Account with SSH access
- Your domain: `aadeshjungsingh.infinityfree.me`
- GitHub Repository: https://github.com/Aadeshjung/CarService

## Option 1: Using SSH (Recommended)

### 1. Connect to Your Server
```bash
ssh your_username@ssh.infinityfree.app
```

### 2. Navigate to Public Directory
```bash
cd ~/public_html
```

### 3. Clone Your Repository
```bash
git clone https://github.com/Aadeshjung/CarService.git
cd CarService
```

### 4. Run Deployment Script
```bash
bash deploy.sh
```

Or use Python deployment script:
```bash
python deploy.py
```

### 5. Configure in Control Panel
- Go to: https://panel.infinityfree.net/
- Select **Python** for your public_html
- **Application root:** `/home/YOUR_USERNAME/public_html/CarService`
- **Startup file:** `passenger_wsgi.py`
- **Entry point:** `application`
- Click **Save**

### 6. Restart Application
- Click **Restart Python** in the control panel
- Wait 1-2 minutes

### 7. Visit Your Site
https://aadeshjungsingh.infinityfree.me

---

## Option 2: Using FTP

### 1. Connect via FTP
- Host: `ftp.infinityfree.app`
- Port: 21
- Username: Your InfinityFree username
- Password: Your InfinityFree password

### 2. Upload Project Files
- Navigate to `/public_html`
- Upload all files from your CarService project

### 3. Create .env File
Create a file named `.env` in the CarService directory with:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=aadeshjungsingh.infinityfree.me
```

### 4. Follow Steps 5-7 from Option 1

---

## Manual Commands (if needed)

After uploading, run via SSH:

```bash
# Install dependencies
pip install -r requirements.txt --user

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Check for errors
python manage.py check
```

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| **502 Bad Gateway** | Check InfinityFree error logs; restart Python |
| **Module not found** | Run `pip install -r requirements.txt --user` |
| **Static files missing** | Run `python manage.py collectstatic --noinput` |
| **Database locked** | Check file permissions on db.sqlite3 |
| **Can't write to db** | SSH and run: `chmod 644 db.sqlite3` |

---

## File Structure After Deployment

```
/home/YOUR_USERNAME/public_html/
└── CarService/
    ├── passenger_wsgi.py        ← Entry point
    ├── .htaccess               ← URL routing
    ├── manage.py
    ├── requirements.txt
    ├── db.sqlite3
    ├── CarService/
    │   ├── settings.py
    │   └── wsgi.py
    ├── sales_rental/
    └── staticfiles/            ← Collected static files
```

---

## Useful Commands

```bash
# Create admin user
python manage.py createsuperuser

# Access admin panel
https://aadeshjungsingh.infinityfree.me/admin

# Check Django setup
python manage.py check

# View logs
tail -f ~/logs/passenger.log

# Update code from GitHub
git pull origin main

# Restart application (via control panel)
Click "Restart Python" in control panel
```

---

## After Deployment

1. ✅ Visit your site: https://aadeshjungsingh.infinityfree.me
2. ✅ Create a superuser for admin access
3. ✅ Test all features
4. ✅ Monitor error logs
5. ✅ Keep code updated with `git pull`

---

**Need help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
