from mitmproxy import http

# 🧡 Cyber Proxy: reroutes and responds with style
def request(flow: http.HTTPFlow):
    # 🔁 Redirect traffic from example.com to mitmproxy.org
    if flow.request.pretty_host == "example.com":
        flow.request.host = "mitmproxy.org"

    # 🍵 Respond to /brew with a glowing teapot status
    elif flow.request.path.endswith("/brew"):
        flow.response = http.Response.make(
            418,  # I'm a teapot
            b"I'm a teapot",  # Glowing orange payload
            {"Content-Type": "text/plain"}
        )
