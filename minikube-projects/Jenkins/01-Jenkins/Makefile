start:
	minikube start -p my-minikube-cluster
	minikube -p my-minikube-cluster addons enable metrics-server
	terraform init
	terraform apply -auto-approve
	@jenkins_pod=$$(kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	adminPassword=$$(kubectl exec -i $$jenkins_pod -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword) && \
	echo "Admin password is: $$adminPassword"
	minikube tunnel -p my-minikube-cluster

start-with-kubectl:
	minikube start -p my-minikube-cluster
	minikube -p my-minikube-cluster addons enable metrics-server
	kubectl apply -f yaml/jenkins-namespace.yaml
	kubectl apply -f yaml/jenkins-service-account.yaml
	kubectl apply -f yaml/jenkins-volume.yaml
	kubectl apply -f yaml/jenkins-deployment.yaml
	@jenkins_pod=$$(kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	adminPassword=$$(kubectl exec -i $$jenkins_pod -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword) && \
	echo "Admin password is: $$adminPassword"
	minikube tunnel -p my-minikube-cluster

dashboard:
	minikube dashboard -p my-minikube-cluster

portforward:
	@jenkins_pod=$(shell kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	kubectl -n jenkins port-forward $$jenkins_pod 8080:8080

getadmin:
	@jenkins_pod=$$(kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	adminPassword=$$(kubectl exec -i $$jenkins_pod -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword) && \
	echo "Admin password is: $$adminPassword"

cleanup:
	minikube delete -p my-minikube-cluster
