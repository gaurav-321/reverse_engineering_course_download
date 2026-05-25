# Mobile API Traffic Analysis Lab

## ✨ Description

`mobile_api_traffic_analysis_lab` is a Python-based learning project focused on studying authenticated mobile-app API communication, request/response structures, HLS streaming concepts, `.m3u8` playlist behavior, and automation-based data organization.

The project was created in a controlled personal research environment using content accessed through my own paid and authenticated account. The goal was to understand how a mobile client communicates with backend APIs and how structured media metadata can be processed for learning, documentation, and security research.

> ⚠️ This project is for educational, personal, and authorized research use only. It must not be used to bypass platform restrictions, DRM, paid-content protection, copyright rules, or terms of service. Do not use this project on systems, accounts, or content you do not own or have explicit permission to analyze.

---

## 🎯 Purpose

This project demonstrates practical learning in:

- Mobile API traffic analysis
- Authenticated request flow understanding
- HLS and `.m3u8` streaming concepts
- Python automation
- JSON parsing and data structuring
- Secure handling of tokens, cookies, and session data
- Responsible reverse engineering methodology

The project is intended as a learning exercise in API analysis and automation, not as a tool for redistributing, bypassing, or extracting protected content.

---

## 🧪 Research Environment

The project was tested in a controlled personal research environment using:

1. **Rooted Android Test Device**  
   Used to gain deeper visibility into Android app behavior during authorized analysis and to observe how the app communicates with backend services.

2. **LSPosed / Xposed Research Environment**  
   Used on the test device as part of a mobile security research setup to study app behavior, runtime conditions, and client-side request flows in a controlled lab environment.

3. **Burp Suite Reverse Proxy**  
   The Android device traffic was routed through a local PC proxy to inspect authorized API requests and responses generated from my own authenticated account.

4. **Authenticated Paid Account**  
   Testing was performed only with content that I had legitimate access to through my own paid account.

5. **API Flow Documentation**  
   Captured requests were analyzed to understand how the app retrieves folders, lecture metadata, quality options, and HLS playlist references.

6. **Python-Based Automation and Data Organization**  
   Python scripts were used to study the authorized API workflow, structure response data, organize metadata, and understand HLS media workflow behavior in a controlled environment.
---

## 🚀 Features

- Studies authenticated mobile API request flows
- Parses structured JSON responses
- Documents folder and lecture metadata behavior
- Handles HLS `.m3u8` playlist analysis for learning purposes
- Organizes accessible metadata into clean local folders
- Cleans invalid characters from generated file and folder names
- Demonstrates safe handling of environment variables and private credentials

---

## 🔐 Security and Privacy Notes

This repository should not contain:

- Access tokens
- Cookies
- API keys
- Session headers
- Private endpoints
- Course provider URLs
- Downloaded media files
- Paid or copyrighted content

Use a `.env` file or environment variables for private values during local testing.

Example:

```env
ACCESS_TOKEN=your_access_token_here
COURSE_ID=your_course_id_here
OUTPUT_DIR=research_output
```

Add private files and generated outputs to `.gitignore`:

```gitignore
.env
__pycache__/
*.mp4
*.ts
downloads/
research_output/
downloaded_lectures/
```

---

## 🛠️ Installation

```bash
git clone https://github.com/gag3301v/mobile_api_traffic_analysis_lab.git
cd mobile_api_traffic_analysis_lab
pip install -r requirements.txt
```

FFmpeg may be useful for studying media-processing workflows:

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install ffmpeg
```

---

## 📦 Usage

This project is designed for authorized research environments only.

Before running any script, make sure:

- You are using your own account.
- You have permission to analyze the traffic.
- You are not bypassing DRM, access controls, or platform restrictions.
- You are not redistributing copyrighted content.
- You have removed all private tokens, cookies, and provider-specific URLs from the code.

Example structure for local testing:

```python
from download_ts import get_all_course, make_dir

course_id = "authorized_course_id_here"
output_dir = "research_output"

make_dir(output_dir)
get_all_course(course_id)
```

Run locally:

```bash
python download_ts.py
```

---

## 📁 Project Structure

```text
mobile_api_traffic_analysis_lab/
├── README.md
├── requirements.txt
├── download_ts.py
├── .env.example
└── .gitignore
```

---

## 📚 Learning Outcomes

This project helped me understand:

- How mobile applications communicate with backend APIs
- How authenticated API requests are structured
- How HLS streaming and `.m3u8` playlists work
- How to parse and organize API response data using Python
- How to manage sensitive values securely
- How to approach reverse engineering responsibly and ethically

---

## ✅ Responsible Use

This project should only be used for:

- Personal learning
- Authorized testing
- API behavior documentation
- Security research in a controlled environment
- Content and systems you own or have permission to analyze

Do not use this project to:

- Circumvent DRM
- Bypass paid-content restrictions
- Share or redistribute copyrighted content
- Access another user's account or data
- Violate a platform's terms of service

---

## 📄 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This project is created for educational and authorized research purposes only. The author is not responsible for misuse. Use it only in environments where you have permission to analyze the application, traffic, and content. Do not use it to bypass platform restrictions, DRM, copyright protections, or access controls.
