email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]  
# This Extracts the username from an email address (the part before @).email.index("@") finds the position of the @ symbol, and email[:...] slices the string from the start to that position (exclusive).
domain_name = email[email.index("@")+1:]
# This Extracts the domain name (the part after @). email.index("@") + 1 moves the index to the first character after @, and email[...] slices the string from that point to the end.

format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)