#!/bin/bash

gst-launch-1.0 rtspsrc location=rtsp://$1:8554/stream ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! videobalance saturation=0.0 ! videoconvert ! autovideosink sync=false
