import subprocess
import os

def run(cmd):
    """Execute shell command safely."""
    subprocess.run(cmd, shell=True, check=True)

def detect_os():
    """Detect Linux distribution and return package manager."""
    try:
        with open("/etc/os-release") as f:
            os_info = f.read()
        
        if "Ubuntu" in os_info or "Debian" in os_info:
            return "apt"
        elif "CentOS" in os_info or "Rocky" in os_info or "RHEL" in os_info:
            return "yum"
        elif "Amazon Linux" in os_info:
            return "dnf"
        else:
            print("Unsupported Linux distribution.")
            exit(1)
    except FileNotFoundError:
        print("Unable to detect OS version. Exiting.")
        exit(1)

def setup_ansible():
    """Main function to install and configure Ansible."""
    pkg_manager = detect_os()
    
    # Get new username
    new_user = input("Enter the new username to be created: ")

    # Install Ansible
    if pkg_manager == "apt":
        run("sudo apt update -y && sudo apt install -y software-properties-common")
        run("sudo add-apt-repository --yes --update ppa:ansible/ansible")
        run("sudo apt update -y && sudo apt install -y ansible")
    elif pkg_manager == "yum":
        run("sudo yum install -y epel-release")
        run("sudo yum install -y ansible")
    elif pkg_manager == "dnf":
        run("sudo dnf install -y ansible")

    # Verify installation
    run("ansible --version")

    # Create user and set permissions
    run(f"sudo useradd -m -s /bin/bash {new_user}")
    run(f"sudo mkdir -p /home/{new_user}/.ssh")
    run(f"sudo chown -R {new_user}:{new_user} /home/{new_user}/.ssh")
    run(f"sudo chmod 700 /home/{new_user}/.ssh")

    # Generate SSH key
    ssh_key_path = f"/home/{new_user}/.ssh/id_ecdsa"
    run(f"sudo -u {new_user} ssh-keygen -t ecdsa -b 521 -N '' -f {ssh_key_path}")

    with open(f"{ssh_key_path}.pub") as f:
        print(f"This is your public key:\n{f.read()}")

    input("Press Enter to continue...")

    # Get user inputs for dynamic inventory
    inventory_group = input("Enter inventory group name: ")
    node_name = input("Enter node name: ")
    host_ip = input("Enter target node private IP address: ")
    ssh_user = input("Enter target machine SSH username: ")

    # Create inventory file entry
    inventory_entry = f"[{inventory_group}]\n{node_name} ansible_ssh_host={host_ip} ansible_ssh_user={ssh_user}\n"
    run("sudo chmod 666 /etc/ansible/hosts")
    with open("/etc/ansible/hosts", "w") as f:
        f.write(inventory_entry)
    run("sudo chmod 644 /etc/ansible/hosts")

    print("Inventory file '/etc/ansible/hosts' updated.")

if __name__ == "__main__":
    setup_ansible()
