import kanboard

import tasks

kb = kanboard.Client('http://localhost/jsonrpc.php', 'admin',
                     'e7c16f5e7565eaceaaadfb1ef55cfe8f15cbe9853966dfcf057d0ecc355a')


if __name__ == "__main__":

    with open("tasks.pdf", "wb") as pdf:
        pdf.write(tasks.tasks_report(kb))
