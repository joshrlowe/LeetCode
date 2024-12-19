def problem_exists(conn, problem_number):
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM problems WHERE number = %s", (problem_number,))
    result = cur.fetchone()
    cur.close()
    return result


def insert_problem(conn, problem_number, problem_name, problem_link, difficulty):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO problems (number, title, link, difficulty)
        VALUES (%s, %s, %s, %s) RETURNING id
        """,
        (problem_number, problem_name, problem_link, difficulty),
    )
    problem_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return problem_id


def upsert_solution(conn, problem_id, language, solution_link):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO solutions (problem_id, language, solution_link)
        VALUES (%s, %s, %s)
        ON CONFLICT (problem_id, language)
        DO UPDATE SET solution_link = EXCLUDED.solution_link
    """,
        (problem_id, language, solution_link),
    )
    conn.commit()
    cur.close()
