from django.test import SimpleTestCase
from django.urls import reverse

class MessPageTests(SimpleTestCase):

    def test_url_exist_at_correct_loction(self):
        response = self.client.get("/massagee/")
        self.assertEqual(response.status_code, 200)

    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('mess'))
        self.assertEqual(response.status_code, 200)

    
    def test_templat_name(self):
        response = self.client.get(reverse("mess"))
        self.assertTemplateUsed(response, 'home.html')

    def test_templat_content(self):
        response = self.client.get("/massagee/")
        self.assertContains(response, '<h1>wwww</h1>')