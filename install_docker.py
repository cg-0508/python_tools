import os

def exec_cmd(cmd):
    os.system(cmd + " > /dev/null")

def update_repo():
    exec_cmd("sudo apt-get update")

def install_dependency():
    exec_cmd("sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common")

def add_gpg_key():
    exec_cmd("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")

def install_tools():
    tools = ["curl"]
    for i in tools:
        exec_cmd("sudo apt-get install "+i)

def add_sources():
    str = """
    sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
    """
    exec_cmd(str)

def add_user_to_docker_group():
    exec_cmd("sudo groupadd docker")
    exec_cmd("sudo usermod -aG docker ${USER}")
    exec_cmd("sudo systemctl restart docker")

def install_docker():
    exec_cmd("sudo apt-get install -y docker-ce")
    print(exec_cmd("sudo docker -v"))


if __name__ == '__main__':

    print("Updating software source ...")
    update_repo()
    print("Updating software source ... done")

    print("Installing tools ...")
    install_tools()
    print("Installing tools ... done")

    print("Installing dependencies ...")

    install_dependency()
    print("Installing dependencies ... done")

    print("Add GPG key ...")
    add_gpg_key()
    print("Add GPG key ... done")

    print("Add docker source ...")
    add_sources()
    update_repo()
    print("Add docker source ... done")

    print("Installing docker-ce ...")
    install_docker()
    print("Installing docker-ce ... done")

    print("Setting ...")
    add_user_to_docker_group()
    print("Completed!")
    print("Please quit the current user and log back in.")
