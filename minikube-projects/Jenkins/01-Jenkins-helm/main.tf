resource "kubernetes_persistent_volume" "jenkins_pv" {
  metadata {
    name = "jenkins-pv"
  }

  spec {
    capacity = {
      storage = "8Gi"
    }

    access_modes = ["ReadWriteOnce"]

    persistent_volume_reclaim_policy = "Retain"

    persistent_volume_source {
      host_path {
        path = "/mnt/data" # Change this path as necessary for your environment
      }
    }
  }
}

resource "kubernetes_persistent_volume_claim" "jenkins_pvc" {
  metadata {
    name      = "jenkins-pvc"
    namespace = "default"
  }

  spec {
    access_modes = ["ReadWriteOnce"]

    resources {
      requests = {
        storage = "8Gi"
      }
    }
  }
}

resource "helm_release" "jenkins" {
  name       = "jenkins"
  namespace  = "default"
  chart      = "jenkins"
  repository = "https://charts.jenkins.io"
  version    = "5.1.2" # Specify a valid version
  wait       = false // Do not wait for the helm_release to fully deploy as we need to run minikube tunnel

  values = [
    "${file("values.yaml")}"
  ]

  set {
    name  = "controller.admin.password"
    value = "admin1234"
  }

  set {
    name  = "controller.serviceType"
    value = "LoadBalancer"
  }

  set {
    name  = "controller.persistentVolumeClaim.existingClaim"
    value = kubernetes_persistent_volume_claim.jenkins_pvc.metadata[0].name
  }

  set {
    name = "controller.probes.startupProbe.httpGet.path"
    value = "/login"
  }

  set {
    name = "controller.probes.failureTreshold"
    value = "13"
  }

  set {
    name = "controller.probes.periodSeconds"
    value = "20"
  }

  set {
    name = "controller.probes.timeoutSeconds"
    value = "25"
  }

  set {
    name = "controller.probes.initialDelaySeconds"
    value = "25"
  }
}

