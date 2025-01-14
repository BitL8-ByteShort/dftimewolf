#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the modules manager."""

from __future__ import unicode_literals

import unittest

from dftimewolf.lib import module
from dftimewolf.lib.modules import manager


class TestModule(module.BaseModule):  # pylint: disable=abstract-method
  """Test module."""


class ModulesManagerTest(unittest.TestCase):
  """Tests for the modules manager."""

  def testModuleRegistration(self):
    """Tests the RegisterModule and DeregisterModule functions."""
    # pylint: disable=protected-access
    number_of_module_classes = len(manager.ModulesManager._module_classes)

    manager.ModulesManager.RegisterModule(TestModule)
    self.assertEqual(
        len(manager.ModulesManager._module_classes),
        number_of_module_classes + 1)

    with self.assertRaises(KeyError):
      manager.ModulesManager.RegisterModule(TestModule)

    manager.ModulesManager.DeregisterModule(TestModule)
    self.assertEqual(
        len(manager.ModulesManager._module_classes), number_of_module_classes)

  # TODO: add tests for GetModuleByName

  def testRegisterModules(self):
    """Tests the RegisterModules function."""
    # pylint: disable=protected-access
    number_of_module_classes = len(manager.ModulesManager._module_classes)

    manager.ModulesManager.RegisterModules([TestModule])
    self.assertEqual(
        len(manager.ModulesManager._module_classes),
        number_of_module_classes + 1)

    manager.ModulesManager.DeregisterModule(TestModule)


if __name__ == '__main__':
  unittest.main()
