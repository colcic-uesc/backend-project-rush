from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewTests(APITestCase):
    def setUp(self):
        self.department1 = Department.objects.create(name="Department 1")
        self.department2 = Department.objects.create(name="Department 2")
        self.valid_payload = {"name": "New Department"}
        self.invalid_payload = {"name": ""}

    def test_get_departments(self):
        response = self.client.get(reverse("departments"))
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_department(self):
        response = self.client.post(
            reverse("departments"), data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 3)

    def test_create_invalid_department(self):
        response = self.client.post(
            reverse("departments"), data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DepartmentDetailViewTests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Department 1")
        self.valid_payload = {"name": "Updated Department"}
        self.invalid_payload = {"name": ""}

    def test_get_valid_single_department(self):
        response = self.client.get(
            reverse("department-detail", kwargs={"pk": self.department.pk})
        )
        department = Department.objects.get(pk=self.department.pk)
        serializer = DepartmentSerializer(department)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_department(self):
        response = self.client.get(reverse("department-detail",
                                           kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_department(self):
        response = self.client.put(
            reverse("department-detail", kwargs={"pk": self.department.pk}),
            data=self.valid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, "Updated Department")

    def test_invalid_update_department(self):
        response = self.client.put(
            reverse("department-detail", kwargs={"pk": self.department.pk}),
            data=self.invalid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_department(self):
        response = self.client.delete(
            reverse("department-detail", kwargs={"pk": self.department.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Department.objects.filter(pk=self.department.pk).exists()
        )

    def test_delete_invalid_department(self):
        response = self.client.delete(reverse("department-detail",
                                              kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
