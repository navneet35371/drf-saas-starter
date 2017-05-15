from django.contrib.sites.models import Site
from django.db.utils import IntegrityError
from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError

from apps.tenants.models import Domain, Tenant
from apps.users.models import User


class SiteCreationTest(TestCase):
    """ Testing the Site creation 
    
    There is an error with Sites in the create_tenant Site.objects.create method, when using MIGRATION_MODULES

    django.db.utils.IntegrityError: duplicate key value violates unique constraint "django_site_pkey"
    DETAIL:  Key (id)=(1) already exists.

    Ticket is posted to Cookiecutter: https://github.com/pydanny/cookiecutter-django/issues/1163
    
    MIGRATION_MODULES = {
        'sites': 'apps.contrib.sites.migrations'
    }
    """

    def test_django_site_setup(self):

        Site.objects.create(name="foo", domain="foo.com")


class TenantDomainTests(TestCase):
    """ """

    def setUp(self):
        """ """

        self.tenant_domain = Tenant.objects.get_tenant_domain()
        self.site = Site.objects.create(name="a.example.com", domain="a.example.com")
        self.tenant = Tenant.objects.create(name="A", site=self.site)

    def test_create_tenant_without_site_should_fail(self):
        """ Every Tenant needs at site """

        with self.assertRaises(IntegrityError):
            Tenant.objects.create(name="B")

    def test_a_site_can_only_belong_to_one_tenant(self):
        """A site can only be set for one tenant """

        with self.assertRaises(IntegrityError):
            Tenant.objects.create(name="B", site=self.site)

    def test_domains(self):
        """Can the tenant set external domains?"""

        self.domain = Domain.objects.create(domain="a.com", tenant=self.tenant)

    def test_create_tenant_method(self):
        """Can the tenant set external domains?"""

        user = User.objects.create(email="newtenant@example.com", first_name="Taylor", last_name="Tenant")

        Tenant.objects.create_tenant(user, "B", "b")

    def test_create_tenant_with_already_existing_domain(self):
        """Can the tenant set external domains?"""

        user = User.objects.create(email="newtenant@example.com", first_name="Taylor", last_name="Tenant")

        with self.assertRaises(ValidationError):
            Tenant.objects.create_tenant(user, "A", "a")