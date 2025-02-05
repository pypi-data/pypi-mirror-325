"""Unit tests for the `AllocationViewSet` class."""

from django.test import RequestFactory, TestCase

from apps.allocations.models import Allocation
from apps.allocations.views import AllocationViewSet
from apps.users.models import Team, User


class GetQueryset(TestCase):
    """Test the filtering of database records based on user permissions."""

    fixtures = ['testing_common.yaml']

    def test_get_queryset_for_staff_user(self) -> None:
        """Test staff users can query all reviews."""

        request = RequestFactory()
        request.user = User.objects.get(username='staff_user')

        viewset = AllocationViewSet()
        viewset.request = request

        expected_queryset = Allocation.objects.all()
        self.assertQuerySetEqual(expected_queryset, viewset.get_queryset(), ordered=False)

    def test_get_queryset_for_non_staff_user(self) -> None:
        """Test non-staff users can only query allocations for their own teams."""

        user = User.objects.get(username='member_1')
        team = Team.objects.get(name='Team 1')

        request = RequestFactory()
        request.user = user

        viewset = AllocationViewSet()
        viewset.request = request

        expected_queryset = Allocation.objects.filter(request__team__in=[team.id])
        self.assertQuerySetEqual(expected_queryset, viewset.get_queryset(), ordered=False)
