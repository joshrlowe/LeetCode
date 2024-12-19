def generate_readme(conn, readme="README.md"):
    try:
        # Connect to RDS PostgreSQL database
        print(f"Generating {readme}...")
        cur = conn.cursor()

        # Fetch distinct languages
        cur.execute("SELECT DISTINCT language FROM solutions")
        languages = [lang[0] for lang in cur.fetchall()]
        languages.remove("General") if "General" in languages else None

        # Fetch all problems
        cur.execute(
            """
            SELECT p.number, p.title, p.link, p.difficulty, s.language, s.solution_link
            FROM problems p
            LEFT JOIN solutions s ON p.id = s.problem_id
            """
        )
        results = cur.fetchall()

        # Organize data
        problems = {}
        for number, title, link, difficulty, language, solution_link in results:
            if number not in problems:
                problems[number] = {
                    "title": title,
                    "link": link,
                    "difficulty": difficulty,
                    "general_solution": None,
                    "language_solutions": {lang: "-" for lang in languages},
                }
            if language == "General":
                problems[number]["general_solution"] = solution_link
            elif language in languages:
                problems[number]["language_solutions"][language] = solution_link

        # Generate Markdown Table
        with open(readme, "w") as file:
            file.write("# LeetCode\n\n")
            file.write("## LeetCode Algorithms\n\n")
            file.write(
                'Note: "🔒" means you need to subscribe to LeetCode Premium to view the problem.\n\n'
            )

            # Write the table header
            file.write(
                "| Number | Problem Name | Difficulty | General Solution | "
                + " | ".join(languages)
                + " |\n"
            )
            file.write(
                "|:-------|:-------------|:-----------|:-----------------|:"
                + "--------|" * len(languages)
                + "\n"
            )

            # Write each problem row
            for number, data in sorted(problems.items()):
                general_solution = (
                    f"[Solution]({data['general_solution']})"
                    if data["general_solution"]
                    else "-"
                )
                language_solutions = " | ".join(
                    (
                        f"[Solution]({data['language_solutions'][lang]})"
                        if data["language_solutions"][lang] != "-"
                        else "-"
                    )
                    for lang in languages
                )
                file.write(
                    f"| {number} | [{data['title']}]({data['link']}) | {data['difficulty']} | {general_solution} | {language_solutions} |\n"
                )

        print(f"{readme} generated successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()
