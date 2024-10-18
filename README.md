# This is an automation of Telegram report submission.

This script automates the process of submitting reports to Telegram using proxies and randomized user data. It is designed to submit reports in bulk, making it efficient for users needing to report multiple issues at once. 

### Features
- Randomized user agents for each request.
- Valid phone numbers generated randomly.
- Random email generation.
- Multithreading support for concurrent submissions.
- Proxy support for enhanced anonymity.
- Logs errors for troubleshooting.

### Requirements
To run this script, you need:
- Python 3.x
- Necessary libraries installed:
  - `requests`
  - `bs4`
  - `phonenumbers`
  - `random_user_agent`
  - `emailtools`

### Step-by-Step Instructions

1. **Install Python and pip:**
   ```bash
   pkg install python
   pkg install python-pip
   ```

2. **Install Required Libraries:**
   Use pip to install the necessary libraries:
   ```bash
   pip install requests beautifulsoup4 phonenumbers random-user-agent emailtools
   ```

3. **Prepare Proxy Files:**
   Create text files for each proxy type (e.g., `http_proxies.txt`, `socks4_proxies.txt`, `socks5_proxies.txt`). Each file should contain a list of proxies, one per line.

4. **Create the Message File:**
   Create a `message.txt` file containing the message templates you want to use for reports. Use `{username}` as a placeholder for the username or link.

5. **Run the Script:**
   Start the script using Python:
   ```bash
   python your_script.py
   ```
   Replace `your_script.py` with the actual name of your Python file.

6. **Input Username or Link:**
   When prompted, enter the username or link of the person, channel, or group you wish to report.

7. **Monitor Progress:**
   The script will run continuously, submitting reports and printing the status of successes and failures in the terminal.

### Important Notes
- Be mindful of Telegram's policies regarding abuse and reporting. This script should be used responsibly.
- This tool is for educational purposes only! Any misuse of the tool is your own responsibility!
