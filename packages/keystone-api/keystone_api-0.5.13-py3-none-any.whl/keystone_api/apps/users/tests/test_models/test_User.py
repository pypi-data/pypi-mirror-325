"""Unit tests for the `User` class."""

from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.users.models import User


class UserModelRegistration(TestCase):
    """Test the registration of the model with the Django authentication system."""

    def test_registered_as_default_user_model(self) -> None:
        """Test the `User` class is returned by the built-in `get_user_model` method."""

        self.assertIs(User, get_user_model())


class UserModel(TestCase):

    def setUp(self) -> None:
        """Set up a test user instance."""
        
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.user = User(
            username=self.username,
            email=self.email,
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_creation(self) -> None:
        """Test a `User` instance can be created successfully."""
        
        self.user.save()
        self.assertIsNotNone(self.user.pk)
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)

    def test_profile_image_generation(self) -> None:
        """Test a profile image is generated if one does not exist."""
        
        self.assertFalse(self.user.profile_image)
        self.user.save()  # Saving the user should trigger image generation

        self.assertTrue(self.user.profile_image)
        self.assertTrue(self.user.profile_image.name.endswith('.png'))

    def test_default_image_grid_size(self) -> None:
        """Test the generated default image grid size."""
        
        self.user.save()
        image = self.user._generate_default_image(grid_size=(6, 6), square_size=40)
        self.assertEqual(image.size, (240, 240))  # 6 * 40, 6 * 40

    def test_randomness_of_image_generation(self) -> None:
        """Test different users generate different images."""
        
        user1 = User(username='user1')
        user2 = User(username='user2')

        user1.save()
        user2.save()

        self.assertNotEqual(user1.profile_image.read(), user2.profile_image.read())

    def test_save_with_existing_image(self) -> None:
        """Test saving a user when an image already exists."""
        
        self.user.save()
        original_image = self.user.profile_image

        self.user.save()
        self.assertEqual(self.user.profile_image.name, original_image.name)
