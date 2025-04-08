# 📚 Reverse Engineering Course Download

## ✨ Description

(reverse_engineering_course_download) is a Python program designed to download video lectures from the ClassPlus platform. This tool simplifies the process of accessing educational content offline, making it accessible for students and learners on-the-go.

## 🚀 Features

- **Auto-Detect Content:** Automatically fetches all course content, including folders and lectures.
- **High-Quality Downloads:** Downloads videos in 1280x720 resolution to ensure the best quality.
- **Progressive Downloading:** Handles large files efficiently with a user-friendly progress bar.
- **Local Storage:** Organizes downloaded content into structured directories for easy access.

## 🛠️ Installation

To get started, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/gag3301v/reverse_engineering_course_download.git
   cd reverse_engineering_course_download
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## 📦 Usage

Here’s how you can use the script to download video lectures:

```python
from download_ts import get_all_course, make_dir, clean_path

# Set up directory and course ID
course_id = "your_course_id_here"
output_dir = "downloaded_lectures"

make_dir(output_dir)

# Start downloading all course content
get_all_course(course_id)
```

## 🔧 Configuration (if applicable)

No additional configuration is required. The script will automatically handle the necessary settings to download videos.

## 🧪 Tests

To ensure everything works as expected, you can run the following command:

```sh
pytest
```

## 📁 Project Structure

```
reverse_engineering_course_download/
├── README.md
├── requirements.txt
└── download_ts.py
```

- `README.md`: This file.
- `requirements.txt`: Lists all dependencies.
- `download_ts.py`: The main script for downloading videos.

## 👩‍💻 Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you’d like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance! 😊