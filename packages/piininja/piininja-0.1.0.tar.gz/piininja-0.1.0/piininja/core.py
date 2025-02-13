import pandas as pd
import numpy as np
import re
from .techniques import (
    mask_email,
    mask_phone,
    generalize_age,
    tokenize_names,
    add_noise_to_numeric
)

class DataAnonymizer:
    def __init__(self, file_path):
        """
        Initialize the DataAnonymizer with a file path
        Supports Excel, CSV, and other pandas-readable formats
        """
        try:
            self.original_df = pd.read_excel(file_path)
            self.anonymized_df = self.original_df.copy()
        except Exception as e:
            raise ValueError(f"Error loading file: {e}")
    
    def anonymize_column(self, column, technique='default'):
        """
        Anonymize a specific column using different techniques
        
        Techniques:
        - 'email': Mask email addresses
        - 'phone': Mask phone numbers
        - 'name': Tokenize names
        - 'age': Generalize age groups
        - 'numeric': Add noise to numeric columns
        """
        techniques_map = {
            'email': mask_email,
            'phone': mask_phone,
            'age': generalize_age,
            'name': tokenize_names,
            'numeric': add_noise_to_numeric
        }
        
        if technique not in techniques_map:
            raise ValueError(f"Unsupported technique: {technique}")
        
        # Apply the selected technique
        self.anonymized_df[column] = self.anonymized_df[column].apply(
            techniques_map[technique]
        )
        
        return self
    
    def auto_anonymize(self):
        """
        Automatically detect and anonymize sensitive columns
        """
        # Email detection
        email_columns = self.anonymized_df.columns[
            self.anonymized_df.columns.str.contains('email', case=False)
        ]
        for col in email_columns:
            self.anonymize_column(col, 'email')
        
        # Phone number detection
        phone_columns = self.anonymized_df.columns[
            self.anonymized_df.columns.str.contains('phone', case=False)
        ]
        for col in phone_columns:
            self.anonymize_column(col, 'phone')
        
        # Age/Date columns
        age_columns = self.anonymized_df.columns[
            self.anonymized_df.columns.str.contains('age|birth', case=False)
        ]
        for col in age_columns:
            self.anonymize_column(col, 'age')
        
        # Numeric columns
        numeric_columns = self.anonymized_df.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            self.anonymize_column(col, 'numeric')
        
        return self
    
    def save(self, output_path=None):
        """
        Save the anonymized dataframe
        If no path provided, saves with '_anonymized' suffix
        """
        if output_path is None:
            base_path = re.sub(r'\.[^.]+$', '', output_path)
            output_path = f"{base_path}_anonymized.xlsx"
        
        self.anonymized_df.to_excel(output_path, index=False)
        print(f"Anonymized data saved to {output_path}")
        return self.anonymized_df