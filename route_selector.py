import csv

routes = []
with open("routes.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        routes.append(row)

print("Available routes:")
for i, r in enumerate(routes):
    print(str(i+1) + ". " + r['RouteName'] + " | Time: " + r['TimeMin'] + " mins | Risk: " + r['RiskScore'])

try:
    max_risk = float(input("Enter maximum risk score you accept (0-1): "))
    max_time = float(input("Enter maximum travel time in minutes: "))
except:
    print("Invalid input.")
    exit()

found = False
for route in routes:
    if float(route['RiskScore']) <= max_risk and float(route['TimeMin']) <= max_time:
        print("Recommended Route: " + route['RouteName'])
        print("Time: " + route['TimeMin'])
        print("Risk Score: " + route['RiskScore'])
        found = True
        break

if not found:
    print("No route found matching your criteria.")
