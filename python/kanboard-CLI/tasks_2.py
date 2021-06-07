import kanboard
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
styles = getSampleStyleSheet()


kb = kanboard.Client('http://localhost/jsonrpc.php', 'admin',
                     'e7c16f5e7565eaceaaadfb1ef55cfe8f15cbe9853966dfcf057d0ecc355a')

styleN = styles["Normal"]
styleL = styles['UnorderedList']

styleH = styles['Heading1']
story = []
# add some flowables


for project in kb.get_my_projects():
    print(project['name'])
    story.append(Paragraph(project['name'], styleH))
    text = []
    for task in kb.getAllTasks(project_id=project['id'], status_id=1):

        story.append(Paragraph(task['title'], styleL))
        print("  ", task['title'])


doc = SimpleDocTemplate('mydoc.pdf', pagesize=A4)
doc.build(story)
