from io import BytesIO
from pdfdocument.document import PDFDocument
from datetime import date


# def table_test():
#     f = BytesIO()
#     pdf = PDFDocument(f)
#     pdf.init_report()
#     d = date.today().strftime("%d.%m.%Y")
#     pdf.style.heading2.textColor = "#FC6600"
#     pdf.style.bullet.bulletText = '□'
#     pdf.h1(f"Tasks Stand {d}")
#     pdf.spacer()
#     table = [["A", "B", "C"], ["1", "2", "3"], ["4", "5", "6"]]

#     pdf.table(table, 20)
#     pdf.generate()
#     return f.getvalue()


def start_timetracking(kb, id, uid):
    for subtask in kb.getAllSubtasks(task_id=id, user_id=uid):
        if subtask['title'] == "Zeit":
            print(kb.setSubtaskStartTime(
                subtask_id=subtask['id'], user_id=uid))


def stop_timetracking(kb, id, uid):
    for subtask in kb.getAllSubtasks(task_id=id,):
        if subtask['title'] == "Zeit":
            print(kb.setSubtaskEndTime(subtask_id=subtask['id'], user_id=uid))


def get_timetracking(kb, id, uid):
    for subtask in kb.get_all_subtasks(task_id=id):
        if subtask['title'] == "Zeit":
            print(kb.hasSubtaskTimer(subtask_id=subtask['id'], user_id=uid))


def tasks_report(kb):

    f = BytesIO()
    pdf = PDFDocument(f)
    pdf.init_report()
    d = date.today().strftime("%d.%m.%Y")
    pdf.style.heading2.textColor = "#FC6600"
    pdf.style.bullet.bulletText = '□'
    pdf.h1(f"Tasks Stand {d}")
    pdf.spacer()

    for project in kb.get_my_projects():
        print(project['name'])

        pdf.h2(project['name'])
        l = []
        for task in kb.get_all_tasks(project_id=project['id'], status_id=1):
            l.append(task['title']+" id: " + task['id'])
            print("  ", task['title'])

        pdf.ul(l)
    pdf.generate()
    return f.getvalue()


if __name__ == "__main__":
    import kanboard
    import time

    kb = kanboard.Client('http://localhost/jsonrpc.php', 'admin',
                         'e7c16f5e7565eaceaaadfb1ef55cfe8f15cbe9853966dfcf057d0ecc355a')

    # with open("tasks.pdf", "wb") as pdf:
    #     pdf.write(tasks_report(kb))

    user = kb.get_me()
    start_timetracking(kb, 21, user['id'])
    # time.sleep(90)
    stop_timetracking(kb, 21, user['id'])
