"""Unit tests for the `AllocationReviewViewSet` class."""

from django.test import RequestFactory, TestCase
from rest_framework import status

from apps.allocations.models import AllocationRequest, AllocationReview
from apps.allocations.views import AllocationReviewViewSet
from apps.users.models import Team, User


class GetQueryset(TestCase):
    """Test the filtering of database records based on user permissions."""

    fixtures = ['testing_common.yaml']

    def test_get_queryset_for_staff_user(self) -> None:
        """Test staff users can query all reviews."""

        request = RequestFactory()
        request.user = User.objects.get(username='staff_user')

        viewset = AllocationReviewViewSet()
        viewset.request = request

        expected_queryset = AllocationReview.objects.all()
        self.assertQuerySetEqual(expected_queryset, viewset.get_queryset(), ordered=False)

    def test_get_queryset_for_non_staff_user(self) -> None:
        """Test non-staff users can only query reviews for their own teams."""

        request = RequestFactory()
        request.user = User.objects.get(username='member_1')

        viewset = AllocationReviewViewSet()
        viewset.request = request

        team1 = Team.objects.get(name='Team 1')
        expected_queryset = AllocationReview.objects.filter(request__team__in=[team1.id])
        self.assertQuerySetEqual(expected_queryset, viewset.get_queryset(), ordered=False)


class Create(TestCase):
    """Test the creation of new records."""

    fixtures = ['testing_common.yaml']

    def setUp(self) -> None:
        """Load test data from fixtures."""

        self.staff_user = User.objects.get(username='staff_user')
        self.request = AllocationRequest.objects.get(pk=1)

    def test_create_with_automatic_reviewer(self) -> None:
        """Test the reviewer field is automatically set to the current user."""

        request = RequestFactory().post('/allocation-reviews/')
        request.user = self.staff_user
        request.data = {
            'request': self.request.id,
            'status': 'AP'
        }

        viewset = AllocationReviewViewSet()
        viewset.request = request
        viewset.format_kwarg = None

        # Test the returned response data
        response = viewset.create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['reviewer'], self.staff_user.id)

        # Test the created DB record
        review = AllocationReview.objects.get(pk=response.data['id'])
        self.assertEqual(review.reviewer, self.staff_user)
        self.assertEqual(review.request, self.request)
        self.assertEqual(review.status, 'AP')

    def test_create_with_provided_reviewer(self) -> None:
        """Test the reviewer field in the request data is respected if provided."""

        request = RequestFactory().post('/allocation-reviews/')
        request.user = self.staff_user
        request.data = {
            'request': self.request.id,
            'reviewer': self.staff_user.id,
            'status': 'AP'
        }

        viewset = AllocationReviewViewSet()
        viewset.request = request
        viewset.format_kwarg = None

        # Test the returned response data
        response = viewset.create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['reviewer'], self.staff_user.id)

        # Test the created DB record
        review = AllocationReview.objects.get(pk=response.data['id'])
        self.assertEqual(review.reviewer, self.staff_user)
        self.assertEqual(review.request, self.request)
        self.assertEqual(review.status, 'AP')
