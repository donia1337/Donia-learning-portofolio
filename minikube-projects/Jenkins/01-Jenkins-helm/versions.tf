terraform {
  required_version = ">= 0.13"

  required_providers {
    kubectl = { source  = "gavinbunney/kubectl", version = ">= 1.7.0" }
    kubernetes = { source = "hashicorp/kubernetes", version = "2.17.0"}
    helm = { source = "hashicorp/helm", version = "2.13.2"}
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
  config_context = "jenkins-cluster"
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}
