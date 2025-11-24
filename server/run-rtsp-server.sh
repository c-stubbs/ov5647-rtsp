#!/bin/bash

cleanup() {
	echo ""
	echo "Ctrl+C detected! Stopping rtsp server..."

	kill $RTSP_SERVER 2>/dev/null
	kill $UDP_STREAM 2>/dev/null

	wait $RTSP_SERVER $UDP_STREAM 2>/dev/null

	echo "Server stopped."
	exit
}

trap cleanup SIGINT

echo "Starting RTSP server."
./udp_stream.sh 2>/dev/null &
UDP_STREAM=$!
echo "Internal UDP stream started."
python3 rtsp-server.py > /dev/null &
RTSP_SERVER=$!
echo "RTSP server started."
wait

