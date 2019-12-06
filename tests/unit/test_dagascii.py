import mock
import os

from dvc import dagascii
from dvc.env import DVC_PAGER


def test_less_pager_returned_when_less_found():
    with mock.patch.object(os, "system") as m:
        m.return_value = 0
        pager = dagascii.find_pager()

    assert pager.cmd == dagascii.DEFAULT_PAGER_FORMATTED


def test_plainpager_returned_when_less_missing():
    with mock.patch.object(os, "system") as m:
        m.return_value = 1  # any non-zero value
        pager = dagascii.find_pager()

    assert pager.__name__ == "plainpager"


def test_tempfilepager_returned_when_var_defined():
    os.environ[DVC_PAGER] = dagascii.DEFAULT_PAGER
    pager = dagascii.find_pager()

    assert pager.cmd == dagascii.DEFAULT_PAGER
