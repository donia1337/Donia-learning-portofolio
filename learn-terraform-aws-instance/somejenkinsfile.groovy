pipeline {
    agent none
    stages {
        stage('Stage 1') {
            agent {
                kubernetes {
                    label 'agent1'
                    defaultContainer 'agent'
                }
            }
            steps {
                // Steps for Stage 1
            }
        }
        stage('Stage 2') {
            agent {
                kubernetes {
                    label 'agent2'
                    defaultContainer 'agent'
                }
            }
            steps {
                // Steps for Stage 2
            }
        }
    }
}
