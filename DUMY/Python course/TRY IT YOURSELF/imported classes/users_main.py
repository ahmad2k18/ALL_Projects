# Imported Admin 9-11
# users_main.py

from users import Admin

# Create an instance of Admin
admin_user = Admin("John", "Doe", "johndoe", "johndoe@example.com", "USA")

# Call the show_privileges method
admin_user.privileges.show_privileges()
