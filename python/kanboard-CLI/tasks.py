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


def tasks(kb):

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
        for task in kb.getAllTasks(project_id=project['id'], status_id=1):
            l.append(task['title'])
            print("  ", task['title'])

        pdf.ul(l)
    pdf.generate()
    return f.getvalue()


if __name__ == "__main__":
    import kanboard

    kb = kanboard.Client('http://localhost/jsonrpc.php', 'admin',
                         'e7c16f5e7565eaceaaadfb1ef55cfe8f15cbe9853966dfcf057d0ecc355a')

    with open("tasks.pdf", "wb") as pdf:
        pdf.write(tasks(kb))
