import unittest
from unittest import TestCase
from unittest.mock import patch

from pygeai.core.base.models import Project
from pygeai.core.clients import Geai
from pygeai.organization.responses import AssistantListResponse, ProjectListResponse, ProjectDataResponse


class TestGeai(TestCase):
    """
    python -m unittest pygeai.tests.core.test_clients.TestGeai
    """

    @unittest.skip("Requires call to API")
    def test_get_assistant_list(self):
        client = Geai()
        result = client.get_assistant_list()

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, AssistantListResponse))

    @unittest.skip("Requires call to API")
    def test_get_project_list(self):
        client = Geai()
        result = client.get_project_list()

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, ProjectListResponse))

    @unittest.skip("Requires call to API")
    def test_get_project_data(self):
        client = Geai()
        result = client.get_project_data("2ca6883f-6778-40bb-bcc1-85451fb11107")

        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, ProjectDataResponse))

    @unittest.skip("Requires call to API")
    def test_create_project_simple(self):
        client = Geai()

        project = Project(
            project_name="Test project - SDK",
            project_email="alejandro.trinidad@globant.com",
            project_description="Test project to validate programmatic creation of project"
        )
        response = client.create_project(project)
        self.assertIsNotNone(response)
