\# Store Platform (Local Kubernetes Stack)



Tech Stack:

\- FastAPI backend

\- WordPress frontend

\- MariaDB

\- Docker

\- kind (Kubernetes)

\- Helm



Run order:



Backend:

cd backend

docker build -t store-backend:1.0 .

kind load docker-image store-backend:1.0 --name urumi

kubectl apply -f k8s.yaml

kubectl port-forward svc/store-backend 8000:8000



Frontend:

helm install demo bitnami/wordpress --set service.type=NodePort

kubectl port-forward svc/demo-wordpress 9090:80



