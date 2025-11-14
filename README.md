```markdown
# Mes Final Project Camera 🎥

A Python + OpenCV project for capturing photos from a webcam.  
Each session automatically creates a new folder organized by **date** and **start time (hour, minute, second)**. Photos are saved sequentially (`_00.jpg`, `_01.jpg`, …) inside that folder.

---

## 📂 Project Structure

```
Mes_Final_Project/
├── camera.py          # Camera capture script
├── main.py            # Optional entry point
├── pyproject.toml     # Project dependencies (managed by uv)
├── uv.lock            # Lockfile for reproducibility
├── photos/            # Captured photos organized by date/time
│   └── 2025-11-14/
│       └── 15h18m42s/
│           ├── _00.jpg
│           ├── _01.jpg
│           └── ...
└── README.md          # Project documentation
```

---

## 🚀 Features

- Live webcam preview using **OpenCV**.
- **Space bar** → capture and save a photo (`_00.jpg`, `_01.jpg`, …).
- **ESC** → exit the program.
- Photos stored in:
  ```
  photos/YYYY-MM-DD/HHhMMmSSs/
  ```
  Example: `photos/2025-11-14/15h18m42s/_00.jpg`
- Overlay text shows:
  - Current session folder
  - Next photo filename

---

## 🛠 Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Initialize the project (already done):
   ```bash
   uv init
   ```

2. Install dependencies:
   ```bash
   uv add opencv-python
   ```

3. Run the script:
   ```bash
   uv run python camera.py
   ```

---

## 🎮 Usage

- Start the program:
  ```bash
  uv run python camera.py
  ```
- A preview window opens.
- Press **Space bar** to capture and save a photo.
- Press **ESC** to quit the session.

---

## 📌 Notes

- All photos are stored under the `photos/` directory.
- Each run creates a unique folder based on the exact start time (down to seconds).
- `.gitignore` excludes `photos/` and `.venv/` so they don’t clutter the repository.