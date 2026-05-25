# Reverse Engineering Course Download

## ✨ Description

`reverse_engineering_course_download` is a Python automation project for studying API communication, HLS video streaming, `.m3u8` playlists, and structured video downloading workflows.

It demonstrates how authorized course content can be detected, downloaded, merged, and organized locally for offline access.

> ⚠️ This project is for educational and authorized research use only. Do not use it to bypass platform restrictions, DRM, paid-content protection, or copyright rules.

---

## 🧪 Test Machine Setup

The project was tested in a controlled research environment using:

1. **Rooted Android Test Device**  
   Used to gain deeper visibility into Android app behavior during authorized analysis.

2. **LSPosed / Xposed Research Environment**  
   Used on the test device to observe app behavior and system-level restrictions in a lab setup.

3. **Burp Suite Reverse Proxy**  
   The Android device traffic was routed through a PC proxy to inspect authorized API requests and responses.

4. **API Endpoint Analysis**  
   Captured requests were studied to understand course folders, lecture lists, video quality options, and `.m3u8` playlist URLs.

5. **Python Automation Script**  
   A custom Python script calls the identified API workflow, selects 720p streams, downloads `.ts` video segments, merges them, and saves lectures in organized folders.

---

## 🚀 Features

- Auto-detects course folders and lectures
- Handles HLS `.m3u8` playlists
- Downloads 720p video streams when available
- Merges `.ts` segments into playable video files
- Organizes lectures into clean local folders
- Cleans invalid characters from file and folder names

---

## 🛠️ Installation

```bash
git clone https://github.com/gag3301v/reverse_engineering_course_download.git
cd reverse_engineering_course_download
pip install -r requirements.txt
```

FFmpeg is recommended for media processing:

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install ffmpeg
```

---

## 📦 Usage

```python
from download_ts import get_all_course, make_dir

course_id = "your_course_id_here"
output_dir = "downloaded_lectures"

make_dir(output_dir)
get_all_course(course_id)
```

Run:

```bash
python download_ts.py
```

---

## 🔧 Configuration

Do not hardcode private values such as access tokens, cookies, API keys, or session headers.

Use a `.env` file or environment variables:

```env
ACCESS_TOKEN=your_access_token_here
COURSE_ID=your_course_id_here
OUTPUT_DIR=downloaded_lectures
```

Add private files and downloads to `.gitignore`:

```gitignore
.env
__pycache__/
*.mp4
downloads/
downloaded_lectures/
```

---

## 📁 Project Structure

```text
reverse_engineering_course_download/
├── README.md
├── requirements.txt
├── download_ts.py
├── .env.example
└── .gitignore
```

---

## 📚 Learning Outcomes

This project demonstrates:

- Python automation
- API request handling
- JSON parsing
- HLS video streaming
- `.m3u8` playlist analysis
- File and folder management
- Authorized reverse engineering methodology

---

## 📄 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This project is created for educational and authorized research purposes only. The author is not responsible for misuse. Use it only for content you own, have permission to access, or are explicitly authorized to download.
