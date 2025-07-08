# 🧪 Web Automation and Reporting CLI

This project is a complete browser automation and reporting system using **Python**, **Playwright**, and **CLI interfaces**. It is designed to:

- 🔍 Perform **single or batch search queries** using DuckDuckGo
- 🌐 Automate real-world **website interactions**:
  - ZIM’s Hebrew website ([zim.com/he](https://www.zim.com/he)) using full XPath selectors
  - ZIM Labs’ English site ([zimlabs.zim.com](https://zimlabs.zim.com)) using robust content-based logic
- 🧾 Generate beautiful, readable **HTML reports** logging all actions (successes and failures)
- 🛠️ Provide modular infrastructure that supports:
  - `Aluminum`-style page object modeling
  - `Browser-use` functional encapsulation and parameter-driven control
- 💡 Ideal for training, testing automation skills, and demonstrating end-to-end browser-based workflows

---

## 📁 Project Structure

Project/
│
├── core/ # Core automation logic
│ ├── runner.py # Entry point for searches
│ ├── batch.py # Batch query handler
│ ├── zim_interactions.py # Hebrew ZIM.com automation
│ ├── zimlabs_interactions.py # English ZIMLabs automation
│ └── zim_xpath_snippet.py # Utility for XPath-based scraping
│
├── interface/ # CLI commands
│ ├── cli.py
│ └── init.py
│
├── reports/ # HTML report generator
│ ├── generator.py
│ └── init.py
│
├── utils/ # Timestamp utility
│ └── time.py
│
├── data/ # Input & output
│ ├── keywords.txt # List of queries for batch mode
│ ├── output/ # Where reports are saved
│ └── output.csv # Placeholder (not used yet)
│
├── main.py # Entrypoint for CLI
├── requirements.txt # All dependencies
├── README.md # This file
└── usefulInfo.txt # Notes and experiments

---

## 🧠 Features

- 🔍 Single search automation (`--query`)
- 📂 Batch file support (`--file`)
- 🌐 Real website interaction with:
  - [https://www.zim.com/he](https://www.zim.com/he)
  - [https://zimlabs.zim.com](https://zimlabs.zim.com)
- 📜 HTML reports with:
  - Emoji-coded steps
  - Logs for each interaction
  - Fail-safe `finally` report generation
- 🌱 Written in pure Python with modular architecture

---

## ⚙️ Setup Instructions

1. **Create Virtual Environment**

python3 -m venv path/to/venv
source path/to/venv/bin/activate

python3 -m pip install -r requirements.txt
playwright install
deactivate

🚀 How to Use
▶️ Single Search
python3 main.py --query "OpenAI"

📄 Batch Mode
python3 main.py --file data/keywords.txt

🌐 Interact with ZIM Hebrew site
python3 core/zim_interactions.py

🌐 Interact with ZIM Labs (English)
python3 core/zimlabs_interactions.pypython3 core/zimlabs_interactions.py

📊 Reports
• All HTML reports are saved inside: data/output/
• Filenames include the query and timestamp
• Each report includes:
• A clean layout with title
• A list of all automation steps
• ✅ Success / ❌ Failure indicators
• Always generated even if a failure occurs (via finally)

💡 Tips
• Make sure your browser has network access.
• You can change the search engine or target sites easily via runner.py or cli.py.
• XPath selectors are used for all ZIM Hebrew site interactions.
• Reports open with:
open path/to/output/report.html

🧾 Author & License
Created by Shalev Lazarof
