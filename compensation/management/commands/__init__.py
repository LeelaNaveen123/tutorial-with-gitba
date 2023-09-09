""" export pops lines module """
import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone



class Command(BaseCommand):
    """ Command class """
    help = 'Exports all Employee details from the file'

    def add_arguments(self, parser):
        parser.add_argument('--input_petid_spreadsheet', type=str, required=True)
        
    
    @transaction.atomic
    def handle(self, *args, **options):
        """ handle method """
        filepath = options['input_petid_spreadsheet']
        self.stdout.write("Reading the file {}".format(filepath))

        header = [
            'Employee Identifier',
            'Salaries',
            'Other Salaries',
            'Total Salary',
            'Retirement',
            'Health and Dental',
            'Other Benefits',
            'Total Benefits',
        	'Total Compensation',
        ]
        
        with open(filepath, 'r') as csvfile:
            input_file_reader = csv.DictReader(csvfile, delimiter='\t')
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()

            for count, order_line in enumerate(
                self._vet_diet_lines(options['select_year'], options['select_month']),
                start=1,
            ):
                writer.writerow(self._vet_diet_line_to_dict(order_line))
                if count % 500 == 0:
                    self.stdout.write(f'Status: written {count} order lines.')

        self.stdout.write('Finished Vet Diet POPS lines export.')
