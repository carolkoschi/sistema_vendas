# Baixa a chave GPG da Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
rm microsoft.gpg


# Adiciona manualmente o repositório para Ubuntu 22.04 (jammy), mesmo no Ubuntu 24.04
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Atualiza os pacotes
sudo apt-get update

# Instala o driver ODBC 17 e dependências
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev
