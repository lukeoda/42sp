#! /bin/bash
chmod +x ./http_server.sh
cd rotas
python3 -m http.server
