Here’s a clean and professional `README.md` you can use for your project:

---

````markdown
# 📂 Download File Organizer

A lightweight Python script that automatically monitors your `Downloads` folder and organizes files into subfolders based on their file types (Documents, Images, Videos, Archives, Installers, Audio).

---

## 🚀 Features

- Real-time monitoring of the `Downloads` folder using `watchdog`
- Automatically moves files to categorized folders:
  - `Documents/`
  - `Images/`
  - `Videos/`
  - `Archives/`
  - `Installer/`
  - `Audio/`
- Skips temporary `.part` download files (e.g., from Chrome)

---

## 🛠 Requirements

- Python 3.6+
- Required Python packages:
  - `watchdog`

Install dependencies with:

```bash
pip install watchdog
````

---

## 🧠 How It Works

1. The script uses `watchdog` to listen for new files created in the `~/Downloads` folder.
2. When a file is detected (and not still downloading), it waits 2 seconds to ensure the file is fully written.
3. Based on its extension, the file is moved to a designated folder (created if it doesn't exist).

---

## 🗂 Folder Structure

Files are sorted into subfolders in your `Downloads` directory:

```
~/Downloads/
├── Documents/
├── Images/
├── Videos/
├── Archives/
├── Installer/
└── Audio/
```

---

## ▶️ How to Run

Run the script from terminal:

```bash
python file_organizer.py
```

Leave the terminal running — it will keep organizing files in the background until stopped (Ctrl+C).

---

## 🖥️ Optional: Run on System Startup (Windows)

If you'd like this script to run every time your PC starts:

1. Convert the script to `.exe` using `pyinstaller`
2. Add the `.exe` or a `.bat` file to the Windows Startup folder
3. Alternatively, use Task Scheduler for background execution

---

## 📦 Future Ideas

* Add GUI for enabling/disabling categories
* Log file support for moved files
* Custom rules or folder mappings

---

## 🧑‍💻 Author

**Jamie Na**

---

## 📄 License

This project is open source and free to use.

