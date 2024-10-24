pipeline {
    agent any
    stages {
        stage('Clean and Prepare Workspace') {
            steps {
                script {
                    sh '''
                        echo "Apagando todos os arquivos do diretório atual..."
                        rm -rf .[!.]* * || true  # Remove todos os arquivos, incluindo ocultos (exceto . e ..)

                        echo "Clonando o repositório mais recente do GitHub..."
                        git clone https://github.com/TSFZacks/jenkins_test.git .

                        echo "Verificando o conteúdo do diretório após a clonagem:"
                        pwd  # Mostra o caminho do diretório atual
                        ls -la  # Lista todos os arquivos no diretório atual

                        echo "Conteúdo do Dockerfile:"
                        cat Dockerfile || echo "Dockerfile não encontrado!"  # Verifica se o Dockerfile foi clonado corretamente
                    '''
                }
            }
        }

        stage('Clean Docker Environment') {
            steps {
                script {
                    sh '''
                        echo "Removendo todas as imagens Docker existentes..."
                        docker system prune -a -f  # Remove todas as imagens, containers, volumes e redes que não estão em uso
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        echo "Construindo a imagem Docker a partir do Dockerfile..."
                        docker build -t docker-images:latest .  # Cria a imagem a partir do Dockerfile no diretório clonado
                    '''
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    sh '''
                        echo "Marcando a imagem Docker com a tag correta..."
                        docker tag docker-images:latest 536697235329.dkr.ecr.eu-north-1.amazonaws.com/docker-images:v1.0.4  # Tag da imagem para ECR
                    '''
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh '''
                        echo "Autenticando no Amazon ECR..."

                        aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 536697235329.dkr.ecr.eu-north-1.amazonaws.com/docker-images

                        echo "Enviando a imagem Docker para o Amazon ECR..."
                        docker push 536697235329.dkr.ecr.eu-north-1.amazonaws.com/docker-images:v1.0.4  # Faz o push da imagem para o ECR
                    '''
                }
            }
        }

        stage('Run Code in Docker') {
            agent {
                docker {
                    image 'docker-images:latest'  // Usa a imagem recém-construída
                    args '-v /opt/chrome:/opt/chrome -v /opt/chromedriver:/opt/chromedriver --user=root'
                }
            }
            steps {
                script {
                    sh '''
                        echo "Verificando se o Chrome e o Chromedriver estão instalados corretamente:"
                        /opt/chrome/chrome-linux64/chrome --version
                        /opt/chromedriver/chromedriver-linux64/chromedriver --version

                        # Executar o script Python
                        echo "Executando script.py:"
                        python /var/lib/jenkins/workspace/Teste-Webhooks@2/script.py || echo "Erro: script.py não encontrado no diretório /var/lib/jenkins/workspace/Teste-Webhooks@2/"
                    '''
                }
            }
        }
    }
}
