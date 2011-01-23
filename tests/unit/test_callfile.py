"""Unit tests for `pycall`."""

from unittest import TestCase

from nose.tools import eq_, raises

from pycall import CallFile


class TestCallFile(TestCase):
	"""Run tests on the `CallFile` class."""

	@raises(TypeError)
	def test_create_callfile(self):
		"""Ensure creating an empty `CallFile` object fails."""
		CallFile()

	def test_callfile_attrs(self):
		"""Ensure `CallFile` attributes stick."""
		c = CallFile(0, 1, 2, 3, 4, 5, 6, 7)
		eq_(c.call, 0)
		eq_(c.action, 1)
		eq_(c.set_var, 2)
		eq_(c.archive, 3)
		eq_(c.user, 4)
		eq_(c.tmpdir, 5)
		eq_(c.file_name, 6)
		eq_(c.spool_dir, 7)