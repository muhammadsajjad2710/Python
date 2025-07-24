import mysql.connector
from mysql.connector import Error
import PyPDF2
import re
import os
import mysql.connector
import pandas as pd
import glob

pdf_dir = r'D:\Interrnship\Statement 23-24\Statement 23-24\Sch issued Oct 23 will be paid Nov 23'
    
    # Get a list of all PDF files in the directory
pdf_files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    
    # Loop through each PDF file and process it
for pdf_path in pdf_files:

    def pdf_text_from_pdf(pdf_path):
        text_per_page = []
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_per_page.append(text)
        return text_per_page
    def extract_statement_references_from_text(pdf_text):
        statement_reference = None  # Initialize statement reference variable
        for text in pdf_text:
            if statement_reference is None:  # Check if statement reference is not assigned yet
                statement_reference_match = re.search(r'Statement\s*Reference\s*([\d/]+)', text)
                if statement_reference_match:
                    statement_reference = statement_reference_match.group(1)
                    break  # Break loop after finding the first statement reference
        return statement_reference
    def extract_text_from_pdf(pdf_path):
        text_per_page = []
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_per_page.append(text)
                # Check if the text "Contract Monthly Pay Statement" is in the extracted text
                if "Contract Monthly Pay Statement" in text:
                    break  # Stop extracting text from further pages
        return text_per_page


    def extract_performers_superannuation_table(pdf_text):
        # Define the start and end patterns for the table
        start_pattern = r'Performers\' Superannuation Contribution'
        end_pattern = r'Patients\' Charges'

        # Find the start and end positions of the table
        start_match = re.search(start_pattern, pdf_text)
        end_match = re.search(end_pattern, pdf_text)

        # If both start and end patterns are found, extract the table text
        if start_match and end_match:
            table_text = pdf_text[start_match.end():end_match.start()].strip()
            return table_text
        else:
            return None
    def extract_rows_from_text(text):
        # Define a more flexible pattern to capture rows
        pattern = r'(\d+)\s+([A-Za-z\s]+)@?\s+([\d.]+)%\s*(-?£[\d.,]+)'
        #rows = re.findall(r'(\d+)\s+([A-Za-z\s]+)@?\s+([\d.]+)%\s+£([\d.]+)', cleaned_table_text)

        # Find all matches in the text
        matches = re.findall(pattern, cleaned_text)

        # Return a list of matched rows
        return matches

    def format_table(rows, Contract_ID, statement_reference):
        formatted_rows = []
        for row in rows:
                   # Extract the numeric part of the amount string and convert to float
            amount_str = re.sub(r'[^.\d]', '', row[3])  # Remove all non-numeric characters except '.'
            amount = float(amount_str)  # Convert to float

            formatted_row = {
                "contract_id": Contract_ID,
                "statement_reference": statement_reference,
                "performer_id": row[0],
                "name": row[1].strip(),
                "percentage": row[2],
                "amount": amount
            }
            formatted_rows.append(formatted_row)
        return formatted_rows
    def extract_performers_non_superannuable_deductions(pdf_text):
        # Define the start and end patterns for the table
        start_pattern = r'Non-Superannuable Deductions\s*Statutory Levy'
        end_pattern = r'(?:Performers\' Net Pensionable Earnings|$)'  # End pattern is either end of table or next section

        # Find the start and end positions of the table
        start_match = re.search(start_pattern, pdf_text)
        end_match = re.search(end_pattern, pdf_text)

        # If both start and end patterns are found, extract the table text
        if start_match and end_match:
            table_text = pdf_text[start_match.end():end_match.start()]
            return table_text.strip()
        else:
            return None

    def format_table_non_superannuable_deductions(table_text, Contract_ID, statement_reference):
        # Extracting rows using regular expression
        rows = re.findall(r'(\d+)\s+([A-Za-z\s]+)\s+£([\d.]+)', table_text)


        # Formatting the rows into desired format
        formatted_rows = []
        for row in rows:
            formatted_row = {
                "Contract_ID": Contract_ID,
                "Statement_Reference": statement_reference,
                "Performer_ID": row[0],
                "Performer_Name": row[1],
                "Amount": row[2]


            }
            formatted_rows.append(formatted_row)

        return formatted_rows

    def extract_units_of_dental_activity(text_per_page):
        start_pattern = "Units of Dental Activity per Performer"
        #start_pattern = "Units of Dental Activity per Clinician"
        end_pattern = "THIS STATEMENT SHOULD BE RETAINED FOR TAX PURPOSES"

        relevant_text = ""
        for page_text in text_per_page:
            start_index = page_text.find(start_pattern)
            if start_index != -1:
                end_index = page_text.find(end_pattern, start_index)
                if end_index != -1:
                    relevant_text += page_text[start_index:end_index]
                else:
                    relevant_text += page_text[start_index:]
        return relevant_text

    def parse_performers(text):
        performer_data = re.findall(r'\b(\d+)\s+([A-Za-z\s]+)\s+Current', text)
        performer_ids, performer_names = zip(*performer_data)
        return performer_ids, performer_names

    def extract_current_financial_year_rows(text, pattern, year_col_name, amount_col_name):
        current_year_rows = []
        lines = text.strip().split('\n')
        for line in lines:
            match = re.search(pattern, line)
            if match:
                year = match.group(1) if match.group(1) else '0'  # If year is missing, consider it as '0'
                current_year_rows.append({year_col_name: year, amount_col_name: match.group(2)})
        return current_year_rows


    if __name__ == "__main__":
        # Extract the table text
        pdf_text = pdf_text_from_pdf(pdf_path)
        complete_pdf_text = "\n".join(pdf_text)
        performers_superannuation_table_text = extract_performers_superannuation_table(complete_pdf_text)
        cleaned_table_text = re.sub(r'\(\d+\)', '', performers_superannuation_table_text)
        pattern = r"Performers' Added Benefit.*$"

        # Use regex to substitute the matched pattern with an empty string
        cleaned_text = re.sub(pattern, '', cleaned_table_text, flags=re.DOTALL)

        # Trim any leading or trailing whitespace
        cleaned_text = cleaned_text.strip()





        pdf_text = pdf_text_from_pdf(pdf_path)
        statement_reference = extract_statement_references_from_text(pdf_text)

        if statement_reference:
            print("Extracted Statement Reference:", statement_reference)
        else:
            print("No Statement Reference found in the PDF.")

        extracted_text = extract_text_from_pdf(pdf_path)
        found_text = False  # Flag to check if the desired text is found
        contract_monthly_pay_statement_text = ""  # Initialize empty string to store the desired text
        for page_num, text in enumerate(extracted_text, start=1):
            if found_text:
                contract_monthly_pay_statement_text += text.strip() + "\n---\n"  # Append the text to the output
            elif "Contract Monthly Pay Statement" in text:
                found_text = True  # Set the flag to True when the desired text is found
                contract_monthly_pay_statement_text += text.strip() + "\n---\n"  # Append the text to the output

        extracted_text = extract_text_from_pdf(pdf_path)
        found_start = False
        contract = ""  # Initialize empty string to store the desired text
        for page_num, text in enumerate(extracted_text, start=1):
            if found_start:
                if "CONTRACT" in text:
                    break
                contract += text.strip() + "\n"
            elif "CONTRACT" in text:
                found_start = True
                # Find the index of the start of "Contract Monthly Pay Statement" and "CONTRACT"
                start_index = text.find("CONTRACT") + len("CONTRACT")
                end_index = text.find("If ")
                # Append the text between these indices
                contract += text[start_index:end_index].strip() + "\n"

        # Splitting the contract string into Contract_ID and Contract_Name
        contract_lines = contract.split("\n", 1)  # Splitting into two parts at the first newline

        # Assuming the first part is Contract_ID and the second part is Contract_Name
        contract_id = contract_lines[0].strip()
        Contract_Name = contract_lines[1].strip()
        Contract_ID = ''.join(filter(str.isdigit, contract_id))
        print("Contract_ID:", Contract_ID)
        # Extract rows using the updated pattern
        rows = extract_rows_from_text(cleaned_text)


        # Format the extracted rows into DataFrame
        formatted_table = format_table(rows, Contract_ID, statement_reference)
        df2 = pd.DataFrame(formatted_table)
        # Convert data types
        df2['contract_id'] = df2['contract_id'].astype(str)
        df2['statement_reference'] = df2['statement_reference'].astype(str)
        df2['performer_id'] = df2['performer_id'].astype(str)
        df2['name'] = df2['name'].astype(str)
        df2['percentage'] = df2['percentage'].astype(float)
        df2['amount'] = df2['amount'].astype(float)
        # Display the DataFrame

        print("Performers' Superannution Deductions Statutory Levy Table:")
        print(df2)

        performers_non_superannuation_table_text = extract_performers_non_superannuable_deductions(complete_pdf_text)

        # Print the extracted table text
        if performers_non_superannuation_table_text:
            print("Performers' Non-Superannuable Deductions Statutory Levy Table:")
            #print(performers_non_superannuation_table_text)

            # Format the table text
            formatted_table = format_table_non_superannuable_deductions(performers_non_superannuation_table_text, Contract_ID, statement_reference)

            # Convert the formatted table to DataFrame
            df = pd.DataFrame(formatted_table)

            # Print DataFrame
            #print(df)


    # Create a boolean mask to identify rows where 'Performer_Name' is either 'Contract' or 'Superannuable'
            mask = ~df['Performer_Name'].isin(['Contract', 'Superannuable'])

    # Apply the mask to filter out rows that do not match the conditions
            df3 = df[mask]

    # df_filtered now contains only the rows where 'Performer_Name' is neither 'Contract' nor 'Superannuable'
            df3['Amount'] = df3['Amount'].astype(float)

            print(df3)
        else:
            print("Performers' Non-Superannuable Deductions Statutory Levy Table not found in the PDF text.")

        relevant_text = extract_units_of_dental_activity(pdf_text)

        # Parse performer data
        performer_ids, performer_names = parse_performers(relevant_text)

        # Create performer DataFrame
        df_performers = pd.DataFrame({'Contract_ID': Contract_ID,'Statement_Reference':statement_reference,'Performer_ID': performer_ids, 'Name': performer_names})

        # Extract financial year rows
        current_year_rows = extract_current_financial_year_rows(relevant_text, 
                                                                r'Current Financial Year (\d{4}/\d{2})\s+([\d.]+)',
                                                                'Current_Financial_Year', 
                                                                'Current_Financial_Year_Amount')

        last_year_rows = extract_current_financial_year_rows(relevant_text, 
                                                                r'Last Financial Year (\d{4}/\d{2})\s+([\d.]+)',
                                                                'Last_Financial_Year', 
                                                                'Last_Financial_Year_Amount')

        other_year_rows = extract_current_financial_year_rows(relevant_text, 
                                                                r'Other Financial Years(?: (\d{4}/\d{2}))?\s+([\d.]+)',
                                                                'Other_Financial_Years', 
                                                                'Other_Financial_Year_Amount')

        # Create financial year DataFrames
        df_current = pd.DataFrame(current_year_rows)
        df_last = pd.DataFrame(last_year_rows)
        df_other = pd.DataFrame(other_year_rows)

        # Concatenate financial year DataFrames
        df_financial_years = pd.concat([df_current, df_last, df_other], axis=1)

        # Print combined DataFrame
        combined_df = pd.concat([df_performers, df_financial_years], axis=1)
        df4 =combined_df 


        df4['Current_Financial_Year_Amount'] = df4['Current_Financial_Year_Amount'].astype(float)
        df4['Last_Financial_Year_Amount'] = df4['Last_Financial_Year_Amount'].astype(float)
        df4['Other_Financial_Year_Amount'] = df4['Other_Financial_Year_Amount'].astype(float)
        df4.rename(columns={'Other_Financial_Year_Amount': 'Other_Finacial_Year_Amount'}, inplace=True)
        print("Performers' Units of Dental Activity Table:")
        print(df4)


        host = 'localhost'
        user = 'root'
        password = ''
        database = 'new'


        # Establish connection to MySQL
        try:
            conn = mysql.connector.connect(
                user=user,

                password=password,
                host=host,
                database=database
            )
            print("Connected to MySQL database:", conn.database)
        except mysql.connector.Error as err:
            print("Error connecting to MySQL:", err)

        # Prepare SQL insert statement
        insert_statement = """
        INSERT INTO dashboard_units_details
        (Contract_ID, Statement_Reference, Performer_ID, Name, Current_Financial_Year, 
        Current_Financial_Year_Amount, Last_Financial_Year, Last_Financial_Year_Amount, 
        Other_Finacial_Years, Other_Finacial_Year_Amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            with conn.cursor() as cursor:
            # Iterate over DataFrame rows
                for index, row in df4.iterrows():
                # Extract values from DataFrame row and perform necessary conversions
                    values = (
                        row['Contract_ID'],
                        row['Statement_Reference'],
                        row['Performer_ID'],
                        row['Name'],
                        row['Current_Financial_Year'],
                        float(row['Current_Financial_Year_Amount']),  # Convert to float
                        row['Last_Financial_Year'],
                        float(row['Last_Financial_Year_Amount']),  # Convert to float
                        row['Other_Financial_Years'],
                        float(row['Other_Finacial_Year_Amount'])  # Convert to float
                    )

                # Execute SQL insert statement
                    cursor.execute(insert_statement, values)

        # Commit changes to the database
            conn.commit()
            print("Data Performers' Units of Dental Activity Table inserted successfully into MySQL table")

        except Exception as e:
            print(f"Error occurred: {e}")

        df4 = df4.iloc[0:0]
        insert_statement = """
        INSERT INTO dashboard_superannuationdetails
        (contract_id, statement_reference, name, percentage, amount, performer_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            with conn.cursor() as cursor:
            # Iterate over DataFrame rows
                for index, row in df2.iterrows():
                # Extract values from DataFrame row and perform necessary conversions
                    values = (
                        row['contract_id'],
                        row['statement_reference'],
                        row['name'],
                        row['percentage'],  
                        row['amount'],
                        row['performer_id']
                    )

                # Execute SQL insert statement
                    cursor.execute(insert_statement, values)

        # Commit changes to the database
            conn.commit()
            print("Data of Performers' Superannution Deductions Statutory Levy Table inserted successfully into MySQL table")

        except Exception as e:
            print(f"Error occurred: {e}")
        df2 = df2.iloc[0:0]
        insert_statement = """
        INSERT INTO dashboard_nonsuperannuable
        (Contract_ID, Statement_Reference, Performer_ID, Performer_Name, Amount)
        VALUES (%s, %s, %s, %s, %s)
        """

        try:
            with conn.cursor() as cursor:
            # Iterate over DataFrame rows
                for index, row in df3.iterrows():
                # Extract values from DataFrame row and perform necessary conversions
                    values = (
                        row['Contract_ID'],
                        row['Statement_Reference'],
                        row['Performer_ID'],
                        row['Performer_Name'],
                        float(row['Amount']) if pd.notnull(row['Amount']) else None  # Convert to float (handle NaN)
                    )

                # Execute SQL insert statement
                    cursor.execute(insert_statement, values)

        # Commit changes to the database
            conn.commit()
            print("Data Of Performers' Non-Superannuable Deductions Statutory Levy Table inserted successfully into MySQL table")

        except Exception as e:
            print(f"Error occurred: {e}")

        #df3 = df3.iloc[0:0]
