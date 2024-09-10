import json
import boto3
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
Clientes_table = dynamodb.Table('Clientes')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        comprador_id = str(uuid.uuid4())
        nome = body.get('nome')
        email = body.get('email')
        cpf = body.get('cpf')

        if not all([nome, email, cpf]):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Nome, Email e CPF são obrigatórios'})
            }

        try:
            response = Clientes_table.get_item(Key={'cpf': cpf})
            if 'Item' in response:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Comprador já cadastrado'})
                }
        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'Erro ao verificar comprador: {e.response["Error"]["Message"]}'})
            }

        Clientes_table.put_item(
            Item={
                'id': comprador_id,
                'nome': nome,
                'email': email,
                'cpf': cpf
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Comprador cadastrado com sucesso', 'comprador_id': comprador_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Erro ao cadastrar comprador: {str(e)}'})
        }
