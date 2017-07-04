import csv

class Util():
	
    @staticmethod
    def gen_csv(filename):
        with open(filename, "r") as csvfile:
            datareader = csv.DictReader(csvfile)
            for row in datareader:
                yield list(row.values())

    @staticmethod
    def run_gen_csv_with_state(csv):
        gen_csv = Util.gen_csv(csv)
        try:
            current_row = next(gen_csv)
        except StopIteration:
            return
        for next_row in gen_csv:
            prev_row, current_row = current_row, next_row
            yield prev_row, current_row