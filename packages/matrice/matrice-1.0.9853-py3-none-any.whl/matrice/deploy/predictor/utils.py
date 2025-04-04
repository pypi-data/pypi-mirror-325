import logging
import subprocess

def pull_docker_image(docker_image):
    """Download the docker image"""
    try:
        check_docker()
        logging.info(f"Starting download of docker image: {docker_image}")
        docker_pull_process = subprocess.Popen(
            ["docker", "pull", docker_image],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        logging.info("Docker pull command initiated successfully")
        return docker_pull_process
    except Exception as e:
        logging.error(
            f"Docker image download failed with error: {str(e)}", exc_info=True
        )
        raise

def check_docker():
    """Check the Docker status on the system. Install if not present."""
    try:
        subprocess.run(["docker", "--version"], check=True)
        logging.info("Docker is already installed.")
    except subprocess.CalledProcessError:
        logging.info("Docker is not installed. Installing Docker...")
        uninstall_docker()
        install_docker()
        test_docker()

def test_docker():
    """Test if Docker is installed and running properly."""
    try:
        subprocess.run(["docker", "run", "hello-world"], check=True)
        logging.info("Docker is installed and running correctly.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Docker test: {e}")

def install_docker():
    """Install Docker on the system."""
    install_commands = [
        "apt-get update -y",
        "apt-get install ca-certificates curl -y",
        "install -m 0755 -d /etc/apt/keyrings",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
        "chmod a+r /etc/apt/keyrings/docker.asc",
        """echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null""",
        "apt-get update -y",
        "apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y"
    ]

    try:
        for command in install_commands:
            subprocess.run(command, shell=True, check=True)
        logging.info("Docker installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing Docker: {e}")

def uninstall_docker():
    """Uninstalls Docker from the system."""
    try:
        subprocess.run(
            ["apt-get", "remove", "docker.io", "docker-doc", "docker-compose", 
             "docker-compose-v2", "podman-docker", "containerd", "runc", "-y"],
            check=True
        )
        logging.info("Docker uninstalled successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error uninstalling Docker: {e}")
