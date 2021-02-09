# -*- coding: utf-8 -*-
from lib import schedule_parser


# def ...

if __name__ == "__main__":
	keywords = ("DATES", "COMPDAT", "COMPDATL")
	parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
					"Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
					"Skin factor", "D-factor")
	input_file = "input_data/test_schedule.inc"
	output_csv = "output_data/schedule.csv"

	schedule_df = schedule_parser.transform_schedule(keywords, parameters, input_file, output_csv)
