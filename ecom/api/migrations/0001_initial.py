from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(name="nandini",
                          email="nandinichhajed08@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9876543210",
                          gender="Female")
        user.set_password("nandini")
        user.save()

# if it is dependent on some other model then we add dependencies
    dependencies = [

    ]
    
    operations = [
        migrations.RunPython(seed_data)
    ]