import subprocess

subprocess.check_call(["rm", "-rf", "build"])
subprocess.check_call(["rm", "-rf", "dist"])
subprocess.check_call(["rm", "-rf", "deloreanby.egg-info/"])
subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])
subprocess.check_call(["git", "commit", "-a"])
subprocess.check_call(["twine", "upload", "dist/*"])
