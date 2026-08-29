pipeline {
    agent { label 'built-in' }

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el código del repositorio...'
                checkout scm
            }
        }

        stage('Verificar Docker') {
            steps {
                sh '/usr/bin/docker --version'
            }
        }

        stage('Construir Imagen Base') {
            steps {
                sh '/usr/bin/docker build -t atm-python-base:1.0 -f Dockerfile.base .'
            }
        }

        stage('Verificar Python') {
            steps {
                sh '/usr/bin/docker run --rm atm-python-base:1.0 python --version'
            }
        }

        stage('Ejecutar Pruebas Python') {
            steps {
                sh '/usr/bin/docker run --rm -v "$PWD:/app" -w /app atm-python-base:1.0 python test_atm.py'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh '/usr/bin/docker build -t atm-python:latest .'
            }
        }

        stage('Ejecutar Pruebas en Docker') {
            steps {
                sh '/usr/bin/docker run --rm atm-python:latest python test_atm.py'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente con Python, pruebas y Docker.'
            }
        }
    }
}
