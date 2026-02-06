#!/bin/bash

# CarService InfinityFree Deployment Script
# This script automates the deployment process to InfinityFree

set -e  # Exit on error

echo "=========================================="
echo "CarService Deployment to InfinityFree"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if already in the project directory
if [ ! -f "manage.py" ]; then
    echo -e "${RED}Error: manage.py not found. Please run this script from the CarService directory.${NC}"
    exit 1
fi

echo -e "${YELLOW}Step 1: Installing dependencies...${NC}"
pip install -r requirements.txt --user 2>/dev/null || pip3 install -r requirements.txt --user
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

echo -e "${YELLOW}Step 2: Running database migrations...${NC}"
python manage.py migrate 2>/dev/null || python3 manage.py migrate
echo -e "${GREEN}✓ Migrations completed${NC}"
echo ""

echo -e "${YELLOW}Step 3: Collecting static files...${NC}"
python manage.py collectstatic --noinput 2>/dev/null || python3 manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"
echo ""

echo -e "${YELLOW}Step 4: Running system checks...${NC}"
python manage.py check 2>/dev/null || python3 manage.py check
echo -e "${GREEN}✓ System checks passed${NC}"
echo ""

echo -e "${YELLOW}Step 5: Setting file permissions...${NC}"
chmod 755 . -R
chmod 644 db.sqlite3
chmod 755 staticfiles
echo -e "${GREEN}✓ Permissions set${NC}"
echo ""

echo -e "${GREEN}=========================================="
echo "Deployment Complete! ✓"
echo "==========================================${NC}"
echo ""
echo "Next steps:"
echo "1. Go to InfinityFree Control Panel"
echo "2. Navigate to Python Settings"
echo "3. Set Application root: /home/YOUR_USERNAME/public_html/CarService"
echo "4. Set Startup file: passenger_wsgi.py"
echo "5. Set Entry point: application"
echo ""
echo "Your application should be live at:"
echo "https://aadeshjungsingh.infinityfree.me"
echo ""
