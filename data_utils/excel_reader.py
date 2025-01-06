# data_utils/excel_reader.py
"""
Module to read data from an Excel file.
"""

import logging
import openpyxl

# Set up logging
logger = logging.getLogger(__name__)

def read_data_from_excel(file_path, sheet_name):
    """
    Reads data from an Excel file.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to read data from.

    Returns:
        list: List of tuples containing data read from the Excel file.
    """
    logger.info(f"Reading data from Excel file: '{file_path}', sheet: '{sheet_name}'")
    
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    
    data = []
    is_first_row = True
    row_count = 0
    
    for row in sheet.iter_rows(values_only=True):
        row_count += 1
        logger.debug(f"Processing row {row_count}: {row}")
        
        # Skip header row
        if is_first_row:
            logger.info(f"Header row: {row}")
            is_first_row = False
            continue
        
        # Skip empty rows
        if not row or not any(row):
            logger.debug(f"Skipping empty row {row_count}")
            continue
            
        try:
            # Handle cases where row might have fewer columns
            row_data = list(row) + [''] * (4 - len(row)) if len(row) < 4 else row
            
            first_name = str(row_data[0] or '').strip()
            last_name = str(row_data[1] or '').strip()
            email = str(row_data[2] or '').strip()
            company_name = str(row_data[3] or '').strip()
            
            logger.debug(f"Processed data: {first_name=}, {last_name=}, {email=}, {company_name=}")
            
            # Basic validation
            if first_name and company_name:  # Minimum required fields
                data.append((first_name, last_name, email, company_name))  # Removed default designation
                logger.info(f"Added row {row_count}: {first_name} {last_name} at {company_name}")
            else:
                logger.warning(f"Row {row_count} missing required fields: {row}")
                
        except Exception as e:
            logger.error(f"Error processing row {row_count}: {e}")
            continue
    
    logger.info(f"Found {len(data)} valid rows out of {row_count-1} total rows (excluding header)")
    return data
