import pytest


from psi.controller.experiment_action import ExperimentAction


@pytest.fixture
def simple_experiment_action():
    return ExperimentAction(event='experiment_end')


@pytest.fixture
def complex_experiment_action():
    return ExperimentAction(event='experiment_end and not task_active')


@pytest.fixture
def context():
    return {
        'experiment_end': True,
        'task_active': False,
    }


def test_evaluate_simple(simple_experiment_action, context):
    assert simple_experiment_action.match(context) == True


def test_evaluate_complex(complex_experiment_action, context):
    assert complex_experiment_action.match(context) == True


def test_evaluate(complex_experiment_action):
    context = {'experiment_end': False, 'task_active': False}
    result = complex_experiment_action.match(context)
    assert result == False

    context = {'experiment_end': True, 'task_active': True}
    result = complex_experiment_action.match(context)
    assert result == False

    context = {'experiment_end': False, 'task_active': True}
    result = complex_experiment_action.match(context)
    assert result == False
