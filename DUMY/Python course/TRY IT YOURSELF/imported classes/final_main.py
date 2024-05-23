# Multiple Modules 9-12

# final_main.py

from new_admin import Admin

# Create an instance of Admin
admin_user = Admin("John", "Doe", "john doe", "johndoe@example.com", "USA")

# Call the show_privileges method
admin_user.privileges.show_privileges()
