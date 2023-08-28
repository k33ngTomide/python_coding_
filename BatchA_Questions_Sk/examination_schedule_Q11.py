import datetime

exam_st_date = "11,12,2014"
exam_date = exam_st_date.replace(",", "/")

print(f"The examination will start from: {exam_date}")


# exam_date = input("Enter the date of exam (yyyy-mm-dd): ")
# today_date = datetime.date.today()
#
# calc_date = today_date - exam_date
# print(today_date)