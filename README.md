# package Jalali-Django
Jalali Calendar for Django 

## instructions :
###  Introduce the app to the main settings
    INSTALLED_APPS = [
                       #add extensions PersianJalali
                       'extensions',
                     ]
                     
### Add the function to the desired module :
 `from extensions.utils import django_PersianJalali_Converter`
 
 Introduce the following code to the desired class in the app folder and the module file.
 
      def Jalali(self):
             return django_PersianJalali_Converter(self.datePush)
             Jalali.short_description = "  زمان انتشار "
---

- And you can call the function in the admin file section
