import sys
def test():
	f = open('data.csv', 'r')
	d = f.readline()
	for k in range(30):
		a = f.readline()
		b = a.split(",")
		result = "{\"name\":\"" + b[0] + "\",\"region\":\""+b[1] + "\",\"gdp\":["
		counter = 2
		for k in range(1990,2016):
			temp = "[" + str(k) + "," + b[counter] + "],"
			counter = counter + 1
			result = result + temp;
		result = result[:-1] + "],\"co2\":["
		for k in range(1990,2016):
			temp = "[" + str(k) + "," + b[counter] + "],"
			counter = counter + 1
			result = result + temp;
		result = result[:-1] + "],\"forest\":["
		for k in range(1990,2016):
			temp = "[" + str(k) + "," + b[counter] + "],"
			counter = counter + 1
			result = result + temp;
		result = result[:-1] + "],\"highTech\":["
		for k in range(1990,2016):
			temp = "[" + str(k) + "," + b[counter] + "],"
			counter = counter + 1
			result = result + temp;
		result = result[:-1] + "],\"Population\":["
		for k in range(1990,2016):
			temp = "[" + str(k) + "," + b[counter] + "],"
			counter = counter + 1
			result = result + temp;   
		result = result[:-1] + "]},"
		print result

test()

