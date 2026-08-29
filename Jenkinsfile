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
                sh 'python3 --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh 'python3 test_atm.py'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente.'
            }
        }
    }
}
