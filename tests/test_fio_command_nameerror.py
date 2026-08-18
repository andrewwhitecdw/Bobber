# SPDX-License-Identifier: MIT
"""Regression test for the FIO command NameError bug.

When a FIO log does not contain at least two ``/usr/bin/fio --rw...``
command lines, ``fio_command_details()`` must raise a clear ``ValueError``.
Before the fix, the error message referenced an undefined variable ``log``,
so callers instead got ``NameError: name 'log' is not defined``.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bobber.lib.analysis.common import fio_command_details  # noqa: E402


def test_missing_fio_commands_raises_valueerror_not_nameerror():
    with pytest.raises(ValueError, match='FIO command not found'):
        fio_command_details('no fio commands here', {}, {})


def test_valid_fio_log_still_parses():
    log_contents = (
        '/usr/bin/fio --rw=read --bs=1M --size=1G --name=read_test\n'
        'some output\n'
        '/usr/bin/fio --rw=write --bs=1M --size=1G --name=write_test\n'
    )
    reads, writes = fio_command_details(log_contents, {}, {})
    assert reads['rw'] == 'read'
    assert writes['rw'] == 'write'
