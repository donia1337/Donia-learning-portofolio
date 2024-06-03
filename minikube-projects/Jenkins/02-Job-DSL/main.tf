data "kubectl_file_documents" "seed_job" {
    content = file("${path.module}/yaml/seed-job.yaml")
}

resource "kubectl_manifest" "seed_job" {
    for_each  = data.kubectl_file_documents.seed_job.manifests
    yaml_body = each.value
}
