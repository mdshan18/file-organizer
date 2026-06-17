📁 File Organizer Tool

**Automated File Management System Using Python & Linux**

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu%2FCentOS-green)](https://www.linux.com/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-orange)](https://git-scm.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📖 Overview

**File Organizer** is an **automated file management system** that demonstrates core **Linux system administration**, **Python automation scripting**, and **DevOps practices**.

This tool intelligently categorizes files by type and organizes them into structured folders automatically - reducing manual file management overhead and showcasing practical scripting expertise.

**Perfect for:**
- ✅ Learning Linux file system operations
- ✅ Python automation scripting
- ✅ DevOps automation practices
- ✅ Real-world problem solving

---

## 🎓 What You Learn

This project demonstrates:

| Concept | What You Learn |
|---------|---|
| **Linux File Systems** | File operations, permissions, directory management |
| **Python Scripting** | Automation scripts for system administration |
| **DevOps Automation** | Reducing manual effort through automation |
| **Git Workflow** | Version control best practices |
| **Problem Solving** | Breaking down problems into automation solutions |

---

## ⚙️ How It Works
User Provides Folder Path

↓

Script Scans All Files

↓

Identifies File Type (by extension)

↓

Creates Category Folders

(Images, Videos, Documents, etc.)

↓

Moves Files to Appropriate Folders

↓

Directory Organized! ✅

---

## ✨ Features

| Feature | Details |
|---------|---------|
| **Image Organization** | Auto-moves .jpg, .png, .gif to `Images/` folder |
| **Video Organization** | Auto-moves .mp4, .mkv, .avi to `Videos/` folder |
| **Document Organization** | Auto-moves .pdf, .docx, .txt to `Documents/` folder |
| **Audio Organization** | Auto-moves .mp3, .wav, .m4a to `Audio/` folder |
| **Cross-Platform** | Works on Linux, macOS, Windows |
| **Safe Operations** | Error handling for permission issues |

---

## 🛠️ Technologies Used
┌─────────────────────────┐

│    Technologies         │

├─────────────────────────┤

│ • Python 3.6+          │

│ • Linux (File System)  │

│ • Git (Version Control)│

│ • VS Code (Editor)     │

└─────────────────────────┘

---

## 📦 Project Structure
file-organizer/

│

├── organizer.py          # Main Python script

├── requirements.txt      # Python dependencies

├── .gitignore           # Git ignore file

├── README.md            # This file

└── LICENSE              # MIT License

### **File Descriptions:**

- **`organizer.py`** - Main script that performs file organization
- **`requirements.txt`** - Python dependencies (if any)
- **`.gitignore`** - Files to ignore in Git
- **`README.md`** - Project documentation

---

## 📋 Prerequisites

### **System Requirements:**

```bash
✓ Python 3.6 or higher
✓ Linux/macOS/Windows
✓ Terminal/Command Prompt access
✓ Read/Write permissions on target folder
```

### **Check Prerequisites:**

```bash
# Check Python version
python3 --version

# Should output: Python 3.x.x
# If not installed, install from: https://www.python.org
```

---

## 🚀 Installation & Usage

### **Step 1: Clone the Repository**

```bash
# Clone from GitHub
git clone https://github.com/mdshan18/file-organizer.git

# Navigate to project folder
cd file-organizer
```

### **Step 2: View the Script (Optional)**

```bash
# See what the script does before running
cat organizer.py

# Or open in your text editor
code organizer.py
```

### **Step 3: Run the Organizer**

```bash
# Execute the Python script
python3 organizer.py

# Script will prompt you for a folder path
```

### **Step 4: Provide Folder Path**

```bash
$ python3 organizer.py
Enter the folder path: /path/to/your/folder

# Example paths:
# On Linux/Mac: /home/user/Downloads
# On Windows:   C:\Users\YourName\Downloads
```

### **Step 5: Watch the Magic! ✨**

```bash
Scanning files in: /home/user/Downloads
Found 25 files

Organizing files:
✅ Moved photo1.jpg → Images/
✅ Moved movie.mp4 → Videos/
✅ Moved resume.pdf → Documents/
✅ Moved song.mp3 → Audio/
... (more files)

Success! 15 files organized in 2 seconds.
```

---

## 📊 Example Output

### **Before Running Script:**
Downloads/

├── photo1.jpg

├── photo2.png

├── movie.mp4

├── tutorial.mkv

├── resume.pdf

├── notes.docx

├── budget.xlsx

├── song.mp3

├── podcast.wav

└── image.gif

### **After Running Script:**
Downloads/

├── Images/

│   ├── photo1.jpg

│   ├── photo2.png

│   └── image.gif

├── Videos/

│   ├── movie.mp4

│   └── tutorial.mkv

├── Documents/

│   ├── resume.pdf

│   ├── notes.docx

│   └── budget.xlsx

├── Audio/

│   ├── song.mp3

│   └── podcast.wav

---

## 💻 Code Highlights

### **Main Logic:**

The script uses Python's **`os` module** for file operations:

```python
import os
import shutil

# File categories mapping
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a']
}

# How it works:
# 1. Get file extension
# 2. Match with category
# 3. Create category folder if not exists
# 4. Move file to that folder
```

---

## ⚠️ Troubleshooting

### **Issue 1: "Permission Denied" Error**

```bash
❌ Error: Permission denied: '/path/to/file'

✅ Solution 1: Run with sudo
sudo python3 organizer.py

✅ Solution 2: Change folder permissions
chmod 755 /path/to/folder
python3 organizer.py
```

### **Issue 2: "File Not Found" Error**

```bash
❌ Error: [Errno 2] No such file or directory

✅ Solution: Check if path is correct
# List available folders
ls ~

# Use correct path
python3 organizer.py
# Then enter: /home/yourusername/Downloads
```

### **Issue 3: Script Not Running**

```bash
❌ Error: python3: command not found

✅ Solution: Install Python
# On Ubuntu/Debian:
sudo apt-get install python3

# On macOS:
brew install python3

# Then verify:
python3 --version
```

### **Issue 4: Some Files Not Moving**

```bash
❌ Files left in original folder

✅ Possible Reasons:
- File extension not in categories list
- File permissions prevent moving
- File is open in another program

✅ Solution:
- Add new categories in script
- Check file permissions
- Close any open files
```

---

## 🔧 Customization

### **Add Custom Categories**

Edit `organizer.py` and modify the `file_categories` dictionary:

```python
# Add more file types
file_categories = {
    'Images': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv'],
    'Documents': ['.pdf', '.docx'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],  # NEW!
    'Code': ['.py', '.js', '.html'],      # NEW!
}
```

### **Exclude Specific Folders**

```python
# Don't organize files in these folders
exclude_folders = ['.git', '__pycache__', '.venv']
```

---

## 🌟 Key Learning Outcomes

After working with this project, you'll understand:

✅ **Linux File System Operations**
- Working with directories
- File permissions and ownership
- Path handling (absolute vs relative)

✅ **Python for Automation**
- File system manipulation (`os` module)
- File operations (`shutil` module)
- String manipulation for extensions

✅ **DevOps Thinking**
- Automation reduces manual effort
- Scripting for system administration
- Real-world problem solving

✅ **Version Control (Git)**
- Tracking code changes
- Collaboration on projects
- Best practices for commits

---

## 🚀 Future Enhancements

Ideas for improving this project:

- [ ] Add configuration file support (.env) for custom categories
- [ ] Implement logging to track file movements
- [ ] Add dry-run mode to preview changes before execution
- [ ] Support for nested folder organization
- [ ] GUI interface (using tkinter)
- [ ] Scheduling with cron jobs (Linux)
- [ ] Docker containerization
- [ ] Unit tests for file operations
- [ ] Undo functionality to restore files
- [ ] Multi-threading for faster processing
- [ ] Cloud integration (AWS S3, Google Drive)
- [ ] Web interface using Flask

---

## 📚 Resources for Learning

### **Python Documentation:**
- [Python Official Docs](https://docs.python.org/3/)
- [Python `os` Module](https://docs.python.org/3/library/os.html)
- [Python `shutil` Module](https://docs.python.org/3/library/shutil.html)

### **Linux Learning:**
- [Linux Command Line Basics](https://ubuntu.com/tutorials)
- [File Permissions Explained](https://www.linux.com/training-tutorials/)

### **Git Learning:**
- [Git Official Tutorial](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)

---

## 🤝 Contributing

Want to improve this project? Here's how:

### **Step 1: Fork the Repository**

```bash
# Visit: https://github.com/mdshan18/file-organizer
# Click "Fork" button in top right
```

### **Step 2: Clone Your Fork**

```bash
git clone https://github.com/YOUR-USERNAME/file-organizer.git
cd file-organizer
```

### **Step 3: Create Feature Branch**

```bash
git checkout -b feature/add-archives-support
```

### **Step 4: Make Changes**

```bash
# Edit organizer.py
# Add new features
# Test your changes
```

### **Step 5: Commit Changes**

```bash
git add .
git commit -m "feat: add archives file type support"
```

### **Step 6: Push to GitHub**

```bash
git push origin feature/add-archives-support
```

### **Step 7: Create Pull Request**
Visit your fork on GitHub and click "Create Pull Request"

---

## 📝 Commit Message Guidelines

Write clear, meaningful commit messages:

```bash
# Good commit messages:
git commit -m "feat: add archives category to file organizer"
git commit -m "fix: resolve permission denied error handling"
git commit -m "docs: update README with troubleshooting section"
git commit -m "refactor: improve file categorization logic"

# Bad commit messages:
git commit -m "update"
git commit -m "fixed"
git commit -m "changes"
git commit -m "wip"
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What MIT License means:**
- ✓ You can use this code freely
- ✓ You can modify and improve it
- ✓ You can distribute it
- ✓ You must include the original license

---

## 📞 Questions & Support

### **If You Have Issues:**

1. **Check Troubleshooting Section** - Most common issues are covered above
2. **Read the Code Comments** - Understanding helps solve problems
3. **Search GitHub Issues** - Someone may have faced the same problem
4. **Open a GitHub Issue** - Describe your problem clearly

### **Report a Bug:**

Go to: https://github.com/mdshan18/file-organizer/issues
Click "New Issue"
Describe:

What you did
What went wrong
Expected result
Your system info (OS, Python version)




---

## 🎯 DevOps Relevance

**How this project teaches DevOps principles:**
Manual File Organization (Old Way)

└─> Time consuming

└─> Prone to errors

└─> Not scalable

└─> Repetitive
Automated File Organization (DevOps Way)

└─> Fast and reliable

└─> Consistent results

└─> Scalable to any folder size

└─> Reusable code

**Key DevOps Concepts:**
- **Automation** - Reducing manual effort
- **Scripting** - Using code for system management
- **Problem Solving** - Creating practical solutions
- **Version Control** - Tracking and managing code
- **Best Practices** - Writing maintainable code

---

## 👤 Author & Contact

**MD Shan**
- **Role:** DevOps Developer (Learning)
- **Email:** mdshanjgp@gmail.com
- **GitHub:** [@mdshan18](https://github.com/mdshan18)
- **LinkedIn:** https://www.linkedin.com/in/md-shan-179113349?utm_source=share_via&utm_content=profile&utm_medium=member_android
- **Location:** Noida, Delhi NCR

---

## 🎓 Portfolio Value

This project demonstrates to recruiters:

✅ **Linux Fundamentals**
- File system knowledge
- Permissions and operations
- Command-line proficiency

✅ **Python Scripting**
- Practical automation skills
- Code organization
- Error handling

✅ **DevOps Mindset**
- Automation thinking
- Problem solving
- Real-world applications

✅ **Version Control**
- Git proficiency
- Professional workflow
- Collaboration skills

---

## ⭐ Project Quality Metrics

| Metric | Value |
|--------|-------|
| **Difficulty Level** | Beginner-Intermediate |
| **Learning Value** | ⭐⭐⭐⭐⭐ (5/5) |
| **Code Quality** | ⭐⭐⭐⭐ (4/5) |
| **Documentation** | ⭐⭐⭐⭐⭐ (5/5) |
| **Interview Value** | ⭐⭐⭐⭐ (4/5) |

---

## 🚀 Quick Start (TL;DR)

```bash
# Copy-paste these 4 commands:

git clone https://github.com/mdshan18/file-organizer.git
cd file-organizer
python3 organizer.py
# Enter your folder path when prompted!
```

---

## 📌 What's New

- **v1.0.0** (June 2026) - Initial Release
  - File organization by type
  - Multiple category support
  - Error handling
  - Cross-platform compatibility

---

**Made with ❤️ for Learning DevOps**

Last Updated: June 2026  
Status: ✅ Actively Maintained  
Version: 1.0.0
