class ElectronicDevice:
    def turn_on(self):
        print("Device is turned on")


class Phone(ElectronicDevice):
    def make_call(self):
        print("Making a call")


class SmartDevice(ElectronicDevice):
    def connect_wifi(self):
        print("Connecting to WiFi")


class SmartPhone(SmartDevice):
    def use_app(self):
        print("Using an app")


class Camera:
    def take_photo(self):
        print("Taking a photo")

class SmartCamera(SmartDevice, Camera):
    def record_video(self):
        print("Recording a video")


class Laptop(ElectronicDevice):
    def code(self):
        print("Coding on laptop")

class Tablet(ElectronicDevice):
    def draw(self):
        print("Drawing on tablet")


class WearableDevice:
    def track_steps(self):
        print("Tracking steps")

class SmartWatch(SmartDevice, WearableDevice):
    def show_time(self):
        print("Showing time")




phone = Phone()
phone.turn_on()     
phone.make_call()   


smartphone = SmartPhone()
smartphone.turn_on()     
smartphone.connect_wifi()
smartphone.use_app()     


smart_camera = SmartCamera()
smart_camera.turn_on()      
smart_camera.connect_wifi() 
smart_camera.take_photo()   
smart_camera.record_video() 


laptop = Laptop()
tablet = Tablet()
laptop.turn_on()   
laptop.code()      
tablet.turn_on()   
tablet.draw()      


smart_watch = SmartWatch()
smart_watch.turn_on()         
smart_watch.connect_wifi()    
smart_watch.track_steps()     
smart_watch.show_time()       
