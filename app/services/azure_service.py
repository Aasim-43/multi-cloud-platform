from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

from app.config import *

def get_resource_groups():

    credential = ClientSecretCredential(
        tenant_id=AZURE_TENANT_ID,
        client_id=AZURE_CLIENT_ID,
        client_secret=AZURE_CLIENT_SECRET
    )

    client = ResourceManagementClient(
        credential,
        AZURE_SUBSCRIPTION_ID
    )

    groups = []

    for group in client.resource_groups.list():
        groups.append(group.name)

    return groups