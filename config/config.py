from datetime import datetime
from os import getcwd

timestamp = datetime.today()
prowler_version = "3.0-alfa"

# Groups
groups_file = "groups.json"

# AWS services-regions matrix json
aws_services_json_file = "providers/aws/aws_regions_by_service.json"

default_output_directory = getcwd() + "/output"

csv_file_suffix = timestamp.strftime("%Y%m%d%H%M%S") + ".csv"
json_file_suffix = timestamp.strftime("%Y%m%d%H%M%S") + ".json"
json_asff_file_suffix = timestamp.strftime("%Y%m%d%H%M%S") + "asff.json"
