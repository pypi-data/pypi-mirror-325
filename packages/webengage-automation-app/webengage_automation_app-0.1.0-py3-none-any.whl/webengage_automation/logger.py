import subprocess
import requests
import argparse

def send_log(log_message, endpoint_url):
    try:
        response = requests.post(endpoint_url, data=log_message.encode("utf-8"), headers={"Content-Type": "text/plain"})
        if response.status_code == 200:
            print("Log sent successfully.")
        else:
            print(f"Failed to send log. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending log: {e}")

def capture_logs(endpoint_url):
    subprocess.run(["adb", "logcat", "-c"])
    process = subprocess.Popen(
        ["adb", "logcat", "*:I", "*:D"],  # Capture only Info and Debug logs
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("Listening for Android logs...")

    while True:
        log_line = process.stdout.readline().strip()
        if log_line and "Processing event:" in log_line:
            send_log(log_line, endpoint_url)

def main():
    parser = argparse.ArgumentParser(description="Track webengage android logs automatically and send them to webengage endpoint.")
    parser.add_argument("--webengage-android", required=True, help="Provide your endpoint url to send webengage logs data.")
    args = parser.parse_args()

    capture_logs(args.webengage_android)

if __name__ == "__main__":
    main()
