def melon_delivery_report(day, order_file):
    the_file = open(order_file)
    print("Day {}".format(day))    
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
            
        print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
    the_file.close()

melon_delivery_report(1, "um-deliveries-20140519.txt")
melon_delivery_report(2, "um-deliveries-20140520.txt")
melon_delivery_report(3, "um-deliveries-20140521.txt")