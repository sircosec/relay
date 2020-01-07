I have a lamp. Actually, I have a lamp with four separate bulbs that I like to control together. I decided to put my lamp in my workshop and have it be motion-controlled. I'm using a 4-way relay, cheap PIR motion sensor, and a raspberry pi zero running raspbian lite to be the brains.

The idea was that the lamp should turn on when it senses motion for a minimum of five minutes. If no further motion is detected within those five minutes, the lamps should turn off. If motion is detected again, the counter should restart. If everything works correctly, after five minutes of no activity, everything should turn off and wait for motion.

I also installed it as a service which should run automatically anytime the machine is running. I configured it to log events to 
/var/log/pir_lamps/ and also set it to logrotate automatically.
