ENVIRONMENT:=staging

init:
	cd tf && terraform init

plan:
	cd tf && terraform plan -var-file="${ENVIRONMENT}.tfvars"

apply:
	cd tf && terraform apply -var-file="${ENVIRONMENT}.tfvars"

destroy:
	cd tf && terraform destroy -var-file="${ENVIRONMENT}.tfvars"