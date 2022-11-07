terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "3.1.0"
    }
  }
}

provider "null" {}

resource "null_resource" "run_docker_compose_create" {
    triggers = {
        always_run = timestamp()
    }
    provisioner "local-exec" {
        when = create
        on_failure = fail
        command = <<EOT
            cd ../
            cd docker
            docker-compose -p elk-stack up -d --build
        EOT
    }
}

resource "null_resource" "run_docker_compose_destroy" {
    triggers = {
        always_run = timestamp()
    }
    provisioner "local-exec" {
        when = destroy
        on_failure = fail
        command = <<EOT
            cd ../
            cd docker
            docker-compose -p elk-stack down
        EOT
    }
}
