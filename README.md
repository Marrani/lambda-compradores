# lambda-compradores

Este projeto contém o código-fonte e arquivos de suporte para uma aplicação serverless que você pode implantar com o SAM CLI. Inclui os seguintes arquivos e pastas:

- `clientes/` - Código para a função Lambda de cadastro de clientes.
- `events/` - Eventos de invocação que você pode usar para invocar a função.
- `tests/` - Testes unitários para o código da aplicação.
- `template.yaml` - Um template que define os recursos AWS da aplicação.

A aplicação utiliza vários recursos AWS, incluindo funções Lambda e uma API Gateway. Esses recursos estão definidos no arquivo `template.yaml` neste projeto. Você pode atualizar o template para adicionar recursos AWS através do mesmo processo de implantação que atualiza o código da sua aplicação.

Se você preferir usar um ambiente de desenvolvimento integrado (IDE) para construir e testar sua aplicação, pode utilizar o AWS Toolkit. O AWS Toolkit é um plug-in de código aberto para IDEs populares que utiliza o SAM CLI para construir e implantar aplicações serverless na AWS. O AWS Toolkit também adiciona uma experiência simplificada de depuração passo a passo para o código da função Lambda. Veja os links a seguir para começar.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Implantar a aplicação de exemplo

O AWS Serverless Application Model Command Line Interface (SAM CLI) é uma extensão do AWS CLI que adiciona funcionalidades para construir e testar aplicações Lambda. Ele utiliza Docker para executar suas funções em um ambiente Amazon Linux que corresponde ao Lambda. Ele também pode emular o ambiente de construção e a API da sua aplicação.

Para usar o SAM CLI, você precisa das seguintes ferramentas:

* SAM CLI - [Instalar o SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 instalado](https://www.python.org/downloads/)
* Docker - [Instalar Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

Para construir e implantar sua aplicação pela primeira vez, execute os seguintes comandos no seu terminal:

```bash
sam build --use-container
sam deploy --guided
