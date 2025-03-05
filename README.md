# meredian-csv-to-denaro
This Python script serves as a tool for tracking financial transactions, allowing users to record income and expenses with detailed information. The script supports both manual entry and importing transactions from a CSV file.

## Groups Definition

The financial transactions are categorized into five groups, each with its own percentage allocation:

1. **School Savings (50%):** Money saved for education.
2. **Savings (20%):** Money saved for large purchases.
3. **Free Spend (20%):** Money that can be freely spent.
4. **Insurance (10%):** Money set aside for insurance.

## CSV File Format

### Groups Information

```csv
GROUPID;GROUPNAME;GROUPDESCRIPTION
1, 5;School Savings;Money saved for education (20%)
2, 2;Savings;Money that is saved for large purchases (15%)
3, 1;Free Spend;Money that I can freely spend (40%)
4, 3;Tithe;Money to donate (10%)
5, 4;Insurance;Money set aside for insurance (15%)
```

### Transaction Information

```csv
ID;M/D/YYYY;Name;Type;RepeatInterval;RepeatFrom;RepeatEndDate;Amount;RGBA;UseGroupColor;GroupID;GroupName;GroupDescription;GroupRGBA;Tags
```

## Python Code Usage

1. **Run the Script:**
   - Execute the Python script by entering the file name when prompted.

2. **Choose Option:**
   - Select an option:
     - Option 1: Start from scratch and manually enter transaction details.
     - Option 2: Use a premade input line from an official Meredian website CSV exported file.

3. **Transaction Entry:**
   - Provide details such as the transaction date, name, type (income/expense), amount, and select the appropriate group.

4. **Success Message:**
   - Upon successful entry, a confirmation message will be displayed.

## Note

- The script automatically calculates the transaction ID based on the last recorded transaction.
- Date format should be provided as Month/Day/Year (M/D/YYYY).
- Group information is predefined and corresponds to the five groups mentioned above.

Feel free to contribute to and customize this script based on your specific needs.
