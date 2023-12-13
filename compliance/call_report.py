# complycat/call_report.py

class FilingInstitution:
    def __init__(self, name, domestic_only, total_assets, has_foreign_office, is_advanced_approaches):
        # Initialize the FilingInstitution object with relevant attributes
        self.name = name  # Name of the institution
        self.domestic_only = domestic_only  # Whether the institution has only domestic offices
        self.total_assets = total_assets  # Total assets of the institution
        self.has_foreign_office = has_foreign_office  # Whether the institution has a foreign office
        self.is_advanced_approaches = is_advanced_approaches  # Whether the institution follows advanced approaches

class CallReportFiler:
    def __init__(self, filing_institution):
        # Initialize the CallReportFiler with the FilingInstitution it relates to
        self.filing_institution = filing_institution

    def determine_call_report_form(self):
        # Determine the appropriate Call Report form based on the characteristics of the filing institution
        if self.filing_institution.has_foreign_office or self.filing_institution.is_advanced_approaches:
            return "FFIEC 031"
        elif self.filing_institution.domestic_only:
            if self.filing_institution.total_assets >= 100_000_000:
                return "FFIEC 031"
            elif 5_000_000 <= self.filing_institution.total_assets < 100_000_000:
                return "FFIEC 041"
            elif self.filing_institution.total_assets < 5_000_000:
                return "FFIEC 051"
        return None  # Return None if no matching form is found
