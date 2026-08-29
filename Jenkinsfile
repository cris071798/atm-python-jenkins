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
                sh '/usr/bin/python3.11 --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh '/usr/bin/python3.11 -m pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh '/usr/bin/python3.11 test_atm.py'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente.'
            }
        }
    }
}
