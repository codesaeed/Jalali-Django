'''
#    /** Programmer Saeed Jeddi
#       | websit : saeedjeddi.ir | email : saeedjeddimail@gmail.com **/
# --------------------------------------------------------------------------------------------
# instructions :
#    Introduce the app to the main settings
#   // INSTALLED_APPS = [
#                        #add extensions PersianJalali
#                        'extensions',
# ]
#--------------------------------------------------------------------------------------------
# Add the function to the desired module
#         from extensions.utils import django_PersianJalali_Converter
# Introduce the following code to the desired class in the app folder and the module file.
#     def PersianJalaliConverter(self):
#         return django_PersianJalali_Converter(self.publish)
#     PersianJalaliConverter.short_description = "  Publication time in Persian "
'''
#------------------------------------------------------------------------------------------
from . import PersianJalali
from django.utils import timezone
def persian_numbers_converter (STR):
    numbers = {"0":"۰","1":"۱","2":"۲","3":"۳","4":"۴","5":"۵","6":"۶","7":"۷","8":"۸","9":"۹",}
    for k , v in numbers.items():
        STR = STR.replace(k,v)
    return STR
def django_PersianJalali_Converter(time):
    Pj =['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = PersianJalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    for index, month in enumerate(Pj):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    output ='{} {} {} ، ساعت {}:{}'.format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )
    return persian_numbers_converter(output)
