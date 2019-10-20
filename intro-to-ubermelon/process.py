# Creates variable called log_file containing open a text file function.
log_file = open("um-server-01.txt")

# Creates sales_reports function
def sales_reports(log_file):
    # iterates through lines in log_file
    for line in log_file:
        # removes white space from line
        line = line.rstrip()
        # Creates variable day, equal to position 0 to 3 in line.
        day = line[0:3]
        # Conditional statement. If day in line is Monday, prints line.
        if day == "Mon":
            print(line)

# Runs sales_reports function on um-server-01.txt
sales_reports(log_file)
