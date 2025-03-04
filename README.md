# Stardew Valley Host Swapper

A command-line tool to **swap the host player in a Stardew Valley multiplayer save file** with one of the farmhands.

## 📜 Features
- Swap the `<player>` and `<Farmer>` sections in the Stardew Valley save file.
- Specify which `<Farmer>` should be the new host. Useful for save files with more than two players.
- Maintains XML structure without modifying tag names.
- Outputs a modified save file, preserving the original.

## 🛠️ Installation

### 🔹 Option 1: Run with Python (Recommended)
Ensure you have **Python 3+** installed.

1. Clone this repository:
   ```sh
   git clone https://github.com/JRitmeester/Stardew-Coop-Host-Swapper.git
   cd Stardew-Coop-Host-Swapper
   ```

2. Run the script with Python:
   ```sh
   python swap.py <save_file_path> <current_host_name> <new_host_name>
   ```

   Example:
   ```sh
   python swap.py MySaveFile_123456789 Player1 Player2
   ```

### 🔹 Option 2: Use a Standalone Executable (No Python Required)
For **Windows**:
1. Download the latest `swap.exe` from [Releases](https://github.com/your-username/stardew-host-swapper/releases).
2. Open a terminal (`cmd.exe` or PowerShell) and navigate to the file location.
3. Run:
   ```sh
   swap.exe <save_file_path> <current_host_name> <new_host_name>
   ```

For **macOS**:
1. Download `swap` from [Releases](https://github.com/your-username/stardew-host-swapper/releases).
2. Open a terminal and navigate to the file location.
3. Run:
   ```sh
   chmod +x stardew-swap  # Give execute permissions (only needed once)
   ./swap <save_file_path> <current_host_name> <new_host_name>
   ```

---

## ⚠️ Notes & Limitations
- The **current host name** must match exactly (case-insensitive).
- The **new host must already be a farmhand** in the save file.
- A **new save file** (`*_modified.xml`) is created to prevent accidental loss. Rename the old save file by adding `.old` to it as a backup. Remove the `_modified.xml` suffix before use and place it next to the old save file.

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).

---

## 💡 Contributing
Have an idea or found a bug? Feel free to open an issue or submit a pull request!
