from django.test import TestCase
from .models import Certificate
import datetime

class CertificateModelTest(TestCase):
    def test_save_certificate_with_long_paths(self):
        # Create a certificate with simulated long path for fields
        cert = Certificate.objects.create(
            title="Career Essentials in GitHub Professional Certificate",
            organization="Github",
            issue_date=datetime.date.today(),
            credential_id="cccd74234d90312b60072bbd4fd6bce6fb3f25b72a83da209f7a45c5e6fc5e6d",
            verification_url="https://www.linkedin.com/learning/certificates/cccd74234d90312b60072bbd4fd6bce6fb3f25b72a83da209f7a45c5e6fc5e6d?trk=share_certificate",
            order=2
        )
        # Manually set long names
        cert.certificate_file.name = "certificates/pdf/CertificateOfCompletion_Career_Essentials_in_GitHub_Professional_Certificate_With_A_Very_Long_Name_To_Ensure_It_Exceeds_The_Previous_One_Hundred_Character_Limit_In_Length_Completely_Without_Any_Issues.pdf"
        cert.certificate_image.name = "certificates/CertificateOfCompletion_Career_Essentials_in_GitHub_Professional_Certificate_With_A_Very_Long_Name_To_Ensure_It_Exceeds_The_Previous_One_Hundred_Character_Limit_In_Length_Completely_Without_Any_Issues.png"
        cert.save()
        
        saved_cert = Certificate.objects.get(id=cert.id)
        self.assertTrue(len(saved_cert.certificate_file.name) > 150)
        self.assertTrue(len(saved_cert.certificate_image.name) > 150)
