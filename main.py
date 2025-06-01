from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == 'android':
    from android import mActivity
    from jnius import autoclass
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')


class WebApp(App):
    def build(self):
        if platform == 'android':
            webview = WebView(mActivity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.setWebViewClient(WebViewClient())

            # Load local HTML file from assets
            webview.loadUrl("file:///android_asset/index.html")

            mActivity.setContentView(webview)
        else:
            from kivy.uix.label import Label
            return Label(text="WebView only supported on Android")


if __name__ == '__main__':
    WebApp().run()