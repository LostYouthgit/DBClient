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
          "_grade": '0'
          }


class DB_Central:
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
        self.central_id = ""
        self.board_name = ""
        self.dev_type = "33"
        self.hub_subtype = ""
        self.time = ""
        self.color = ""
        self.konstruct()

    def konstruct(self):
        from qr_scanner_handler import qr
        global qr_code
        qr_code = qr[:9] + "**-*****-*" + qr[19:]
        self.central_id = qr[:9].replace("-", "")
        print(qr_code)
        if not qr:
            print("NOT QR")
            return
        if qr_code[19] == "1":
            self.color = "white"
        if qr_code[19] == "2":
            self.color = "black"
        if qr_code[20] == "1":
            self.hub_subtype = "1"
        if qr_code[20] == "3":
            self.hub_subtype = "2"
        if qr_code[20] == "3":
            self.hub_subtype = "3"
        if qr_code[20] == "4":
            self.hub_subtype = "4"
        if qr_code[20] == "5":
            self.hub_subtype = "5"
        else:
            pass
        self.board_name = dev_types.board_name_hub["{}".format(self.hub_subtype)]
        self.time = datetime.datetime.now()

    def register(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_register (qr, region, central_id, board_name, dev_type, hub_subtype, color) VALUES (%s, %s, %s, %s, %s, %s, %s)"  # <<< REGISTER
        val = (qr_code, fields["region"], self.central_id, self.board_name, self.dev_type, self.hub_subtype, self.color)
        self.cur.execute(sql, val)

    def add_prog(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_prog (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"  # <<< PROG
        val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.hub_prog_info))

        self.cur.execute(sql, val)

    def add_assembler(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_assembling (qr, operator, success, time) VALUES (%s, %s, %s, %s)"  # <<< ASSEMBLING
        val = (qr_code, fields["_operator"], fields["_success"], self.time)

        self.cur.execute(sql, val)

    def add_longtest(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_long_test (qr, operator, success, time, info) VALUES (%s, %s, %s, %s, %s)"  # <<< PROG
        val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.hub_long_info))

        self.cur.execute(sql, val)

    def add_qc(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_qc (qr, operator, success, time, info, grade) VALUES (%s, %s, %s, %s, %s, %s)"  # <<< QC
        val = (qr_code, fields["_operator"], fields["_success"], self.time, json.dumps(calib_json.hub_qc_info), fields["_grade"])

        self.cur.execute(sql, val)

    def add_packer(self):
        global qr_code
        sql = "INSERT INTO debug_production.central_pack (qr, operator, success, time) VALUES (%s, %s, %s, %s)"  # <<< ASSEMBLING
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
            tables = ['central_pack', "central_qc", "central_long_test", "central_assembling", "central_prog", "central_repair", "central_register"]
            for table in tables:
                sql = "DELETE FROM debug_production.{0} WHERE qr = %s".format(table)
                val = (qr_code,)
                self.cur.execute(sql, val)

        except Exception as ex:
            print(ex)

    def save_changes(self):
        self.cur.execute("SELECT * FROM central_register ORDER BY id DESC LIMIT 5;")
        res = str(self.cur.fetchall())
        res = res.replace("), ", "\n")
        self.db.autocommit(True)
        return res

    def close_conn(self):
        self.db.close()

