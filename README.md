#General design points 
#Kept modular - allows us to come back and re-write/add to easily, and allows same lines to be re-used multiple times. 
#Try-catches are employed, and feature descriptive error messages - these should allow users to pinpoint where errors are coming from.

#Description

#First analysed the task and broke down the process into the key steps. #In this case, I determined that this process can be broken down into 3 distinct parts - import file, parser and the converter.

#Import file is most straight forward - provide users opportunity to enter file directory and location.

#Parser - searches for defined patterns in text. Pattern can be easily re-defined if we wanted to include numbers such as #658, £100, -100 or 100.05 for example.

#converter - consists of a top level number_converter into which a parsed list of strings is passed #Code then loops through this, applying the integer_converter to each list element.

#With integers, it can be seen that number naming convention is centred around what's between thousands separator combined with word for the appropriate power of 1000 #e.g. 1534701 = 'one million' 'five hundred and thirty-four thousand' 'seven hundred and one' #Situation can be solved through recursion - build a converter that easily handles up to three digits, and break down number into its thousands separator.

#numbers up to 999 are converted by the hundreds_handler - this references dictionaries and allow us to convert the numbers into their word forms. #dictionaries are made relatively compact - unnecessary to have a much longer dictionaries! #Thus, break down the number strings into three digit parts and convert them, and add on appropriate power_1000.

#commas and ands generally follows a set pattern, allowing us to easily code this in. #only exception is in the case when there is no hundreds value but last two digits are non zero. #e.g. "one thousand, one hundred and two" is correct, but "one thousand, and two" is incorrect. #Add a cleaning function which removes this comma when appropriate, as well as double spaces caused in this scenario.

#alongside the integer_converter we can place additional extra functions features under number_converter #these could handle decimal places, or currencies/minus signs.

#If wish to convert into different languages, only aspect of code that would need change would be in the converter section as well as new dictionaries.
