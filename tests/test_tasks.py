"""Every task must be solvable (reference solution passes) and not already
solved (starter code fails)."""

import pytest

from pydays.runner import check_task, missing_requirements
from pydays.tasks import TASKS

ALL = [(day, task) for day, tasks in sorted(TASKS.items()) for task in tasks]
IDS = [f"day{d:02d}-{t.id}" for d, t in ALL]


def test_every_day_has_a_task():
    assert sorted(TASKS) == list(range(1, 31))


def test_task_ids_unique_per_day():
    for day, tasks in TASKS.items():
        ids = [t.id for t in tasks]
        assert len(ids) == len(set(ids)), day


@pytest.mark.parametrize("day,task", ALL, ids=IDS)
def test_reference_solution_passes(day, task):
    if missing_requirements(task.requires):
        pytest.skip(f"needs {task.requires}")
    result = check_task(task, task.solution)
    detail = [(c.case.describe(), c.actual, c.error) for c in result.cases if not c.passed]
    assert result.passed, (result.syntax_error, result.missing_constructs, detail)


@pytest.mark.parametrize("day,task", ALL, ids=IDS)
def test_starter_does_not_already_pass(day, task):
    if missing_requirements(task.requires):
        pytest.skip(f"needs {task.requires}")
    assert not check_task(task, task.starter).passed
