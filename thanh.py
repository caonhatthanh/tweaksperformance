import os
# Load ram.rop into memory
with open(os.path.join(os.path.dirname(__file__), 'ram.rop')) as f:
    ram_rop = f.read()
# Apply all settings in ram.rop to the system
def apply_settings():
    # Add code here to apply settings from ram.rop to the system
    pass
if option == 1:
    apply_settings()
