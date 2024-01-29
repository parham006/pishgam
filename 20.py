header = input("enter your header text : ")
parageraf = input("enter your parageraf text : ")

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Testing HTML</title>
    <style>
        p {
          color: green;
          font-weight: bold;
        }

        h1 {
          color: red;
        }
    </style>
</head>
"""

html += f"""
<body>
<h1>{header}</h1>
<p>{parageraf}</p>
</body>
</html>"""

open("text.html", "w").write(html)
print("done")
