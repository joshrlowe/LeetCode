from db.utils import connect_db
from db.operations import problem_exists, insert_problem, upsert_solution
from file.utils import check_directory, format_files
from git.utils import commit as git_commit, push as git_push
from readme.readme_generator import generate_readme


def main():
    conn = connect_db()

    # Check if problem exists in the database
    problem_number = input("Enter Problem Number: ").strip()
    problem = problem_exists(conn, problem_number)

    if not problem:
        print("This is a new problem.")
        print("Please provide the following details:")
        problem_name = input("Problem Name: ").strip()
        problem_link = input("Problem URL: ").strip()
        difficulty = input("Problem Difficulty: ").strip()
        premium = input("Is this a LeetCode Premium problem? (Y/N): ").strip().lower()
        if premium == "y":
            problem_name = f"{problem_name} 🔒"
        problem_id = insert_problem(
            conn, problem_number, problem_name, problem_link, difficulty
        )
    else:
        problem_id = problem[0]
        problem_name = problem[1]
        print(f"Updating existing problem: {problem_name}")

    # Ask for solution language and check if proper directory exists
    language = input("Solution Language: ").strip()
    directory = check_directory(problem_number, problem_name, language)
    solution_link = directory.replace(" ", "%20")

    # Insert or update the solution
    upsert_solution(conn, problem_id, language, solution_link)
    print("Solution updated in the database.")

    # Generate README with new/updated solution
    generate_readme(conn)

    format_files("black", directory)

    # Commit and push changes
    commit_message = input("Enter commit message: ").strip()
    git_commit(directory, commit_message)
    git_push()

    conn.close()


if __name__ == "__main__":
    main()
