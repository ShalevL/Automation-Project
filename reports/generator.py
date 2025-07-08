import os

def generate_report(html_content: str, output_path: str):
    # Ensure parent folders exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Automation Report</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            margin: 40px;
            background: #f5f7fa;
            color: #333;
        }
        h1 {
            border-bottom: 2px solid #444;
            padding-bottom: 0.3em;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 12px 0;
            padding: 10px;
            background: white;
            border-radius: 6px;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
        }
        li:hover {
            background: #e9f5ff;
        }
        a {
            color: #0066cc;
            font-size: 1.1em;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Automation Report</h1>
    <div>
""")
        f.write(html_content)
        f.write("""
    </div>
</body>
</html>""")