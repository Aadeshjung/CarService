# CarService - InfinityFree Deployment Guide

## Step-by-Step Deployment Instructions

### Prerequisites
- InfinityFree Account (free tier)
- GitHub Repository (already set up: https://github.com/Aadeshjung/CarService)
- SSH/FTP access to InfinityFree

### Step 1: Connect to InfinityFree

#### Via SSH (Recommended):
```bash
ssh your_username@ssh.infinityfree.app
```

#### Via FTP:
Use FileZilla or any FTP client with:
- Host: `ftp.infinityfree.app`
- Port: 21
- Username: Your InfinityFree username
- Password: Your InfinityFree password

### Step 2: Clone Your Repository

Once connected, navigate to your public_html directory and clone the repository:

```bash
cd ~/public_html
git clone https://github.com/Aadeshjung/CarService.git
cd CarService
```

### Step 3: Set Up Environment Variables

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
nano .env
```

Update with your values:
- `SECRET_KEY` - Generate a new one: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- `EMAIL_HOST_PASSWORD` - Your Gmail app-specific password
- `KHALTI_SECRET_KEY` - Your Khalti payment gateway key

### Step 4: Install Python Packages

```bash
pip install -r requirements.txt --user
```

Or if that doesn't work:

```bash
pip3 install -r requirements.txt --user
```

### Step 5: Database Migration

```bash
python manage.py migrate
```

### Step 6: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 7: Configure InfinityFree

1. Go to InfinityFree Control Panel
2. Navigate to **Settings** > **Python**
3. Set Application root to: `/home/YOUR_USERNAME/public_html/CarService`
4. Set Application startup file: `passenger_wsgi.py`
5. Set Application entry point: `application`

### Step 8: Update DNS (if using custom domain)

In your InfinityFree control panel:
1. Go to **Domain Management**
2. Point your domain `aadeshjungsingh.infinityfree.me` to InfinityFree nameservers

### Step 9: Test the Deployment

Visit: https://aadeshjungsingh.infinityfree.me

### Troubleshooting

**502 Bad Gateway Error:**
- Check error logs in InfinityFree control panel
- Ensure `passenger_wsgi.py` is in the correct location
- Verify all dependencies are installed

**Static files not loading:**
- Run `python manage.py collectstatic --noinput` again
- Check file permissions

**Database errors:**
- Ensure `db.sqlite3` has write permissions
- Run migrations: `python manage.py migrate`

**Module not found errors:**
- Install missing packages: `pip install -r requirements.txt --user`

### Important Security Notes

1. **Never commit `.env` file** - It's in `.gitignore`
2. **Change SECRET_KEY** - Generate a new secure key for production
3. **Use environment variables** - All sensitive data should be in `.env`
4. **Keep dependencies updated** - Periodically update packages

### Monitoring & Maintenance

- Check error logs regularly in InfinityFree control panel
- Monitor database file size
- Keep Django and packages updated
- Regularly backup your database

### Useful Commands

```bash
# Check Python version
python --version

# Test Django settings
python manage.py check

# Create superuser
python manage.py createsuperuser

# Access admin panel
https://aadeshjungsingh.infinityfree.me/admin

# View logs
tail -f ~/logs/passenger.log
```

### Support

- InfinityFree Docs: https://docs.infinityfree.net/
- Django Docs: https://docs.djangoproject.com/
- For issues, check the GitHub repository: https://github.com/Aadeshjung/CarService

---

**Deployment Date:** February 6, 2026
**Domain:** aadeshjungsingh.infinityfree.me
**Framework:** Django 5.0.7
**Python:** 3.13
