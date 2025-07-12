class phone:
    def __init__(self):
        print("calling...")

class camera:
    def __init__(self):
        print("clicking photo...")

class smartdevice(phone, camera):
    def __init__(self):
        phone.__init__(self)
        camera.__init__(self)
        print("smartdevice ready")

# Object creation should be outside the class
device = smartdevice()
