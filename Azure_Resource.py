# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import ResourceManagementClient
#
# import os
#
# # Set environment variables
# os.environ["AZURE_CLIENT_ID"] = "7eb1caa7-924d-4d20-aad8-c3dc26bb7132"
# os.environ["AZURE_CLIENT_SECRET"] = "4zD8Q~~Wd~FqRxkqmQ4m4s5BVBIhg0oW48pcWaZX"
# os.environ["AZURE_TENANT_ID"] = "65582760-3ca3-49d9-91d7-f2fd6402bb4e"
#
# # Initialize Azure Resource Management Client
# credential = DefaultAzureCredential()
# subscription_id = "3b65aa4a-6333-4cf8-9b7d-b41e3df810cb"
# resource_client = ResourceManagementClient(credential, subscription_id)
#
# # Get a list of resource groups
# resource_groups = resource_client.resource_groups.list()
#
# # Iterate through each resource group
# for resource_group in resource_groups:
#     print(f"Resource Group: {resource_group.name}")
#
#     # List resources in the resource group
#     resources = resource_client.resources.list_by_resource_group(resource_group.name)
#
#     # Filter and print resource names ending with "dev"
#     for resource in resources:
#         if resource.name.lower().endswith("jg"):
#             print(f"   - {resource.name} ({resource.type})")


# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["3b65aa4a-6333-4cf8-9b7d-b41e3df810cb"]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Retrieve the list of resource groups
group_list = resource_client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in list(group_list):
    print(f"{group.name:<{column_width}}{group.location}")