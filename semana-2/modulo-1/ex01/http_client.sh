#! /bin/bash
chmod +x ./http_client.sh
curl -i -H "Authorization: token " https://api.github.com/users/torvalds -o jsonfile.json 


