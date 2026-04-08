import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

def deploy():
    print("🛡️ Starting Secure Deployment Process...")

    # 1. Sync with GitHub (Triggers CodeQL & Checkov)
    print("\n--- Pushing to GitHub ---")
    run_command("git add .")
    run_command('git commit -m "Automated deployment: Site Update"')
    run_command("git push origin main")

    # 2. Deploy to Cloudflare Pages
    # Replace 'wonder-way-tours' with your actual project name in Cloudflare
    print("\n--- Deploying to Cloudflare Edge ---")
    run_command("wrangler pages deploy . --project-name=wonder-way-tours")

    print("\n✅ Deployment Complete! Website is live.")

if __name__ == "__main__":
    deploy()