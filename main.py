from kivy.lang import Builder
from kivymd.app import MDApp
from jnius import autoclass, cast

# مكونات أندرويد الضرورية
PythonActivity = autoclass('org.kivy.android.PythonActivity')
VpnService = autoclass('android.net.VpnService')
Intent = autoclass('android.content.Intent')

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    MDTextField:
        id: server_ip
        hint_text: "Server IP"
        helper_text: "أدخل عنوان الخادم"

    MDTextField:
        id: port
        hint_text: "Port"
        helper_text: "أدخل المنفذ"

    MDTextField:
        id: username
        hint_text: "Username"
        helper_text: "أدخل اسم المستخدم"

    MDTextField:
        id: password
        hint_text: "Password"
        helper_text: "أدخل كلمة المرور"
        password: True

    MDRaisedButton:
        id: connect_btn
        text: "Connect"
        on_release: app.connect_vpn()

    MDRaisedButton:
        id: disconnect_btn
        text: "Disconnect"
        on_release: app.disconnect_vpn()

    MDLabel:
        id: status
        text: "Status: Disconnected"
        halign: "center"
'''

class VPNApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.vpn_service = None
        return Builder.load_string(KV)

    def connect_vpn(self):
        # طلب إذن تفعيل VPN
        intent = Intent(PythonActivity.mActivity, VpnService)
        PythonActivity.mActivity.startActivityForResult(intent, 0)

        # محاكاة الاتصال (يجب استبدالها بكود VPN حقيقي)
        self.root.ids.status.text = "Status: Connecting..."
        
        # بعد الاتصال الناجح:
        self.root.ids.status.text = "Status: Connected"

    def disconnect_vpn(self):
        # محاكاة إيقاف الاتصال
        if self.vpn_service:
            self.vpn_service.disconnect()
        self.root.ids.status.text = "Status: Disconnected"

if __name__ == "__main__":
    VPNApp().run()
