# **CodeHammer: A Code Processing Toolkit**

## **Overview**
**CodeHammer** is a lightweight tool designed to **combine, analyze, and manage code files** efficiently. It helps developers extract and format relevant code snippets for **AI-assisted development, debugging, and modification**.

## **Features**
- **File and Directory Inspection**: Retrieve file contents, list directory structures, and analyze project organization.
- **Automated Code Processing**: Identify and manipulate specific code files based on extensions.
- **Code Modification**: Write and update files programmatically.
- **Cleanup and Maintenance**: Remove unnecessary files from results folders.
- **Seamless CLI Integration**: Designed to work with **command-line tools** for easy access.

---

## **Installation**
To install **CodeHammer**, run:
```bash
pip install codehammer
```

---

## **Available CLI Commands**
CodeHammer provides a command-line interface (CLI) to process and manage code files.

### 🔍 **1. tree**
> **Retrieve the structure of a directory**  
Returns a list of all files in a specified directory, excluding `.gitignore`-listed files.

#### **Usage**
```bash
code-hammer tree --folder src --base-dir .
```
#### **Example Output**
```
src/main.py
src/utils/helpers.py
src/config/settings.json
```

---

### 📄 **2. file**
> **Read the content of a specific file**  
Retrieves the contents of a file for analysis or processing.

#### **Usage**
```bash
code-hammer file --file src/main.py --base-dir .
```
#### **Example Output**
```python
def main():
    print("Hello, world!")
```

---

### 📂 **3. files**
> **List all files in a specific folder**  
Provides a JSON list of files within the specified folder.

#### **Usage**
```bash
code-hammer files --folder src --base-dir .
```
#### **Example Output**
```json
{
    "main.py": "def main():\n    print('Hello, world!')",
    "config.json": "{'debug': true, 'version': '1.0'}"
}
```

---

### 📁 **4. files_recursive**
> **Retrieve all files in a folder and its subdirectories**  
Useful for analyzing an entire project structure.

#### **Usage**
```bash
code-hammer files_recursive --folder src --base-dir .
```
#### **Example Output**
```json
{
    "src/main.py": "def main():\n    print('Hello, world!')",
    "src/utils/helpers.py": "def helper():\n    return 'Helper function'"
}
```

---

### 🔎 **5. find_files**
> **Find all files matching specific extensions in the base directory**  
Helpful for searching for specific types of files, such as Python scripts or Markdown documentation.

#### **Usage**
```bash
code-hammer combine --extensions py md --output-file output.txt --base-dir .
```
#### **Example Output**
```
Merged files: ['src/main.py', 'docs/readme.md']
```

---

### ✍️ **6. write**
> **Write or modify a file**  
Creates or modifies a file inside the `.result` folder.

#### **Usage**
```bash
code-hammer write --file output.txt --content "New content for the file" --base-dir .
```
#### **Example Output**
```
File written successfully: .result/output.txt
```

---

### 🧹 **7. clean_result**
> **Remove unnecessary files from the `.result` folder**  
Ensures that old files don’t clutter the workspace.

#### **Usage**
```bash
code-hammer clean_result --exclude-clean output.txt --base-dir .
```
#### **Example Output**
```
Cleaned .result folder. Removed files: ['output.txt']
```

---

### 🛠 **8. combine**
> **Merge multiple files into a single output file**  
Key feature for creating **context-rich** inputs for LLMs.

#### **Usage**
```bash
code-hammer combine --extensions py md --output-file combined.txt --base-dir .
```
#### **Example Output**
```
Merged files: ['src/main.py', 'docs/readme.md']
```

---

## **Using CodeHammer in Python**
CodeHammer provides a **Python API** for programmatic access.

### **Example Usage**
```python
from code_hammer.core.main import CodeHammer

# Initialize CodeHammer
hammer = CodeHammer(base_dir=".")

# Get directory structure
print(hammer.get_directory_tree("."))

# Read file content
print(hammer.get_file_content("src/main.py"))

# Combine Python files into a single output file
hammer.forge_prompt(["py"])
```

---

## **Conclusion**
**CodeHammer** is a simple yet powerful tool for **managing and processing code files**. It is designed to work efficiently with **LLM-powered assistants**, **automated code analyzers**, and **developer workflows**.

---
🚀 **Get started with CodeHammer today!** 🚀