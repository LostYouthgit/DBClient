from main_gui import Ui_MainWindow
from PySide2 import QtWidgets
from dev_db_requests import DB
from qr_scanner_handler import QR
from central_db_requests import DB_Central

qr = ""


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
        print("dsad")
        for a in range(i):
            self.comboBox.addItem(self.port_list[a])

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
        self.START_HUB.clicked[bool].connect(self.start)
        self.REGISTER_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_PROG_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_ASSEMBLER_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_LONGTEST_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_QC_HUB.clicked[bool].connect(self.set_action_hub)
        self.ADD_PACKER_HUB.clicked[bool].connect(self.set_action_hub)
        self.DELETE_HUB.clicked[bool].connect(self.set_action_hub)

    def set_action(self, pressed):
        source = self.sender()
        if pressed:
            if source.objectName() == 'REGISTER':
                self.register = 1
            if source.objectName() == 'ADD_PROG':
                self.add_prog = 1
            if source.objectName() == 'ADD_ASSEMBLER':
                self.add_assembler = 1
            if source.objectName() == 'ADD_LONGTEST':
                self.add_longtest = 1
            if source.objectName() == 'ADD_TESTROOM':
                self.add_testroom = 1
            if source.objectName() == 'ADD_QC':
                self.add_qc = 1
            if source.objectName() == 'ADD_PACKER':
                self.add_packer = 1
            if source.objectName() == 'ADD_CALIB':
                self.add_calib = 1
            if source.objectName() == 'DELETE':
                self.delete = 1

            else:
                pass
        else:
            if source.objectName() == 'REGISTER':
                self.register = 0
            elif source.objectName() == 'ADD_PROG':
                self.add_prog = 0
            elif source.objectName() == 'ADD_ASSEMBLER':
                self.add_assembler = 0
            elif source.objectName() == 'ADD_LONGTEST':
                self.add_longtest = 0
            elif source.objectName() == 'ADD_TESTROOM':
                self.add_testroom = 0
            elif source.objectName() == 'ADD_QC':
                self.add_qc = 0
            elif source.objectName() == 'ADD_PACKER':
                self.add_packer = 0
            elif source.objectName() == 'ADD_CALIB':
                self.add_calib = 0
            elif source.objectName() == 'DELETE':
                self.delete = 0

    def set_action_hub(self, pressed):
        source = self.sender()
        if pressed:
            if source.objectName() == 'REGISTER_HUB':
                self.register_hub = 1
            if source.objectName() == 'ADD_PROG_HUB':
                self.add_prog_hub = 1
            if source.objectName() == 'ADD_ASSEMBLER_HUB':
                self.add_assembler_hub = 1
            if source.objectName() == 'ADD_LONGTEST_HUB':
                self.add_longtest_hub = 1
            if source.objectName() == 'ADD_QC_HUB':
                self.add_qc_hub = 1
            if source.objectName() == 'ADD_PACKER_HUB':
                self.add_packer_hub = 1
            if source.objectName() == 'DELETE_HUB':
                self.delete_hub = 1

            else:
                pass
        else:
            if source.objectName() == 'REGISTER_HUB':
                self.register_hub = 0
            elif source.objectName() == 'ADD_PROG_HUB':
                self.add_prog_hub = 0
            elif source.objectName() == 'ADD_ASSEMBLER_HUB':
                self.add_assembler_hub = 0
            elif source.objectName() == 'ADD_LONGTEST_HUB':
                self.add_longtest_hub = 0
            elif source.objectName() == 'ADD_QC_HUB':
                self.add_qc_hub = 0
            elif source.objectName() == 'ADD_PACKER_HUB':
                self.add_packer_hub = 0
            elif source.objectName() == 'DELETE_HUB':
                self.delete_hub = 0

    def start(self):
        try:
            self.exc_label.setText("")
            scanner = QR()
            scanner.qr(self.comboBox.currentText())
            from qr_scanner_handler import qr
            if len(qr) == 9:
                self.doAction(self.register, self.add_prog, self.add_assembler, self.add_longtest, self.add_testroom, self.add_qc, self.add_packer, self.add_calib, self.delete)
            if len(qr) == 23:
                self.doAction_hub(self.register_hub, self.add_prog_hub, self.add_assembler_hub, self.add_longtest_hub, self.add_qc_hub, self.add_packer_hub, self.delete_hub)
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
            if self.add_calib == 1:
                db.add_calibration()
            if self.add_longtest == 1:
                db.add_longtest()
            if self.add_testroom == 1:
                db.add_testroom()
            if self.add_qc == 1:
                db.add_qc()
            if self.add_packer == 1:
                db.add_packer()
            if self.delete == 1:
                db.delete()
            else:
                pass
            res = db.save_changes()
            self.output_label.setWordWrap(True)
            self.output_label.setText("{}".format(res))
        except Exception as err:
            self.exc_label.setText("{}".format(err))

    def doAction_hub(self, register_hub, add_prog_hub, add_assembler_hub, add_longtest_hub, add_qc_hub, add_packer_hub, delete_hub):
        self.register_hub = register_hub
        self.add_prog_hub = add_prog_hub
        self.add_assembler_hub = add_assembler_hub
        self.add_longtest_hub = add_longtest_hub
        self.add_qc_hub = add_qc_hub
        self.add_packer_hub = add_packer_hub
        self.delete_hub = delete_hub
        try:
            from qr_scanner_handler import qr
            db = DB_Central()
            if self.register_hub == 1:
                db.register()
            if self.add_prog_hub == 1:
                db.add_prog()
            if self.add_assembler_hub == 1:
                db.add_assembler()
            if self.add_longtest_hub == 1:
                db.add_longtest()
            if self.add_qc_hub == 1:
                db.add_qc()
            if self.add_packer_hub == 1:
                db.add_packer()
            if self.delete_hub == 1:
                db.delete()
            else:
                pass
            res = db.save_changes()
            self.output_label_hub.setWordWrap(True)
            self.output_label_hub.setText("{}".format(res))
        except Exception as err:
            self.exc_label_hub.setText("{}".format(err))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MainT()
    w.show()
    app.exec_()
