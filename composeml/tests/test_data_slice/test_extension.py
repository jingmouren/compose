from pytest import fixture

from composeml import LabelMaker


@fixture
def data_slice(transactions):
    lm = LabelMaker(target_entity='customer_id', time_index='time', window_size='1h')
    ds = next(lm.slice(transactions, num_examples_per_instance=1))
    return ds


def test_context(data_slice, capsys):
    print(data_slice.context)
    out = capsys.readouterr().out
    actual = out.splitlines()

    expected = [
        'customer_id                       0',
        'slice_number                      1',
        'slice_start     2019-01-01 08:00:00',
        'slice_stop      2019-01-01 09:00:00',
        'next_start      2019-01-01 09:00:00',
    ]

    assert actual == expected


def test_context_aliases(data_slice):
    assert data_slice.context == data_slice.ctx
    assert data_slice.context.slice_number == data_slice.ctx.count
    assert data_slice.context.slice_start == data_slice.ctx.start
    assert data_slice.context.slice_stop == data_slice.ctx.stop
