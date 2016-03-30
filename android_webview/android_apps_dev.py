from graphviz import Digraph


def webview41():
    G = Digraph(name='Android Webview 4.1~4.3', node_attr={'shape': 'plaintext'})

    G.node('android_framework', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="2">Android Framework</TD>
        </TR>
        <TR>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>WebView API</TD> </TR>
                <TR> <TD>WebViewFactory WebViewClassic</TD> </TR>
                <TR> <TD>WebViewCore</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.node('android_jni', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="2">Android JNI</TD>
        </TR>
        <TR>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>Android WebCore JNI</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.node('webkit', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="2">WebKit</TD>
        </TR>
        <TR>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>WebCoreSupport</TD> </TR>
                <TR> <TD>WebCore</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.edge("android_framework", "android_jni", color="blue")
    G.edge("android_jni", "webkit", color="blue")
    return G


def webview44():
    G = Digraph(name='Android Webview 4.4+', node_attr={'shape': 'plaintext'})

    G.node('android_framework', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="2">Android Framework</TD>
        </TR>
        <TR>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>WebView API</TD> </TR>
                <TR> <TD>WebViewChromium</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.node('chromium_android_webview', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="2">Chromium android_webview</TD>
        </TR>
        <TR>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>AwContents</TD> </TR>
                <TR> <TD>ContentViewCore</TD> </TR>
                <TR> <TD>Content</TD> </TR>
                <TR> <TD>Blink</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")


    G.edge("android_framework", "chromium_android_webview", color="blue")
    return G


def apps_and_browser():
    G = Digraph(name='Apps and Browser', node_attr={'shape': 'plaintext'})

    G.node('webview_framework', label="""<
    <TABLE>
        <TR>
            <TD ROWSPAN="0" COLSPAN="3">
            <TABLE>
            <TR> <TD>Default Browser</TD> </TR>
            <TR> <TD ROWSPAN="2" PORT="webview">Android Framework<BR/>WebView API</TD> </TR>
            </TABLE> </TD>
            <TD ROWSPAN="1" COLSPAN="3">
            <TABLE BGCOLOR="grey">
                <TR> <TD>Android 4.0</TD> </TR>
                <TR> <TD>Android 4.1~4.3</TD> </TR>
                <TR> <TD>Android 4.4+</TD> </TR>
            </TABLE> </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.node('Apps', label="""<
    <TABLE>
        <TR> <TD>Apps</TD>
        </TR>
    </TABLE>>""", shape="box")

    G.edge("Apps", "webview_framework:webview", color="blue")
    return G


def pc_website():
    G = Digraph(name='website on pc dev', node_attr={'shape': 'plaintext'})

    G.node('pc_chrome', label="""<
    <TABLE>
        <TR> <TD>Debug Tools</TD> </TR>
        <TR> <TD>Chrome</TD> </TR>
        <TR> <TD>PC</TD> </TR>
    </TABLE>>""", shape="box")

    G.node('mobile_web', label="""<
    <TABLE BGCOLOR="grey">
        <TR> <TD> JavaScript </TD> </TR>
        <TR> <TD> CSS </TD> </TR>
        <TR> <TD> HTML </TD> </TR>
    </TABLE>>""", shape="box")

    G.edge("mobile_web", "pc_chrome", color="blue")
    return G

def pcdebug_mobilewebsite():
    G = Digraph(name='website on pc debuging', node_attr={'shape': 'plaintext'})

    G.node('pc_chrome_remote', label="""<
    <TABLE>
        <TR> <TD> Remote Debug Tools </TD> </TR>
        <TR> <TD> Chrome </TD> </TR>
        <TR> <TD> PC </TD> </TR>
    </TABLE>>""", shape="box")

    G.node('mobile_web', label="""<
    <TABLE>
        <TR>
            <TD> Mobile Browser </TD>
            <TD BGCOLOR="grey">
                <TABLE ROWSPAN="1" BGCOLOR="grey">
                    <TR> <TD> JavaScript </TD> </TR>
                    <TR> <TD> CSS </TD> </TR>
                    <TR> <TD> HTML </TD> </TR>
                </TABLE>
            </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.edge("mobile_web", "pc_chrome_remote", label="webdriver", color="blue")
    return G


def hand_mobiledebug_mobileapp():
    G = Digraph(name='website on mobile hand debuging', node_attr={'shape': 'plaintext'})

    G.node('mobile_app', label="""<
    <TABLE>
        <TR>
            <TD>
            <TABLE>
                <TR>
                    <TD> Webview </TD>
                    <TD>
                        <TABLE ROWSPAN="1" BGCOLOR="grey">
                            <TR> <TD> JavaScript </TD> </TR>
                            <TR> <TD> CSS </TD> </TR>
                            <TR> <TD> HTML </TD> </TR>
                        </TABLE>
                    </TD>
                </TR>
            </TABLE>
            </TD>
            <TD COLSPAN="3">Native</TD>
        </TR>
        <TR> <TD COLSPAN="6">Apps</TD> </TR>
    </TABLE>>""", shape="box")

    G.node('automatic_real_devices', label="""<
    <TABLE>
        <TR> <TD> Android SDK </TD></TR>
        <TR> <TD> Hand </TD></TR>
    </TABLE>>""", shape="box")

    G.edge("automatic_real_devices", "mobile_app", color="blue")
    return G


def automaticdebug_mobileapp():
    G = Digraph(name='website on mobile auto debuging', node_attr={'shape': 'plaintext'})
    G.node('mobile_app', label="""<
    <TABLE>
        <TR>
            <TD>
            <TABLE>
                <TR>
                    <TD> Webview </TD>
                    <TD>
                        <TABLE ROWSPAN="1" BGCOLOR="grey">
                            <TR> <TD> JavaScript </TD> </TR>
                            <TR> <TD> CSS </TD> </TR>
                            <TR> <TD> HTML </TD> </TR>
                        </TABLE>
                    </TD>
                </TR>
            </TABLE>
            </TD>
            <TD COLSPAN="3">Native</TD>
        </TR>
        <TR> <TD COLSPAN="6">Apps</TD> </TR>
    </TABLE>>""", shape="box")

    G.node('automatic_real_devices', label="""<
    <TABLE>
        <TR>
            <TD>
                <TABLE>
                    <TR> <TD> Android SDK </TD></TR>
                    <TR> <TD> USB/Wifi </TD></TR>
                </TABLE>
            </TD>
        </TR>
        <TR> <TD> ChromeDriver/selendroid<BR/>UIautomata/UIautomation </TD></TR>
        <TR>
            <TD>
                <TABLE>
                    <TR> <TD> Appium Server </TD></TR>
                    <TR> <TD> Appium Binding </TD></TR>
                    <TR> <TD> Test </TD></TR>
                </TABLE>
            </TD>
        </TR>
    </TABLE>>""", shape="box")

    G.edge("automatic_real_devices", "mobile_app", color="blue")
    return G

