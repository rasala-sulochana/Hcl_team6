import logging
logging.basicConfig(filename="mylogdetails.txt",level=logging.INFO)
logging.info("A new log came")
try:
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    print(n1/n2)
except Exception as e:
    print("cann't divide with zero")
    logging.exception(e)
except ValueError as msg:
    print("value only")
    logging.exception(msg)
logging.info("Log is recorded")

