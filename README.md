DRV8825-with-Raspberry-Pi-3
---------------------------

**Python 3 script running under raspbian on a Raspberry Pi 3 for testing or controlling a DRV8825 Stepper Motor Driver with reading of the fault output.**

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/514e98c7e8b54fe990d1ec8757c486d1)](https://www.codacy.com/app/daniel_43/DRV8825-with-Raspberry-Pi-3?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mauricesifrt/DRV8825-with-Raspberry-Pi-3&amp;utm_campaign=Badge_Grade)

----------


Actually this script was likely written for educational and testing purpose only.
Now I want to share and improve the script for people who have no idea how to control the DRV8825 bipolar stepper motor driver with it's step/dir interface and a raspberry pi 3

**Features:**

- Output of hardware PWM for the step-pin
- Reading output of the fault pin and give out errors (needs improvement)
- Choosing in and output pin as well as frequency and duty cycle userfriendly
- Choosing direction of the motor

**Planned:**

- This script will be replaced by a new project: https://github.com/dan-nkl/RASPI3-DRV8825
