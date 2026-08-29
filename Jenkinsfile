pipeline {
    agent { label 'built-in' }

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo el código del repositorio...'
                checkout scm
            }
        }

        stage('Diagnostico Jenkins') {
            steps {
                sh '''
                    echo "===== DIAGNOSTICO DEL ENTORNO JENKINS ====="
                    echo "Usuario:"
                    whoami

                    echo "PATH:"
                    echo "$PATH"

                    echo "Directorio actual:"
                    pwd

                    echo "Verificando Docker:"
                    if [ -e /usr/bin/docker ]; then
                        echo "DOCKER EXISTE"
                    else
                        echo "DOCKER NO EXISTE"
                    fi

                    if [ -x /usr/bin/docker ]; then
                        echo "DOCKER ES EJECUTABLE"
                    else
                        echo "DOCKER NO ES EJECUTABLE"
                    fi

                    echo "Verificando Python:"
                    if [ -e /usr/bin/python3.11 ]; then
                        echo "PYTHON EXISTE"
                    else
                        echo "PYTHON NO EXISTE"
                    fi

                    if [ -x /usr/bin/python3.11 ]; then
                        echo "PYTHON ES EJECUTABLE"
                    else
                        echo "PYTHON NO ES EJECUTABLE"
                    fi

                    echo "Archivos:"
                    /bin/ls -l /usr/bin/docker /usr/bin/python3.11 || true

                    echo "===== FIN DEL DIAGNOSTICO ====="
                '''
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
