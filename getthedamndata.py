import json
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('getthedamndata', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

with open('course-list.json', 'r') as course_list:
    course_details = course_list.read()
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

    with open("unsw3plushelper/index.html", "w") as index:
        index.write(template.render(courses=parsed_json))

    with open("unsw3plushelper/term1.html", "w") as term1f:
        term1f.write(template.render(courses=term1))

    with open("unsw3plushelper/term2.html", "w") as term2f:
        term2f.write(template.render(courses=term2))

    with open("unsw3plushelper/term3.html", "w") as term3f:
        term3f.write(template.render(courses=term3))

    template = env.get_template('interactive.html')
    with open("unsw3plushelper/interactive.html", "w") as interactive:
        interactive.write(template.render(courses=parsed_json))
