# Route Selection Decision Support System

A simple decision support tool for selecting a route under uncertainty, based on travel time and risk score.

## How it works

- Loads a list of routes with time and risk scores from `routes.csv`
- User inputs their maximum accepted risk score and maximum time
- The system suggests the first available route that fits the criteria

## How to use

1. Edit `routes.csv` to add or update routes and scores
2. Run the script:  
   ```
   python route_selector.py
   ```
3. Enter your preferences when prompted

---

## Example

```
Available routes:
1. A | Time: 20 mins | Risk: 0.2
2. B | Time: 15 mins | Risk: 0.4
3. C | Time: 25 mins | Risk: 0.1
4. D | Time: 30 mins | Risk: 0.3
5. E | Time: 10 mins | Risk: 0.7
6. F | Time: 18 mins | Risk: 0.5

Enter maximum risk score you accept (0-1): 0.3
Enter maximum travel time in minutes: 22

Recommended Route:
Route: A
Time: 20
Risk Score: 0.2
```

---

## UI Diagram

```
+------------------------------+
|  Route Selection System      |
+------------------------------+
|  Load routes.csv             |
|  Show list of routes         |
|  [User input]                |
|   - Max risk                 |
|   - Max time                 |
|  [Recommend route]           |
+------------------------------+
```
