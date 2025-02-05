"""Unit tests for the `ldap_update_users` function."""

from unittest.mock import MagicMock, Mock, patch

from django.test import override_settings, TestCase

from apps.users.models import User
from apps.users.tasks import ldap_update_users


class UpdateUsers(TestCase):
    """Test the updating of user data."""

    @override_settings(AUTH_LDAP_SERVER_URI=None)
    def test_exit_silently_when_uri_is_none(self) -> None:
        """Test the function exits gracefully when no LDAP server URI is provided."""

        ldap_update_users()

    @override_settings(
        AUTH_LDAP_SERVER_URI='ldap://ds.example.com:389',
        AUTH_LDAP_USER_SEARCH=MagicMock(base_dn='dc=example,dc=com'),
        AUTH_LDAP_USER_ATTR_MAP={'username': 'uid'}
    )
    @patch('apps.users.tasks.get_ldap_connection')
    @patch('apps.users.tasks.LDAPBackend')
    def test_users_are_created(self, ldap_backend: Mock, mock_get_ldap_connection: Mock) -> None:
        """Test users are updated from LDAP data."""

        # Mock LDAP search results
        mock_conn = mock_get_ldap_connection.return_value
        mock_conn.search_s.return_value = [
            ('uid=user1,ou=users,dc=example,dc=com', {'uid': [b'user1']}),
            ('uid=user2,ou=users,dc=example,dc=com', {'uid': [b'user2']}),
        ]

        # Mock backend to return user objects
        mock_backend = ldap_backend.return_value
        mock_backend.populate_user.side_effect = lambda username: User(username=username)

        # Test users are created
        ldap_update_users(prune=False)
        user1 = User.objects.get(username='user1')
        user2 = User.objects.get(username='user2')

        # Verify that the users have the is_ldap_user flag set
        self.assertTrue(user1.is_ldap_user)
        self.assertTrue(user2.is_ldap_user)


class UserRemoval(TestCase):
    """Test the removal and/or deactivation of user accounts."""

    @override_settings(
        AUTH_LDAP_SERVER_URI='ldap://ds.example.com:389',
        AUTH_LDAP_USER_SEARCH=MagicMock(base_dn='dc=example,dc=com'),
        AUTH_LDAP_USER_ATTR_MAP={'username': 'uid'}
    )
    @patch('apps.users.tasks.get_ldap_connection')
    def test_users_are_pruned(self, mock_get_ldap_connection: Mock) -> None:
        """Test the deletion of missing user accounts."""

        # Mock an LDAP search result with no users
        mock_conn = MagicMock()
        mock_conn.search_s.return_value = []
        mock_get_ldap_connection.return_value = mock_conn

        # Create users
        User.objects.create(username='user_to_prune', is_ldap_user=True)
        User.objects.create(username='non_ldap_user', is_ldap_user=False)

        # Test missing LDAP users are deleted
        ldap_update_users(prune=True)
        self.assertFalse(User.objects.filter(username='user_to_prune').exists())
        self.assertTrue(User.objects.filter(username='non_ldap_user').exists())

    @override_settings(
        AUTH_LDAP_SERVER_URI='ldap://ds.example.com:389',
        AUTH_LDAP_USER_SEARCH=MagicMock(base_dn='dc=example,dc=com'),
        AUTH_LDAP_USER_ATTR_MAP={'username': 'uid'}
    )
    @patch('apps.users.tasks.get_ldap_connection')
    def test_users_are_deactivated(self, mock_get_ldap_connection: Mock) -> None:
        """Test the deactivation of missing LDAP users, ensuring non-LDAP users are not affected."""

        # Mock an LDAP search result with no users
        mock_conn = MagicMock()
        mock_conn.search_s.return_value = []
        mock_get_ldap_connection.return_value = mock_conn

        # Create users
        User.objects.create(username='user_to_deactivate', is_ldap_user=True, is_active=True)
        User.objects.create(username='non_ldap_user', is_ldap_user=False, is_active=True)

        # Test missing LDAP users are deactivated
        ldap_update_users()
        self.assertFalse(User.objects.get(username='user_to_deactivate').is_active)
        self.assertTrue(User.objects.get(username='non_ldap_user').is_active)
