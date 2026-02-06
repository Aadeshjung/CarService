#!/usr/bin/env python
"""
CarService Deployment Helper for InfinityFree
Automates the deployment process
"""

import os
import sys
import subprocess
from pathlib import Path

class Deployer:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.app_root = self.project_root / 'CarService'
        
    def run_command(self, cmd, description):
        """Run a shell command and report status"""
        print(f"\n📦 {description}...")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {description} - Success!")
                return True
            else:
                print(f"❌ {description} - Failed!")
                print(f"Error: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def deploy(self):
        """Execute deployment steps"""
        print("\n" + "="*50)
        print("🚀 CarService Deployment to InfinityFree")
        print("="*50)
        
        os.chdir(self.app_root)
        
        steps = [
            ("pip install -r requirements.txt --user", "Installing dependencies"),
            ("python manage.py migrate", "Running migrations"),
            ("python manage.py collectstatic --noinput", "Collecting static files"),
            ("python manage.py check", "Running system checks"),
        ]
        
        failed = False
        for cmd, desc in steps:
            # Try with python3 if python fails
            if not self.run_command(cmd, desc):
                alt_cmd = cmd.replace("python", "python3", 1)
                if not self.run_command(alt_cmd, desc + " (with python3)"):
                    failed = True
        
        if not failed:
            print("\n" + "="*50)
            print("✅ Deployment Successful!")
            print("="*50)
            self.print_next_steps()
        else:
            print("\n" + "="*50)
            print("❌ Deployment had errors")
            print("="*50)
            sys.exit(1)
    
    def print_next_steps(self):
        """Print next steps for user"""
        print("""
📋 Next Steps:

1. **InfinityFree Control Panel Configuration:**
   - Go to: https://panel.infinityfree.net/
   - Navigate to: Python → Python for public_html
   - Set these values:
     
     Application root: /home/YOUR_USERNAME/public_html/CarService
     Startup file: passenger_wsgi.py
     Entry point: application
   
2. **Restart Application:**
   - Click "Restart Python"
   - Wait 1-2 minutes for the application to start

3. **Test Your Application:**
   - Visit: https://aadeshjungsingh.infinityfree.me
   - Admin panel: https://aadeshjungsingh.infinityfree.me/admin

4. **If you see errors:**
   - Check logs in InfinityFree Control Panel → Error Logs
   - Verify all files are uploaded
   - Ensure .env file exists with correct values
   - Check file permissions (755 for directories, 644 for files)

5. **Create Superuser (if needed):**
   - SSH into your account
   - Run: python manage.py createsuperuser
   - Follow the prompts

📚 For detailed help, see DEPLOYMENT.md
        """)

if __name__ == "__main__":
    deployer = Deployer()
    deployer.deploy()
