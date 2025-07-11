import subprocess

try:
    # Try to run `npm --version` and capture output
    result = subprocess.run(
        ["npm", "--version"],
        capture_output=True,
        text=True,
        check=True
    )
    print("npm version found:", result.stdout.strip())
except FileNotFoundError:
    print("npm command not found.")
except subprocess.CalledProcessError as e:
    print("npm command found but failed:", e)
except Exception as e:
    print("Unexpected error:", e)
