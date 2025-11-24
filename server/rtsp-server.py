import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')

from gi.repository import Gst, GstRtspServer, GLib

Gst.init(None)

def main():
    server = GstRtspServer.RTSPServer()
    server.set_address("0.0.0.0")
    server.set_service("8554")
    mount = server.get_mount_points()

    pipeline = (
    	"( udpsrc port=5000 buffer-size=26214400 caps=\"video/x-h264,stream-format=byte-stream,alignment=nal\" ! "
    	" queue max-size-buffers=0 max-size-time=0 max-size-bytes=10000000 leaky=downstream ! "
        "h264parse config-interval=1 ! rtph264pay name=pay0 pt=96 mtu=1200 )"
    )

    factory = GstRtspServer.RTSPMediaFactory()
    factory.set_launch(pipeline)
    mount.add_factory("/stream", factory)

    server.attach(None)
    print("RTSP server started at rtsp://@:8554/test")
    loop = GLib.MainLoop()
    loop.run()

if __name__ == '__main__':
    main()

