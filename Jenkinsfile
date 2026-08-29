pipeline {
    agent any

    stages {
        stage('Diagnostico Final') {
            steps {
                sh '''
                    echo "===== PROCESO DEL PIPELINE ====="
                    echo "PID SHELL: $$"
                    echo "PPID: $PPID"

                    echo "===== MOUNT DEL SHELL ====="
                    readlink /proc/$$/ns/mnt || true

                    echo "===== ROOT DEL SHELL ====="
                    readlink /proc/$$/root || true

                    echo "===== PROCESOS JAVA ====="
                    ps -ef | grep java || true

                    echo "===== ARCHIVOS VISIBLES ====="
                    ls -l /usr/bin/git || true
                    ls -l /usr/bin/docker || true
                    ls -l /usr/bin/python3.11 || true

                    echo "===== PROBAR ROOT DEL PID 1 ====="
                    ls -l /proc/1/root/usr/bin/docker || true
                    ls -l /proc/1/root/usr/bin/python3.11 || true

                    /proc/1/root/usr/bin/docker --version || true
                    /proc/1/root/usr/bin/python3.11 --version || true
                '''
            }
        }
    }
}
