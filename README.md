# fanControllerPi
Fan controller in Python for raspberry pi jessie.

1. Copy fan.py to a local directory
2. Be sure it will be executable (sudo chmod +x fan.py)
3. Copy fancontroller.service to /lib/systemd/system/fancontroller.service
4. Enable the service on systemd: sudo systemctl enable fancontroller.service
5. Test the service: sudo systemctl start mouselogger.service
6. Test the service: ps -ef | grep fan.py
7. Reboot and test fan controller
