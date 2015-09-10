"""
Use this module to contain static data. Static data is directly used by the
codebase and should never be changed without a commit, as opposed to data
stored in the database that can change at any moment and whose values are not
necessarily constant.

Note: DO NOT re-use enum values unless you know exactly what you are doing!
"""

import enum

# Enum for permissions available to users.
class Permissions(enum.IntEnum):
  # Site admins: always has access to everything
  ADMIN = 1
  # Add, edit, or delete user data
  USERS = 2
  # Run the room hassle
  HASSLE = 3
  # Manage mailing lists
  EMAIL = 4
