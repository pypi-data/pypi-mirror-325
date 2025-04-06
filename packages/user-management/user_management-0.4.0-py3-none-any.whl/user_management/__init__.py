"""
User Management Package

A package for managing user-related operations using Firebase.
"""

from .firebase_client import FirebaseClient, FirebaseUser

__version__ = "0.4.0"

__all__ = ["FirebaseClient", "FirebaseUser"] 