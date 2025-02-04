import pytest


def test_eval(workbench):
    expected = [
        dict(repetitions=2, level=60, fc=32e3/2),
        dict(repetitions=10, level=60, fc=32e3/10),
        dict(repetitions=15, level=60, fc=32e3/15),
        dict(repetitions=20, level=60, fc=32e3/20),
        dict(repetitions=20, level=60, fc=32e3/20),
        dict(repetitions=2, level=60, fc=32e3/2),
        dict(repetitions=10, level=60, fc=32e3/10),
    ]
    context = workbench.get_plugin('psi.context')

    # Ensure that we loop properly through the selector sequence
    context.apply_changes()
    for e in expected:
        context.next_setting('default')
        assert e == context.get_values()

    # Ensure that apply_changes restarts the selector sequence.
    context.apply_changes()
    for e in expected:
        context.next_setting('default')
        assert e == context.get_values()

    # Ensure that changes to expressions after apply_changes does not affect the
    # result.
    context.apply_changes()
    context.context_items['fc'].expression = '1e3'
    for e in expected:
        context.next_setting('default')
        assert e == context.get_values()

    # Now, the result should change.
    context.apply_changes()
    for e in expected:
        context.next_setting('default')
        e['fc'] = 1e3
        assert e == context.get_values()


def test_unique_values(workbench):
    context = workbench.get_plugin('psi.context')
    result = context.unique_values('repetitions')
    expected = {2, 10, 15, 20}
    assert result == expected


def test_multiple_unique_values(workbench):
    context = workbench.get_plugin('psi.context')
    result = context.unique_values(['repetitions', 'level'])
    expected = {(2, 60.0), (10, 60.0), (15, 60.0), (20, 60.0)}
    assert result == expected


def test_update(workbench):
    '''
    Tests whether the change detection algorithm works as intended.
    '''
    context = workbench.get_plugin('psi.context')
    context.apply_changes()

    assert context.changes_pending == False
    assert context.get_value('level') == 60

    context.next_setting('default')
    assert context.changes_pending == False
    assert context.get_value('level') == 60
    context.context_items['level'].expression = '32'
    assert context.changes_pending == True
    assert context.get_value('level') == 60

    context.next_setting('default')
    assert context.changes_pending == True
    assert context.get_value('level') == 60

    context.apply_changes()
    context.next_setting('default')
    assert context.changes_pending == False
    assert context.get_value('level') == 32

    context.context_items['level'].expression = '60'
    assert context.changes_pending == True
    context.revert_changes()
    assert context.changes_pending == False

    item = context.context_items['repetitions']
    context.selectors['default'].set_value(0, item, '5')
    assert context.changes_pending == True
    assert context.selectors['default'].get_value(0, item) == '5'


def test_duplicate_context_groups(workbench, helpers):
    error = 'ContextGroup with the same name has already been registered'
    with pytest.raises(ValueError, match=error):
        workbench.register(helpers.DuplicateContextGroupManifest())


def test_duplicate_context_items(workbench, helpers):
    error = 'Parameter with the same name has already been registered'
    with pytest.raises(ValueError, match=error):
        workbench.register(helpers.DuplicateContextItemManifest())


def test_register_unregister_context_items(workbench, helpers):
    plugin = workbench.get_plugin('psi.context')

    def _check_items(plugin, include, exclude):
        item_names = [i.name for i in plugin.context_groups['default'].items]
        for item in include:
            assert item in item_names
        for item in exclude:
            assert item not in item_names

    option1 = helpers.ContextItemOption1()
    option2 = helpers.ContextItemOption2()
    workbench.register(option1)
    _check_items(plugin, ['repetitions_1'], ['repetitions_2'])
    workbench.unregister(option1.id)
    _check_items(plugin, [], ['repetitions_1', 'repetitions_2'])
    workbench.register(option2)
    _check_items(plugin, ['repetitions_2'], ['repetitions_1'])
    workbench.unregister(option2.id)
    _check_items(plugin, [], ['repetitions_1', 'repetitions_2'])
