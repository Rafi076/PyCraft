#IN python we can raise custom error by using the raise keyword
# #
a = int(input("Enter any value between 5 to 9 includes or type 'quits': "))
    
if (a<5 or a>9 or a=="quits"):
    raise ValueError("Error!! Value should be between 5 to 9 or 'quits'.")


    # ValueError: Error!! Value should be between 5 to 9.
    #### To get to know more error search python error on webdite!!####
    
    
    