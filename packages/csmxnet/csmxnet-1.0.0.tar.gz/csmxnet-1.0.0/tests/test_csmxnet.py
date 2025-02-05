def test_security_check(self):
    """Ensure security methods return valid output"""
    result = self.network.check_security()

    # ✅ Ensure the function does not return None
    self.assertIsNotNone(result)

    # ✅ Ensure expected keys exist
    self.assertIn("secure_directory", result)
    self.assertIn("fake_python_version", result)

    # ✅ Ensure directory listing is a list
    self.assertIsInstance(result["secure_directory"], list)

    # ✅ Ensure fake Python version is a string
    self.assertIsInstance(result["fake_python_version"], str)
