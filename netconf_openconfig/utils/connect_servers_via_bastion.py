import time

from netconf_openconfig.utils.connect_bastion import connect_ssh_bastion


def connect_servers_ssh_via_bastion(host, login):
    client = connect_ssh_bastion('j.Crestel', 'wr5Qm2Y*-')
    print("Connection to", host)
    ssh_command = "ssh " + login + ":" + "password" + "@" + host
    _, stdout, _ = client.exec_command(ssh_command)

    time.sleep(5)
    resultat_out = ""
    for ligne in stdout:
        resultat_out += ligne
        print("Resultat out: ", resultat_out)

    return client


def disconnect_servers_ssh_via_bastion(client):
    client.exec_command('exit')
