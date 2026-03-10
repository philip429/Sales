import csv
import os

from clients.models import Client

class ClientService:
    def __init__(self,table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
    
    def list_client(self):
        with open(self.table_name, mode='r') as f:
            reader= csv.DictReader(f, fieldnames=Client.schema())
            print(reader)

            return list(reader)
    

    def update_client(self, update_client):
        clients = self.list_client()
        
        updated_clients = []
        for client in clients:
            if client ['uid'] == update_client.uid:
                updated_clients.append(update_client.to_dict())
            else:
                updated_clients.append(client)
        
        self._save_Disk(updated_clients)


    def delete_client(self,delete_client):
        clients = self.list_client()
        
        updated_clients = []
        for client in clients:
            if not client['uid'] == delete_client.uid:
                updated_clients.append(client)
            
        self._save_Disk(updated_clients)
        
    def _save_Disk(self,clients):
        tmp_table_name = self.table_name + '.tmp'
        
        with open(tmp_table_name, mode="w") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)
        
        os.remove(self.table_name)
        os.rename(tmp_table_name,self.table_name)

