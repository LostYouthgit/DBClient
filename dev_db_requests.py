import MySQLdb
import dev_types
import datetime
import db_connect
import json
import calib_json

qr_code = ""
fields = {"region": 'EU',
          "_operator": 'e',
          "_success": '1',
          "_info": '1',
          "_grade": '1'
          }


class DB:
    def __init__(self):
        self.__host = db_connect.host
        self.__user = db_connect.user
        self.__pass = db_connect.passwd
        self.__db = db_connect.db
        self.db = MySQLdb.connect(host=self.__host,
                                  user=self.__user,
                                  passwd=self.__pass,
                                  db=self.__db)

        self.cur = self.db.cursor()
        self.dev_id = ""
        self.board_name = ""
        self.dev_type = ""
        self.time = ""
        self.color = ""
        self.konstruct()

    def konstruct(self):
        from qr_scanner_handler import qr
        global qr_code
        qr_code = qr
        self.dev_id = qr[:6]
        if not qr:
            print("NOT QR")
            return
        if int(qr[-3:-1], 16) >= 10:
            self.dev_type = int(qr[-3:-1], 16)
        else:
            self.dev_type = qr[-3:-1]
        self.board_name = dev_types.board_name["{}".format(self.dev_type)]
        self.time = datetime.datetime.now()
        if int(qr[-1]) == 1:
            self.color = "white"
        else:
            self.color = "black"

    def register(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_register (qr, region, dev_id, board_name, dev_type, color) VALUES (%s, %s, %s, %s, %s, %s)"  # <<< REGISTER
        val = (qr_code, fields["region"], self.dev_id, self.board_name, self.dev_type, self.color)
        self.cur.execute(sql, val)

    def add_prog(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_prog (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"  # <<< PROG
        val = (qr_code, fields["_operator"], fields["_success"], self.time, fields["_info"])

        self.cur.execute(sql, val)

    def add_assembler(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_assembling (qr, operator, success, time) VALUES (%s, %s, %s, %s)"  # <<< ASSEMBLING
        val = (qr_code, fields["_operator"], fields["_success"], self.time)

        self.cur.execute(sql, val)

    def add_longtest(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_long_test (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"  # <<< PROG
        val = (qr_code, fields["_operator"], fields["_success"], self.time, fields["_info"])

        self.cur.execute(sql, val)

    def add_testroom(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_test_room (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"  # <<< PROG
        val = (qr_code, fields["_operator"], fields["_success"], self.time, fields["_info"])

        self.cur.execute(sql, val)

    def add_calibration(self):
        global qr_code
        if self.board_name == "mpo":

            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.mpo_calib))

            self.cur.execute(sql, val)

        if self.board_name == "mpc":
            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.mpc_calib))

            self.cur.execute(sql, val)

        if self.board_name == "motion_plus":
            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.mpp_calib))

            self.cur.execute(sql, val)

        if self.board_name == "fire_protect":
            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.fp_calib))

            self.cur.execute(sql, val)

        if self.board_name == "fire_protect_plus":
            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.fpp_calib_cam))

            self.cur.execute(sql, val)

            sql = "INSERT INTO debug_production.dev_calibration (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"
            val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.fpp_calib_co))

            self.cur.execute(sql, val)

    def add_qc(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_qc (qr, operator, success, time, info, grade) VALUES (%s, %s, %s, %s, %s, %s)"  # <<< QC
        val = (qr_code, fields["_operator"], fields["_success"], self.time, fields["_info"], fields["_grade"])

        self.cur.execute(sql, val)

    def add_packer(self):
        global qr_code
        sql = "INSERT INTO debug_production.dev_pack (qr, operator, success, time) VALUES (%s, %s, %s, %s)"  # <<< ASSEMBLING
        val = (qr_code, fields["_operator"], fields["_success"], self.time)

        self.cur.execute(sql, val)

    def change_freq(self, freq):
        self.freq = freq
        sql = "UPDATE debug_production.dev_register SET region = %s WHERE qr = %s"  # <<< freq
        val = (self.freq, fields["qr"])

        self.cur.execute(sql, val)

    def remove_assembler(self):
        global qr_code
        sql = "UPDATE debug_production.dev_register SET info_assembling = '' WHERE qr = %s"  # <<< --assembler
        val = (qr_code,)

        self.cur.execute(sql, val)

    def remove_packer(self):
        global qr_code
        sql = "UPDATE debug_production.dev_register SET info_pack = '' WHERE qr = %s"  # <<< --pack
        val = (qr_code,)

        self.cur.execute(sql, val)

    def delete(self):
        try:
            global qr_code
            tables = ['dev_pack', "dev_qc", "dev_long_test", "dev_test_room", "dev_calibration", "dev_assembling", "dev_prog", "dev_repair", "dev_register"]
            for table in tables:
                sql = "DELETE FROM debug_production.{0} WHERE qr = %s".format(table)
                val = (qr_code,)
                self.cur.execute(sql, val)

        except Exception as ex:
            print(ex)

    def save_changes(self):
        self.cur.execute("SELECT * FROM dev_register ORDER BY id DESC LIMIT 5;")
        res = str(self.cur.fetchall())
        res = res.replace("), ", "\n")
        self.db.autocommit(True)
        self.db.close()
        return res
