I have a lamp. Actually, I have a lamp with four separate bulbs that I like to control together. I decided to put my lamp in my workshop and have it be motion-controlled. I'm using a 4-way relay, cheap PIR motion sensor, and a raspberry pi zero running raspbian lite to be the brains.

The idea was that the lamp should turn on when it senses motion for a minimum of five minutes. If no further motion is detected within those five minutes, the lamps should turn off. If motion is detected again, the counter should restart. If everything works correctly, after five minutes of no activity, everything should turn off and wait for motion.

I also installed it as a service which should run automatically anytime the machine is running. I configured it to log events to 
/var/log/pir_lamps/ and also set it to logrotate automatically.

Steps for configuring the service:

1. Copy the script to /usr/bin/pir_lamps.py

2. Create the service file: vim /lib/systemd/system/pir_lamps.service

3. Edit the service file like this:

[Unit]
Description=pir lamps service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/bin/pir_lamps_service.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target

4. Reload the service daemon: systemctl daemon-reload

5. Enable the service: systemctl enable pir_lamps.service

6. Start the service: systemctl start pir_lamps.service

7. Check the status of the service: systemctl status pir_lamps.service

It should now start and run at boot.

8. Verify that it's configured to run at boot: systemctl is-enabled pir_lamps

Now to set up the logrotation:

1. Create the config file for logrotate: vim /etc/logrotate.d/pir_lamps.conf

2. Edit the file to look like this:

/var/log/pir_lamps/* {
    daily
    rotate 7
    size 1M
    compress
    delaycompress
}

This will rotate logs daily, maintain 7 days worth, rotate files at 1 MB file size, compress all logs except the current log.
