from django.test import TestCase
from contact.models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name="علی",
            last_name="قاسمی",
            phone_number=9123456789,
            address="تهران، خیابان آزادی",
            number=123,
            email="ali@example.com"
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.first_name, "علی")
        self.assertEqual(self.contact.email, "ali@example.com")
        self.assertTrue(self.contact.created)

    def test_contact_str(self):
        self.assertEqual(str(self.contact), "علی قاسمی - ali@example.com")
