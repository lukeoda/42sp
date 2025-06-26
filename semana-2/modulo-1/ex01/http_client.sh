#! /bin/bash
chmod +x ./http_client.sh
curl -i -H "Authorization: token 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" https://api.github.com/users/torvalds -o jsonfile.json 


