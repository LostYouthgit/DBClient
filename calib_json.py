true = True

mpo_calib = {
	"calib_info": "TOP=66;BOT=58;LIQ=63;TOP_CUR=300;BOT_CUR=300;LIQ_CUR=28",
	"final_calib_state": true,
	"result": true
}

mpc_calib = {
    "result": true,
    "calib_info": "EXT=69;EXT_CUR=38",
    "final_calib_state": true
}

mpp_calib = {
    "result": true,
    "calib_info": 135,
    "final_calib_state": true
}

fp_calib = {
    "smoke_camera": {"result": true, "calib_info": "43"},
    "final_calib_state": true
}

fpp_calib_cam = {
    "smoke_camera": {"result": true, "calib_info": "43"},
    "final_calib_state": true
}

fpp_calib_co = {
    "co_camera": {"co_high": {"calib_info": "924", "result": true},
    "co_low": {"calib_info": "2", "result": true}},
    "final_calib_state": true
}

mpo_prog_info = {
	"app_ver" : "2.37.1",
	"constants" : {
		"512_TEST" : {
			"AVERAGE_512_TIME" : "25",
			"FREQUENCY_DEVIATION" : "12",
			"MAX_V" : "3.4",
			"MIN_V" : "2.9"
		},
		"ANTI_MACKING" : {
			"MAX_BOT_DIFF" : "180",
			"MAX_BOT_OFFSET" : "120",
			"MAX_LIQ_DIFF" : "90",
			"MAX_LIQ_OFFSET" : "120",
			"MAX_TOP_DIFF" : "180",
			"MAX_TOP_OFFSET" : "120",
			"MAX_V" : "18",
			"MIN_BOT_DIFF" : "20",
			"MIN_BOT_OFFSET" : "20",
			"MIN_LIQ_DIFF" : "5",
			"MIN_LIQ_OFFSET" : "20",
			"MIN_TOP_DIFF" : "20",
			"MIN_TOP_OFFSET" : "20",
			"MIN_V" : "14"
		},
		"DEBUG_INIT" : {
			"START_TIME" : "3000"
		},
		"LEDS" : {
			"MAX_GREEN_V" : "2.6",
			"MAX_OFF_V" : "0.1",
			"MAX_RED_V" : "2.0",
			"MIN_GREEN_V" : "2.0",
			"MIN_RED_V" : "1.6"
		},
		"PIR" : {
			"DU_MAIN" : "50",
			"DU_OP" : "50",
			"HF_DETECT" : "5",
			"LF_DETECT" : "5",
			"MAX_CURRENT" : "300",
			"MAX_RMS" : "0.65",
			"MIN_CURRENT" : "250",
			"MIN_RMS" : "0.1",
			"WAIT_TIME" : "35"
		},
		"POWER_TEST" : {
			"MAX_CLOSED_KEY_V" : "3.4",
			"MAX_DCDC_V" : "3.1",
			"MAX_FULL_REV_CURRENT" : "3",
			"MAX_OPEN_KEY_V" : "0.1",
			"MAX_REV_CURRENT" : "30",
			"MAX_REV_V" : "3.1",
			"MIN_CLOSED_KEY_V" : "3.1",
			"MIN_DCDC_V" : "2.8",
			"MIN_FULL_REV_CURRENT" : "0",
			"MIN_REV_CURRENT" : "10",
			"MIN_REV_V" : "2.8"
		},
		"RFM_TEST" : {
			"FREQUENCY_DEVIATION" : "7",
			"MAX_MEAS" : "1000",
			"MIN_MEAS" : "840",
			"RSSI_RX" : "-70",
			"RSSI_TX" : "-87"
		},
		"SLEEP_CURRENT" : {
			"MAX_CURRENT" : "10"
		},
		"SMOKE_TEST" : {
			"MAX_V" : "3.1",
			"MIN_V" : "1.2"
		}
	},
	"fw_ver" : "3.52.0",
	"stand_id" : "ffa7b9",
	"stand_ver" : "2.25",
	"test_results" : {
		"DC/DC_V" : "2.94 V",
		"battery_1_v" : "2.907",
		"battery_2_v" : "2.907",
		"bot_diff" : "180",
		"bot_led_V" : "2.149 V",
		"bot_low" : "75",
		"closed_key_V" : "3.231 V",
		"closed_key_bat1_V" : "3.231 V",
		"closed_key_bat2_V" : "3.231 V",
		"crystal_dev" : "-3.9 us",
		"current" : "0.004mA",
		"fr_delta" : "0 Hz",
		"fr_dev" : -89,
		"fr_rssi_rx" : -49,
		"fr_rssi_tx" : -32,
		"fw_ver" : "3.52.0",
		"green_led_V" : "2.169 V",
		"label_du_main" : "0",
		"label_du_op" : "0",
		"label_hf_detect" : "1",
		"label_lf_detect" : "0",
		"liq_diff" : "23",
		"liq_low" : "58",
		"meas" : 958,
		"multiplier" : "14.762 V",
		"off_bot_led_V" : "0.001 V",
		"off_green_led_V" : "0.001 V",
		"off_red_led_V" : "0.001 V",
		"off_top_led_V" : "0.001 V",
		"open_key_V" : "0.001 V",
		"red_led_v" : "1.794 V",
		"rev_I_1" : "17.549 mA",
		"rev_I_2" : "18.194 mA",
		"rev_I_full" : "1.308 mA",
		"rev_V_1" : "2.95 V",
		"rev_V_2" : "2.95 V",
		"t_value" : "26 degrees",
		"top_diff" : "21",
		"top_led_V" : "2.165 V",
		"top_low" : "70"
	}
}

hub_prog_info = {
	"app_version" : "3.38.0",
	"fw_ver" : "4.50.0",
	"hw_ver" : "0700030101020100",
	"stand_id" : "ff1e4c",
	"stand_ver" : "2.25",
	"test_result" : {
		"IMEI" : "868728037898712",
		"acc_vol" : "4.03V",
		"charge_cur" : "-625.01mA",
		"charge_hysteresis" : "0.14V",
		"charge_vol_max" : "4.28V",
		"charge_vol_min" : "4.14V",
		"crystal_dev" : "-3.0",
		"eth_vol" : "3.254",
		"ext_cur" : "61.190mA",
		"fr_cor" : 0,
		"fr_delta_1" : -176,
		"fr_delta_2" : 205,
		"fr_dev" : "-122 Hz",
		"fr_rssi_rx" : -22,
		"fr_rssi_tx" : -27,
		"gsm_vol" : "4.154",
		"load_res" : "28.24 Ohm",
		"power_off_curr" : "-0.47mA",
		"s_central_id" : "80ab75",
		"s_mac" : [
			"38b8ebc0000e",
			"FFFFFFFFFFFF"
		],
		"stm_vol" : "3.27V"
	}
}

hub_long_info = {
	"app_name" : "HubLongTest4",
	"app_version" : "4.00.39"
}

hub_qc_info = {
	"app" : "New_QC 0.1.68",
	"description" : "Стандартний"
}
