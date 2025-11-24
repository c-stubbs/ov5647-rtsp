#!/bin/bash

rpicam-vid -t 0 --width 720 --height 480 --framerate 15 --inline -o udp://127.0.0.1:5000
