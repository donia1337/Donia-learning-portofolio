pipelineJob('my-pipeline-job') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        url('https://github.com/donia1337/Donia-learning-portofolio/minikube-projects/Jenkins/02-Job-DSL')
                    }
                    branches('main')
                }
            }
            scriptPath('Jenkinsfile')
        }
    }
}
