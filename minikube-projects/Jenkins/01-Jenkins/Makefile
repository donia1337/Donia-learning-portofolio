start:
	minikube start -p my-minikube-cluster
	minikube -p my-minikube-cluster addons enable metrics-server
	kubectl apply -f yaml/jenkins-namespace.yaml
	kubectl apply -f yaml/jenkins-service-account.yaml
	kubectl apply -f yaml/jenkins-volume.yaml
	kubectl apply -f yaml/jenkins-deployment.yaml
	@jenkins_pod=$(shell kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	adminPassword=$(shell kubectl exec -it $$jenkins_pod cat /var/jenkins_home/secrets/initialAdminPassword -n jenkins) && \
	echo "Admin password is: $$adminPassword"
	@jenkins_pod=$(shell kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	kubectl -n jenkins port-forward $$jenkins_pod 8080:8080

dashboard:
	minikube dashboard -p my-minikube-cluster

portforward:
	@jenkins_pod=$(shell kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	kubectl -n jenkins port-forward $$jenkins_pod 8080:8080

getadmin:
	@jenkins_pod=$$(kubectl get pods -n jenkins | grep -o 'jenkins-[^ ]*') && \
	adminPassword=$$(kubectl exec -i $$jenkins_pod -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword) && \
	echo "Admin password is: $$adminPassword"

