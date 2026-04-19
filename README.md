# CLI Keyword Monitor

CLI Keyword Monitor is a Python-based command-line tool that searches and tracks specific keywords online. Useful for monitoring industry trends, product mentions, or even brand names.

## Features
- Specify keywords to track.
- Fetch results from websites, blogs, and forums.
- Export logs and detailed reports in JSON/CSV.
- Customizable frequency to run the tool.
- Lightweight and easy to configure.

## Installation
1. Clone this repository:
   ```plaintext
   git clone https://github.com/saibot07/cli-keyword-monitor.git
   ```
2. Navigate to the repository:
   ```plaintext
   cd cli-keyword-monitor
   ```
3. Install dependencies:
   ```plaintext
   pip install -r requirements.txt
   ```

## Usage
Run the main script with your desired keywords:
```plaintext
python main.py --keywords "AI,Python,Data Science" --frequency 60
```

Options:
- `--keywords`: Comma-separated keywords to monitor.
- `--frequency`: Monitoring frequency in seconds (default: 60).

## Example
```plaintext
python main.py --keywords "AI,Machine Learning" --frequency 30
```

## Contributing
Feel free to fork this repository, report issues, or submit pull requests!

## License
This project is open-source under the MIT License.