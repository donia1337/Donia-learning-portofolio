resource "kubernetes_namespace" "jenkins" {
    metadata {
        name = "jenkins"
    }
}

data "kubectl_file_documents" "jenkins_service_account" {
    content = file("${path.module}/yaml/jenkins-service-account.yaml")
}

resource "kubectl_manifest" "jenkins_service_account" {
    for_each  = data.kubectl_file_documents.jenkins_service_account.manifests
    yaml_body = each.value
}

data "kubectl_file_documents" "jenkins-volume" {
    content = file("${path.module}/yaml/jenkins-volume.yaml")
}

resource "kubectl_manifest" "jenkins-volume" {
    for_each  = data.kubectl_file_documents.jenkins-volume.manifests
    yaml_body = each.value
}

resource "kubectl_manifest" "jenkins_deployment" {
    yaml_body = file("${path.module}/yaml/jenkins-deployment.yaml")
}
