from main_gui import Ui_MainWindow
from PySide2 import QtWidgets
from dev_db_requests import DB
from qr_scanner_handler import QR
from central_db_requests import DB_Central
from qr_scanner_handler import qr


class MainT(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainT, self).__init__()
        self.setupUi(self)
        self.register = 0
        self.register_hub = 0
        self.add_prog = 0
        self.add_prog_hub = 0
        self.add_assembler = 0
        self.add_assembler_hub = 0
        self.add_longtest = 0
        self.add_longtest_hub = 0
        self.add_testroom = 0
        self.add_qc = 0
        self.add_qc_hub = 0
        self.add_packer = 0
        self.add_packer_hub = 0
        self.add_calib = 0
        self.delete = 0
        self.delete_hub = 0
        self.UI()

    def port_choose(self):
        self.port_list = QR().port_choose()
        i = len(self.port_list)
        self.comboBox.clear()
        for a in range(i):
            self.comboBox.addItem(self.port_list[a])
            self.comboBox_hub.addItem(self.port_list[a])
            #self.comboBox.update()

    def UI(self):
        self.comboBox.view().pressed.connect(self.port_choose())
        self.REGISTER.clicked[bool].connect(self.set_action)
        self.ADD_PROG.clicked[bool].connect(self.set_action)
        self.ADD_ASSEMBLER.clicked[bool].connect(self.set_action)
        self.ADD_LONGTEST.clicked[bool].connect(self.set_action)
        self.ADD_TESTROOM.clicked[bool].connect(self.set_action)
        self.ADD_QC.clicked[bool].connect(self.set_action)
        self.ADD_PACKER.clicked[bool].connect(self.set_action)
        self.ADD_CALIB.clicked[bool].connect(self.set_action)
        self.DELETE.clicked[bool].connect(self.set_action)
        self.START.clicked.connect(self.start)
        self.REGISTER_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_PROG_HUB.clicked[bool].connect(self.set_action_hub)
        self.DELETE_HUB.clicked[bool].connect(self.set_action_hub)

    def set_action(self, pressed):
        source = self.sender()
        if pressed:
            if source.text() == 'REGISTER':
                self.register = 1
            if source.text() == 'ADD PROG':
                self.add_prog = 1
            if source.text() == 'ADD ASSEMBLER':
                self.add_assembler = 1
            if source.text() == 'ADD LONGTEST':
                self.add_longtest = 1
            if source.text() == 'ADD TESTROOM':
                self.add_testroom = 1
            if source.objectName() == 'ADD_QC':
                self.add_qc = 1
            if source.text() == 'ADD PACKER':
                self.add_packer = 1
            if source.text() == 'ADD CALIB':
                self.add_calib = 1
            if source.text() == 'DELETE':
                self.delete = 1

            else:
                pass
        else:
            if source.text() == 'REGISTER':
                self.register = 0
            elif source.text() == 'ADD PROG':
                self.add_prog = 0
            elif source.text() == 'ADD ASSEMBLER':
                self.add_assembler = 0
            elif source.text() == 'ADD LONGTEST':
                self.add_longtest = 0
            elif source.text() == 'ADD TESTROOM':
                self.add_testroom = 0
            elif source.text() == 'ADD QC':
                self.add_qc = 0
            elif source.text() == 'ADD PACKER':
                self.add_packer = 0
            elif source.text() == 'ADD CALIB':
                self.add_calib = 0
            elif source.text() == 'DELETE':
                self.delete = 0

    def set_action_hub(self, pressed):
        source = self.sender()
        if pressed:
            if source.objectName() == 'REGISTER_HUB':
                self.register = 1
            if source.objectName() == 'ADD_PROG_HUB':
                self.add_prog = 1
            if source.objectName() == 'ADD_ASSEMBLER_HUB':
                self.add_assembler = 1
            if source.objectName() == 'ADD_LONGTEST_HUB':
                self.add_longtest = 1
            if source.objectName() == 'ADD_QC':
                self.add_qc = 1
            if source.objectName() == 'ADD_PACKER_HUB':
                self.add_packer = 1
            if source.objectName() == 'DELETE_HUB':
                self.delete = 1

            else:
                pass
        else:
            if source.objectName() == 'REGISTER_HUB':
                self.register = 0
            elif source.objectName() == 'ADD_PROG_HUB':
                self.add_prog = 0
            elif source.objectName() == 'ADD_ASSEMBLER_HUB':
                self.add_assembler = 0
            elif source.objectName() == 'ADD_LONGTEST_HUB':
                self.add_longtest = 0
            elif source.objectName() == 'ADD_QC_HUB':
                self.add_qc = 0
            elif source.objectName() == 'ADD_PACKER_HUB':
                self.add_packer = 0
            elif source.objectName() == 'DELETE_HUB':
                self.delete = 0

    def start(self):
        try:
            self.exc_label.setText("")
            scanner = QR()
            scanner.qr(self.comboBox.currentText())

            self.doAction(self.register, self.add_prog, self.add_assembler, self.add_longtest, self.add_testroom, self.add_qc, self.add_packer, self.add_calib, self.delete)

        except Exception as err:
            self.exc_label.setText("{}".format(err))

    def doAction(self, register, add_prog, add_assembler, add_longtest, add_testroom, add_qc, add_packer, add_calib, delete):
        self.register = register
        self.add_prog = add_prog
        self.add_assembler = add_assembler
        self.add_longtest = add_longtest
        self.add_testroom = add_testroom
        self.add_qc = add_qc
        self.add_packer = add_packer
        self.add_calib = add_calib
        self.delete = delete
        try:
            from qr_scanner_handler import qr
            db = DB()
            if self.register == 1:
                db.register()
            if self.add_prog == 1:
                db.add_prog()
            if self.add_assembler == 1:
                db.add_assembler()
            if self.add_longtest == 1:
                db.add_longtest()
            if self.add_testroom == 1:
                db.add_testroom()
            if self.add_qc == 1:
                db.add_qc()
            if self.add_packer == 1:
                db.add_packer()
            if self.add_calib == 1:
                db.add_calibration()
            if self.delete == 1:
                db.delete()
            else:
                pass
            res = db.save_changes()
            self.output_label.setWordWrap(True)
            self.output_label.setText("{}".format(res))
        except Exception as err:
            self.exc_label.setText("{}".format(err))

    def doAction_hub(self, register, add_prog, add_assembler, add_longtest, add_testroom, add_qc, add_packer, add_calib, delete):
        self.register = register
        self.add_prog = add_prog
        self.add_assembler = add_assembler
        self.add_longtest = add_longtest
        self.add_testroom = add_testroom
        self.add_qc = add_qc
        self.add_packer = add_packer
        self.add_calib = add_calib
        self.delete = delete
        try:
            from qr_scanner_handler import qr
            print("SSS")
            db = DB_Central()
            if self.register == 1:
                db.register()
            if self.add_prog == 1:
                db.add_prog()
            else:
                pass
            res = db.save_changes()
            self.output_label.setWordWrap(True)
            self.output_label.setText("{}".format(res))
        except Exception as err:
            self.exc_label.setText("{}".format(err))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MainT()
    w.show()
    app.exec_()
