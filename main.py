from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread, Clock
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
ScreenManager:
    MenuScreen:
    ConnectScreen:

<MenuScreen>:
    name: "menu"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "Welcome to VPN App"
            halign: "center"
            font_style: "H4"
        
        MDRaisedButton:
            text: "Start VPN"
            pos_hint: {"center_x": 0.5}
            on_press: app.switch_to_connect()

<ConnectScreen>:
    name: "connect"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDTextField:
            id: server_ip
            hint_text: "Server IP"
        
        MDTextField:
            id: port
            hint_text: "Port"
            input_filter: "int"
        
        MDTextField:
            id: username
            hint_text: "Username"
        
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
        
        MDRaisedButton:
            text: "Connect"
            pos_hint: {"center_x": 0.5}
            on_press: app.connect_vpn()

        MDRaisedButton:
            text: "Disconnect"
            pos_hint: {"center_x": 0.5}
            on_press: app.disconnect_vpn()

        MDLabel:
            id: status
            text: "Status: Disconnected"
            halign: "center"
            theme_text_color: "Hint"
'''

class MenuScreen(Screen):
    pass


class ConnectScreen(Screen):
    pass


class VPNApp(MDApp):
    def build(self):
        self.screen_manager = Builder.load_string(KV)
        return self.screen_manager

    def switch_to_connect(self):
        """Switch to the connect screen."""
        self.screen_manager.current = "connect"

    @mainthread
    def update_status(self, status, color="Primary"):
        """Update the status label."""
        status_label = self.screen_manager.get_screen("connect").ids.status
        status_label.text = f"Status: {status}"
        if color not in ["Primary", "Secondary", "Hint", "Error", "Custom", "ContrastParentBackground"]:
            color = "Primary"
        status_label.theme_text_color = color

    def connect_vpn(self):
        """Simulate VPN connection."""
        server_ip = self.screen_manager.get_screen("connect").ids.server_ip.text
        port = self.screen_manager.get_screen("connect").ids.port.text
        username = self.screen_manager.get_screen("connect").ids.username.text
        password = self.screen_manager.get_screen("connect").ids.password.text

        if not server_ip or not port or not username or not password:
            self.update_status("Please fill all fields", "Error")
            return

        self.update_status("Connecting...", "Hint")
        Clock.schedule_once(self.simulate_vpn_connection, 2)

    def disconnect_vpn(self):
        """Simulate VPN disconnection."""
        self.update_status("Disconnected", "Error")

    def simulate_vpn_connection(self, dt):
        """Simulate a successful VPN connection."""
        self.update_status("Connected", "Primary")


if __name__ == "__main__":
    VPNApp().run()
