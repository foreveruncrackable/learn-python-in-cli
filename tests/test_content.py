from pydays.curriculum import CURRICULUM, TOTAL_DAYS
from pydays.lessons import load_lesson, split_sections
from pydays.quizzes import QUIZZES


def test_thirty_days():
    assert TOTAL_DAYS == 30
    assert [d["day"] for d in CURRICULUM] == list(range(1, 31))


def test_lessons_exist_and_are_well_formed():
    for day in range(1, 31):
        text = load_lesson(day)
        assert text.startswith(f"# Day {day}"), day
        assert text.count("```") % 2 == 0, f"unbalanced code fence in day {day}"
        assert len(split_sections(text)) >= 2, day


def test_split_ignores_headings_inside_code_fences():
    md = "# T\n\n## A\n```\n## not a heading\n```\n\n## B\ntext"
    assert len(split_sections(md)) == 3


def test_quizzes_valid():
    assert sorted(QUIZZES) == list(range(1, 31))
    for day, questions in QUIZZES.items():
        assert len(questions) >= 2, day
        for question, options, answer, explanation in questions:
            assert 0 <= answer < len(options), (day, question)
            assert len(set(options)) == len(options), (day, question)
            assert explanation


def test_every_lesson_teaches_in_words_not_just_code():
    for day in range(1, 31):
        sections = split_sections(load_lesson(day))
        titles = [s.splitlines()[0] for s in sections]
        assert any(t.startswith("## Key terms") for t in titles), f"day {day}: no Key terms"
        assert any(t.startswith("## Watch out") for t in titles), f"day {day}: no Watch out"
        assert titles[-1].startswith("## Today's Task"), f"day {day}: task must be last"
        assert "Big idea" in load_lesson(day), f"day {day}: no big idea"
