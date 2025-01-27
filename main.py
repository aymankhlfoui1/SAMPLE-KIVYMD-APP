from kivymd.app import MDApp
from kivy.lang import Builder
from jnius import autoclass, cast
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# استيراد الفئات الضرورية من pyjnius
PythonActivity = autoclass('org.kivy.android.PythonActivity')
VpnService = autoclass('android.net.VpnService')
Intent = autoclass('android.content.Intent')

class VPNApp(App):
    def build(self):
        self.server_address = TextInput(hint_text="Enter Server Address", multiline=False)
        self.port = TextInput(hint_text="Enter Port", multiline=False)
        self.username = TextInput(hint_text="Enter Username", multiline=False)
        self.password = TextInput(hint_text="Enter Password", multiline=False, password=True)

        connect_button = Button(text="Connect")
        connect_button.bind(on_press=self.start_vpn)

        self.log_label = Label(text="Logs will appear here...", size_hint_y=None, height=100)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.server_address)
        layout.add_widget(self.port)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(connect_button)
        layout.add_widget(self.log_label)

        return layout

    def start_vpn(self, instance):
        server = self.server_address.text
        port = self.port.text
        username = self.username.text
        password = self.password.text

        if not server or not port or not username or not password:
            self.log_label.text = "All fields are required!"
            return

        try:
            activity = PythonActivity.mActivity
            intent = Intent(activity, VpnService)
            activity.startActivity(intent)
            self.log_label.text = "VPN started successfully!"
        except Exception as e:
            self.log_label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    VPNApp().run()
