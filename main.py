from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import socket
from threading import Thread
from jnius import autoclass

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"

        MDTextField:
            id: server
            hint_text: "Enter Server Address"
            mode: "rectangle"

        MDTextField:
            id: port
            hint_text: "Enter Port"
            mode: "rectangle"
            input_filter: "int"

        MDTextField:
            id: username
            hint_text: "Enter Username"
            mode: "rectangle"

        MDTextField:
            id: password
            hint_text: "Enter Password"
            mode: "rectangle"
            password: True

        MDRaisedButton:
            text: "Connect"
            on_release: app.connect_to_server()

        MDRaisedButton:
            text: "Enable VPN"
            on_release: app.enable_vpn()

        ScrollView:
            MDLabel:
                id: log
                text: "Logs will appear here..."
                size_hint_y: None
                height: self.texture_size[1]
                markup: True
                halign: "left"
'''

class UDPApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def connect_to_server(self):
        server = self.root.ids.server.text
        port = self.root.ids.port.text
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        if not server or not port or not username or not password:
            self.log_message("[color=ff0000]All fields are required![/color]")
            return

        try:
            port = int(port)
            self.log_message(f"Connecting to {server}:{port} as {username}...")
            Thread(target=self.udp_connection, args=(server, port, username, password), daemon=True).start()
        except ValueError:
            self.log_message("[color=ff0000]Invalid port number![/color]")

    def udp_connection(self, server, port, username, password):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(5)

            # Example authentication message
            auth_message = f"{username}:{password}"
            sock.sendto(auth_message.encode(), (server, port))
            self.log_message("[color=00ff00]Authentication sent![/color]")

            # Waiting for response
            response, _ = sock.recvfrom(1024)
            self.log_message(f"[color=00ff00]Server response: {response.decode()}[/color]")

        except socket.timeout:
            self.log_message("[color=ff0000]Connection timed out![/color]")
        except Exception as e:
            self.log_message(f"[color=ff0000]Error: {str(e)}[/color]")
        finally:
            sock.close()

    def enable_vpn(self):
        try:
            self.log_message("[color=00ff00]Enabling VPN...[/color]")
            VpnService = autoclass('android.net.VpnService')
            Intent = autoclass('android.content.Intent')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            activity = PythonActivity.mActivity
            intent = Intent(activity, VpnService)
            intent.setAction(VpnService.ACTION_VPN_SERVICE)
            activity.startActivity(intent)
            self.log_message("[color=00ff00]VPN Service started successfully![/color]")

        except Exception as e:
            self.log_message(f"[color=ff0000]Error enabling VPN: {str(e)}[/color]")

    def log_message(self, message):
        log_label = self.root.ids.log
        log_label.text += f"\n{message}"
        log_label.texture_update()

UDPApp().run()
