terraform {
  required_version = ">= 0.13"

  required_providers {
    kubectl = { source  = "gavinbunney/kubectl", version = ">= 1.7.0" }
    kubernetes = { source = "hashicorp/kubernetes", version = "2.17.0"}
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
  config_context = "my-minikube-cluster"
}
