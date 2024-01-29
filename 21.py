students = [
    {"name": "farbod", "job": "backend-dev", "code": "1101"},
    {"name": "parsa", "job": "front-dev", "code": "1102"},
    {"name": "amirali", "job": "database-admin", "code": "1103"},
    {"name": "amirali", "job": "project-manager", "code": "1104"},
    {"name": "shayan", "job": "software-analyst", "code": "1105"},
    {"name": "parham", "job": "full-stack", "code": "1106"},
]
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Testing HTML</title>
    <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
"""
html +="""<body>
    <div>
    <table>
       <tr>
            <th>Name</th>
            <th>Job</th>
            <th>Code</th>
        </tr>"""
for i in students:
    html += f"""
        <tr>
            <td>{i['name']}</td>
            <td>{i['job']}</td>
            <td>{i['code']}</td>
        </tr>       
    </div>
"""
html += """
    </table>
    </body>
    </html>
    """
open("tabel.html", "w").write(html)
print("done")
