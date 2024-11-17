import tkinter as tk
from tkinter import ttk
import json
import operator

class FinanceTrackerGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")


    def create_widgets(self):
        # Frame for table and scrollbar
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # Treeview for displaying transactions
        self.tree = ttk.Treeview(self.frame, columns=("ID","Type", "Amount", "Date"),show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type",command=lambda: self.sort_by_column("Type", False))
        self.tree.heading("Amount", text="Amount",command=lambda: self.sort_by_column("Amount", False))
        self.tree.heading("Date", text="Date",command=lambda: self.sort_by_column("Date", False))
        self.tree.pack(fill="both", expand=True)

        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Search bar and button
        self.search_label = ttk.Label(self.root, text="Search date(YYYY-MM-DD):")
        self.search_label.pack(side="left", padx=5)
        self.search_entry = ttk.Entry(self.root, width=20)
        self.search_entry.pack(side="left", padx=5)
        self.search_button = ttk.Button(self.root, text="Search",command=self.search_transactions )
        self.search_button.pack(side="left", padx=5)

        
    def load_transactions(self, filename):
         try:
             with open(filename, "r") as file:
                 return json.load(file)
         except FileNotFoundError:
            return {}



    def display_transactions(self, transactions):
        # Remove existing entries
        # Add transactions to the treeview
        categories = []
        amounts = []
        dates = []

        for category, data1 in transactions.items():
            for data2 in data1:
                categories.append(category)
                amounts.append(data2['amount'])
                dates.append(data2['date'])

        index_list = [i+1 for i in range(len(categories))]

        
        for idx,value in enumerate(categories):
            self.tree.insert('',idx,values=(index_list[idx],categories[idx],amounts[idx],dates[idx]))


    def search_transactions(self):
         # Placeholder for search functionality
        search_date=self.search_entry.get()
        for item in self.tree.get_children():
            self.tree.delete(item)

        categories = []
        amounts = []
        dates = []



        for category, data1 in self.transactions.items():
            for data2 in data1:
                if data2["date"] == search_date:
                    categories.append(category)
                    amounts.append(data2["amount"])
                    dates.append(data2["date"])
        index_list = [i+1 for i in range(len(categories))]

        
        for idx,value in enumerate(categories):
            self.tree.insert('',idx,values=(index_list[idx],categories[idx],amounts[idx],dates[idx]))



    def sort_by_column(self, col, reverse=False):
        # Placeholder for sorting functionality
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        data.sort(reverse=reverse, key=operator.itemgetter(0))

        for index, item in enumerate(data):
            self.tree.move(item[1], '', index)

        self.tree.heading(col, command=lambda: self.sort_by_column(col, not reverse))    
    
def main():
    root=tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()
    

if __name__ == "__main__":
    main()
