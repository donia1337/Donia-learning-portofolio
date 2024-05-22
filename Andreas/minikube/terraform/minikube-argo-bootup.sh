#!/usr/bin/env bash
minikube start --nodes 2 -p argocd-helm
terraform init
terraform apply --auto-approve

argocdPassword=$(kubectl get secrets argocd-initial-admin-secret -o yaml -n argocd | grep "password:" | awk '{print $2}' | base64 -d)

echo "Minikube cluster: argocd-helm has successfully been deployed"
echo "---------------------------------------------------------------------------------"
echo "The login for argocd is as follows:"
echo "Username: admin"
echo "Password: $argocdPassword"
echo "Connect to argocd on your local browser at localhost:8080"
echo "---------------------------------------------------------------------------------"
echo "Portforwarding to localhost:8080 - Press Control+C to cancel"
kubectl port-forward svc/argocd-server -n argocd 8080:80