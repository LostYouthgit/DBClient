import serial

from serial.tools.list_ports import comports

qr = ""
mas = []


class QR:
    @staticmethod
    def port_choose():
        global mas
        for c in comports():
            mas.append(c.device)
        return mas

    @staticmethod
    def qr(port):
        try:
            with serial.Serial('{}'.format(port), 115200, timeout=3) as ser:
                line = ser.readline(20)
                global qr
                line_str = str(line)
                qr = line_str[2:-5:1]
                return
        except serial.serialutil.SerialException:
            pass