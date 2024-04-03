

---

# Daily Email Report Automation

This Python script automates the process of sending daily email reports using Gmail. It sends an email with a predefined message to a specified recipient at a specified time every day.

## Prerequisites

Before running the script, ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using Git or download the ZIP file and extract it.

2. **Install Required Libraries**: Open your terminal or command prompt, navigate to the project directory, and run the following command to install the necessary libraries:

    ```bash
    pip install secure-smtplib schedule
    ```

## Usage

1. **Configure Email Settings**:
   - Open the `daily_email_report.py` file in a text editor.
   - Replace `"your_email@example.com"` with your Gmail address in the `sender_email` variable.
   - Replace `"your_password"` with your Gmail account password in the `password` variable.
   - Replace `"recipient@example.com"` with the recipient's email address in the `receiver_email` variable.

2. **Run the Script**:
   - Save the changes to `daily_email_report.py`.
   - Open your terminal or command prompt, navigate to the project directory, and run the following command:

    ```bash
    python3 daily_email_report.py
    ```

3. **Allow Less Secure Apps Access** (for Gmail):
   - If you're using a Gmail account, ensure that "Less Secure Apps" access is enabled. You can do this by going to your [Google Account settings](https://myaccount.google.com/security) and turning on "Allow less secure apps".

## Customization

- **Email Content**: Modify the `message` variable in the script to customize the content of the email report.
- **Schedule**: You can customize the schedule according to your requirements by modifying the `schedule.every().day.at("08:00").do(send_email)` line in the script. Change `"08:00"` to your desired time in the 24-hour format.

## Troubleshooting

If you encounter any issues while running the script, consider the following steps:
- Check your email address, password, and recipient's email address for correctness.
- Ensure that "Less Secure Apps" access is enabled for your Gmail account.
- Check for any error messages displayed in the terminal or command prompt.
- Make sure your network allows SMTP connections on port 587.
- Disable any firewall or antivirus software that may be blocking the SMTP connection.

## Support

If you need further assistance or have any questions, feel free to [open an issue](https://github.com/your-username/daily-email-report/issues) in this repository.

---

Feel free to replace placeholders like `your_email@example.com`, `your_password`, and `recipient@example.com` with your actual email addresses. This README.md provides step-by-step instructions and explanations in simple language to guide users through setting up and running the script.