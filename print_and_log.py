class Logger:
    def __init__(self, output):
        self.output = output

    def print_and_log(self, value):
        print(value)
        print(value, file=self.output)

    def input_and_log(self):
        value = input()
        print(value, file=self.output)
        return value


# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# console_handler = logging.FileHandler("log")
# log_format = '%(message)s'
# console_handler.setFormatter(logging.Formatter(log_format))
# logger.addHandler(console_handler)
#
# message = "ksajfj;skadf"

