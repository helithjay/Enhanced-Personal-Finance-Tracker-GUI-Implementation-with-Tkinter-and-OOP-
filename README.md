# Personal Finance Tracker

## Overview
Personal Finance Tracker is a simple GUI application built using Python and Tkinter. It helps users track their financial transactions, search by date, and sort transactions based on different criteria.

## Features
- Displays financial transactions in a table format.
- Allows searching for transactions by date.
- Sorts transactions by type, amount, and date.
- Reads transaction data from a JSON file.

## Technologies Used
- Python
- Tkinter (for GUI)
- JSON (for data storage)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/helithjay/Enhanced-Personal-Finance-Tracker-GUI-Implementation-with-Tkinter-and-OOP-.git
   ```
2. Navigate to the project directory:
   ```sh
   cd finance-tracker
   ```
3. Install required dependencies (if needed):
   ```sh
   pip install tk
   ```

## Usage
1. Run the Python script:
   ```sh
   python code.py
   ```
2. The GUI will open, displaying the transaction data.
3. Use the search bar to filter transactions by date.
4. Click on column headers to sort transactions accordingly.

## File Structure
```
finance-tracker/
│-- code.py            # Main application script
│-- transactions.json  # JSON file containing transaction data
│-- README.md          # Project documentation
```

## Sample Data
The application loads transaction data from `transactions.json`:
```json
{
  "Groceries": [
    {"amount": 150, "date": "2024-02-03"},
    {"amount": 75, "date": "2024-02-15"}
  ],
  "Salary": [
    {"amount": 1000, "date": "2024-02-01"}
  ]
}
```

## Contributions
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

