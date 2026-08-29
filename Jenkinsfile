pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el código del repositorio...'
                checkout scm
            }
        }

        stage('Verificar Python') {
            steps {
                sh 'sudo /usr/bin/nsenter -t 1 -m -- /usr/bin/python3.11 --version'
            }
        }

        stage('Verificar Docker') {
            steps {
                sh 'sudo /usr/bin/nsenter -t 1 -m -- /usr/bin/docker --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh '''
                    sudo /usr/bin/nsenter -t 1 -m -- /bin/sh -c \
                    "cd '$WORKSPACE' && /usr/bin/python3.11 -m pip install -r requirements.txt"
                '''
            }
        }

        stage('Ejecutar Pruebas Python') {
            steps {
                sh '''
                    sudo /usr/bin/nsenter -t 1 -m -- /bin/sh -c \
                    "cd '$WORKSPACE' && /usr/bin/python3.11 test_atm.py"
                '''
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh '''
                    sudo /usr/bin/nsenter -t 1 -m -- /bin/sh -c \
                    "cd '$WORKSPACE' && /usr/bin/docker build -t atm-python:latest ."
                '''
            }
        }

        stage('Ejecutar Pruebas en Docker') {
            steps {
                sh '''
                    sudo /usr/bin/nsenter -t 1 -m -- /bin/sh -c \
                    "/usr/bin/docker run --rm atm-python:latest python test_atm.py"
                '''
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente con Python, pruebas y Docker.'
            }
        }
    }
}
