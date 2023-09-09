""" export pops lines module """
import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from compensation.models import EmployeeCompensation



class Command(BaseCommand):
    """ Command class """
    help = 'Exports all Employee details from the file'

    def add_arguments(self, parser):
        parser.add_argument('--input_emp_details', type=str, required=True)
        
    
    @transaction.atomic
    def handle(self, *args, **options):
        """ handle method """
        filepath = options['input_emp_details']
        self.stdout.write("Reading the file {}".format(filepath))

        # header = [
        #     'Employee Identifier',
        #     'Salaries',
        #     'Other Salaries',
        #     'Total Salary',
        #     'Retirement',
        #     'Health and Dental',
        #     'Other Benefits',
        #     'Total Benefits',
        # 	'Total Compensation',
        # ]
        
        with open(filepath, 'r') as csvfile:
            input_file_reader = csv.DictReader(csvfile, delimiter=',')
            for row in input_file_reader:
                EmployeeCompensation.objects.create(
                    emp_identifier = row['Employee Identifier'],
                    salary = row['Salaries'],
                    other_salary = row['Other Salaries'],
                    total_salary = row['Total Salary'],
                    retirement = row['Retirement'],
                    health_dental = row['Health and Dental'],
                    other_benefits = row['Other Benefits'],
                    total_benefits = row['Total Benefits'],
                    total_compensation = row['Total Compensation'],
                )

        self.stdout.write('Exported emp details...')
