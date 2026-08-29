pipeline {
     agent { label 'built-in' }
    
     environment {
     PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
}

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el código del repositorio...'
                checkout scm
            }
        }

        stage('Verificar Python') {
            steps {
                sh 'command -v python3.11 && python3.11 --version'
            }
        }

        stage('Verificar Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh 'python3.11 -m pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas Python') {
            steps {
                sh 'python3.11 test_atm.py'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t atm-python:latest .'
            }
        }

        stage('Ejecutar Pruebas en Docker') {
            steps {
                sh 'docker run --rm atm-python:latest python test_atm.py'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente con Python, pruebas y Docker.'
            }
        }
    }
}
