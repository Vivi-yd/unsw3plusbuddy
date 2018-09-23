import json
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('getthedamndata', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

f1 = open('course-list.json','r')
course_details = f1.read()
parsed_json = json.loads(course_details)
course_names = []
term1 = []
term2 = []
term3 = []

for course in parsed_json:
    name = course["title"]
    if course["t1"] == "1":
        term1.append(course)
    if course["t2"] == "1":
        term2.append(course)
    if course["t3"] == "1":
        term3.append(course)
        
template = env.get_template('base.html')
f2 = open("unsw3plushelper/index.html", "w")
f2.write(template.render(courses=parsed_json))
f2.close()

f3 = open("unsw3plushelper/term1.html", "w")
f3.write(template.render(courses=term1))
f3.close()

f4 = open("unsw3plushelper/term2.html", "w")
f4.write(template.render(courses=term2))
f4.close()

f5 = open("unsw3plushelper/term3.html", "w")
f5.write(template.render(courses=term3))
f5.close()

f1.close()
