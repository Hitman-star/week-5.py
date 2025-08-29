# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Call parent constructor
        self.os = os
        self.storage = storage
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.device_info()} is now ON ✅")
        else:
            print(f"{self.device_info()} is already ON")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.device_info()} is now OFF ❌")
        else:
            print(f"{self.device_info()} is already OFF")

    def install_app(self, app_name):
        if self.is_on:
            print(f"📲 Installing {app_name} on {self.device_info()}")
        else:
            print("⚠️ Please power on the phone first")


# Example usage
phone1 = Smartphone("Apple", "iPhone 14", "iOS", "128GB")
phone2 = Smartphone("Samsung", "Galaxy S23", "Android", "256GB")

phone1.power_on()
phone1.install_app("WhatsApp")
phone1.power_off()
