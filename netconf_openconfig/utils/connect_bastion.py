import time

import paramiko


def connect_ssh_bastion(username, password):
    print("Connexion Bastion")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', port=17840, username="admin", password="admin")
    time.sleep(5)
    _, stdout, _ = client.exec_command('who')

    resultat_out = ""
    for ligne in stdout:
        resultat_out += ligne
        print("Resultat out: ", resultat_out)

    return client


def disconnect_ssh_bastion(client):
    client.close()
