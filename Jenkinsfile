pipeline {
    agent none
    stages {
        stages('Build'){
            steps {
                sh 'python -m py_compile add.py main.py'
                stash(name: 'compilt-resuldts', includes: '.jenkins_python/*.py*')
            }
        }
    }
}