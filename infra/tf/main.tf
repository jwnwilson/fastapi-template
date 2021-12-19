terraform {
  backend "s3" {
    region = "eu-west-1"
  }
}

provider "aws" {
  region  = var.aws_region
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "${var.project}-vpc"
  cidr = "10.10.0.0/16"

  azs           = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  intra_subnets = ["10.10.101.0/24", "10.10.102.0/24", "10.10.103.0/24"]

  # Add public_subnets and NAT Gateway to allow access to internet from Lambda
  # public_subnets  = ["10.10.1.0/24", "10.10.2.0/24", "10.10.3.0/24"]
  # enable_nat_gateway = true
}

module "pdf_api" {
  source                  = "terraform-aws-modules/lambda/aws"

  function_name           = "pdf_api"
  description             = "PDF creator API"

  create_package          = false

  image_uri               = "${module.docker_images.ecr_api_url}:19122021-13"
  package_type            = "Image"
  vpc_subnet_ids          = module.vpc.intra_subnets
  vpc_security_group_ids  = [module.vpc.default_security_group_id]
  attach_network_policy   = true
}

module "docker_images" {
  source = "./modules/images/aws"

  api_repo        = var.api_repo
  access_key      = var.aws_access_key
  secret_key      = var.aws_secret_key
  region          = var.aws_region
}
