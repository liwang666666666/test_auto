#! /bin/bash

    adb shell "sed -i 's/BtLocalDeviceName=Pixy/BtLocalDeviceName=liwang6/'  /etc/bluetooth/bt_app.conf"


 adb shell "reboot -f"

 adb wait-for-device root
