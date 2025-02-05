import subprocess
import os

def run(cmd):
    """Run shell commands safely"""
    subprocess.run(cmd, shell=True, check=True)

def get_package_manager():
    """Detect OS type and set package manager"""
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            os_info = f.read().lower()
            if "ubuntu" in os_info or "debian" in os_info:
                return "apt"
            elif "centos" in os_info or "rhel" in os_info or "fedora" in os_info:
                return "yum" if "centos" in os_info else "dnf"
    return None

def setup_ansible():
    """Setup Ansible user with SSH access"""
    try:
        pkg_mgr = get_package_manager()
        if pkg_mgr is None:
            print("Unsupported OS detected. Exiting.")
            exit(1)

        # Ensure SSH is installed
        run(f"sudo {pkg_mgr} install -y openssh-server")

        # Update system
        run(f"sudo {pkg_mgr} update -y")

        # Take new username from user
        new_user = input("Enter the new username to be created in this machine: ")
        run(f"sudo useradd -m -s /bin/bash {new_user}")

        # Set password for the new user
        password = input(f"Enter new password for {new_user}: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            subprocess.run(f'echo "{new_user}:{password}" | sudo chpasswd', shell=True, check=True)
        else:
            print("Passwords do not match. Please run the script again.")
            exit(1)

        # Enable Password Authentication in SSH config
        ssh_config_path = "/etc/ssh/sshd_config" if os.path.exists("/etc/ssh/sshd_config") else "/etc/ssh/ssh_config"
        run(f"sudo sed -i 's/^#PasswordAuthentication no/PasswordAuthentication yes/' {ssh_config_path}")

        # Detect correct SSH service name
        ssh_service = "sshd" if os.path.exists("/etc/systemd/system/sshd.service") else "ssh"

        # Restart SSH service
        run(f"sudo systemctl restart {ssh_service}")

        # Grant sudo access without password
        run(f"echo '{new_user} ALL=(ALL) NOPASSWD: ALL' | sudo tee -a /etc/sudoers")

        # Create .ssh directory for the new user
        run(f"sudo mkdir -p /home/{new_user}/.ssh")
        run(f"sudo chmod 700 /home/{new_user}/.ssh")

        # Edit authorized_keys file
        ssh_key = input("Paste the id_ecdsa.pub key from Ansible Master user machine: ")
        with open(f"/home/{new_user}/.ssh/authorized_keys", "w") as f:
            f.write(ssh_key + "\n")

        # Set permissions
        run(f"sudo chmod 600 /home/{new_user}/.ssh/authorized_keys")

        # Set ownership of the .ssh folder and authorized_keys file
        run(f"sudo chown -R {new_user}:{new_user} /home/{new_user}/.ssh")

        print(f"User {new_user} created successfully with SSH access!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")
        exit(1)

if __name__ == "__main__":
    setup_ansible()
