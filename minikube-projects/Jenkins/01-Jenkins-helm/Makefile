start:
	minikube start -p jenkins-cluster
	minikube -p jenkins-cluster addons enable metrics-server
	minikube -p jenkins-cluster addons enable metallb
	terraform init
	terraform apply -auto-approve
	@open http://localhost:8080/
	@minikube tunnel -p jenkins-cluster





cleanup:
	minikube delete -p jenkins-cluster


