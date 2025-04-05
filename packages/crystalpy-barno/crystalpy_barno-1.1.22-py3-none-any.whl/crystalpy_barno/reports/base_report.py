from CrystalDecisions.CrystalReports.Engine import ReportDocument
from crystalpy_barno.config.database_config import DatabaseConfig
from crystalpy_barno.helpers.database_helper import DatabaseHelper
from crystalpy_barno.helpers.report_parameter_helper import ReportParameterHelper

import logging

logging.basicConfig(filename="report_errors.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


class BaseReport:
    def __init__(self, filename, output_path):
        self.report = ReportDocument()
        self.report.Load(filename)
        self.output_path = output_path

    def set_parameters(self, parameters):
        for name, value in parameters.items():
            ReportParameterHelper.set_parameter(self.report, name, value)

    def set_formula_fields(self, formulas):
        for name, value in formulas.items():
            ReportParameterHelper.set_formula_field(self.report, name, value)

    def apply_database_connection(self):
        DatabaseHelper.apply_connection(self.report)

    def set_stored_procedure(self, stored_procedure_name):
        """
        Set the stored procedure for the report.
        :param stored_procedure_name: The name of the stored procedure.
        """
        try:
            database_name = DatabaseConfig.get_database_name()
            if database_name:
                sp_location = f"{database_name}.dbo.{stored_procedure_name}"
                logging.info(f"Stored procedure set to: {sp_location}")
                self.report.Database.Tables[0].Location = sp_location
                
            else:
                logging.error(f"Database name not set. Ensure the connection is properly configured.")
                raise ValueError("Database name not set. Ensure the connection is properly configured.")
        except Exception as e:
            logging.error(f"Error setting stored procedure: {e}")
            raise

    def export(self, format_type):
        self.report.ExportToDisk(format_type, self.output_path)
