import os
import subprocess


def check_directory(problem_number, problem_name, language):
    directory = (
        f"./algorithms/{problem_number}. {problem_name}/{language}/"
        if language != "General"
        else f"./algorithms/{problem_number}. {problem_name}/"
    )
    if not os.path.exists(directory):
        print(
            f"Directory '{directory}' does not exist. Please create it and try again."
        )
        exit(1)
    return directory


def format_files(tool, directory, options=[]):
    print(f"Formatting files using {tool}...")
    subprocess.run([tool] + options + [directory])
    print("Files formatted successfully!")
