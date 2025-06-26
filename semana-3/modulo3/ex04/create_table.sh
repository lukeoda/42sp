TABLE_NAME="Usuarios"

echo "Checando se a tabela '$TABLE_NAME' existe."
aws dynamodb describe-table --table-name "$TABLE_NAME" --no-cli-pager > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Tabela '$TABLE_NAME' encontrada. Deletando."
    aws dynamodb delete-table --table-name "$TABLE_NAME" --no-cli-pager

    echo "Aguardando a exclusão da tabela '$TABLE_NAME'."
    aws dynamodb wait table-not-exists --table-name "$TABLE_NAME" --no-cli-pager
    echo "Tabela '$TABLE_NAME' deletada com sucesso."
fi
echo 'Criando a tabela DynamoDB.' 
aws dynamodb create-table \
    --table-name Usuarios \
    --attribute-definitions \
        AttributeName=Id,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD \
    --no-cli-pager
echo 'Aguardando a tabela estar ativa.'

aws dynamodb wait table-exists \
    --table-name Usuarios --no-cli-pager

echo 'Tabela criada com sucesso.'
