pipeline {
    agent any

    stages {
        stage('Localizar entorno Jenkins') {
            steps {
                sh '''
                    echo "PID DEL SHELL: $$"
                    echo "Esperando 600 segundos..."
                    sleep 600
                '''
            }
        }
    }
}
