# Simple Discord RPC

A modern, light, and easy-to-use **Discord Rich Presence** configurator built with **Python**, **CustomTkinter**, and **pypresence**. 

Customize your Discord activity status in real time with a clean Dark Mode GUI. Save your settings automatically, add images, track elapsed time, and include custom buttons linking to your projects or social profiles!

---

## Preview & Configuration Fields

| Setting | Description | Example |
| :--- | :--- | :--- |
| **Application ID** | Your Discord Developer Application Client ID | `140000000000000000` |
| **Details (Line 1)** | First line of your Rich Presence status | `Adding visual interface` |
| **State (Line 2)** | Second line of your Rich Presence status | `Release date : unknown` |
| **Large Image Key** | Asset key for the main image set in Developer Portal | `logo` |
| **Large Text** | Tooltip text on hovering the large image | `My Awesome Project` |
| **Small Image Key** | Asset key for the badge image | `python` |
| **Small Text** | Tooltip text on hovering the small image | `In Development` |
| **Buttons** | Custom labels and URL links (up to 2 buttons) | Label: `GitHub`, URL: `https://github.com` |

---

## Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.
- An active **Discord Desktop App** running on your computer.
- A **Discord Application Client ID** created on the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/Miaoumap24/Simple-Discord-RPC.git
   cd Simple-Discord-RPC
   ```

2. **Install Dependencies**:
   Install required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Execute the main script:
   ```bash
   python app.py
   ```

---

## How to Set Up Your Discord Application ID

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, enter a name, and create it.
3. Copy the **Application ID** found under the *General Information* tab and paste it into the app's **Application ID** field.
4. *(Optional)* To add images:
   - Go to **Rich Presence > Art Assets** in the Developer Portal.
   - Upload your images and give them keys (e.g., `logo`, `python`).
   - Enter those exact key names in the app's image key fields.

---

## Project Structure

```text
├── app.py              # Main Python script
├── config.json         # Configuration file
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
```

---

## Built With

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI library built on top of Tkinter.
- [pypresence](https://github.com/qwertyquerty/pypresence) - Discord RPC wrapper for Python.

---

## License

This project is open source and available under the [AGPL-3.0 License](LICENSE).
