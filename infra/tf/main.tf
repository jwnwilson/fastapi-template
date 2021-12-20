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

module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  name          = "pdf-generator-api"
  description   = "My pdf generator service"
  protocol_type = "HTTP"

  cors_configuration = {
    allow_headers = ["content-type", "x-amz-date", "authorization", "x-api-key", "x-amz-security-token", "x-amz-user-agent"]
    allow_methods = ["*"]
    allow_origins = ["*"]
  }

  # Custom domain
  # domain_name                 = "terraform-aws-modules.modules.tf"
  # domain_name_certificate_arn = "arn:aws:acm:eu-west-1:052235179155:certificate/2b3a7ed9-05e1-4f9e-952b-27744ba06da6"

  # Access logs
  # default_stage_access_log_destination_arn = "arn:aws:logs:eu-west-1:835367859851:log-group:debug-apigateway"
  # default_stage_access_log_format          = "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId $context.integrationErrorMessage"

  # Routes and integrations
  integrations = {
    "GET /" = {
      lambda_arn             = module.pdf_api.lambda_function_arn
      payload_format_version = "2.0"
      timeout_milliseconds   = 12000
    }

    "$default" = {
      lambda_arn = module.pdf_api.lambda_function_arn
    }
  }

  tags = {
    Name = "http-apigateway"
  }
}

module "pdf_api" {
  source                  = "terraform-aws-modules/lambda/aws"

  function_name           = "pdf_api"
  description             = "PDF creator API"

  create_package          = false

  image_uri               = "${module.docker_images.ecr_api_url}:20122021-18"
  package_type            = "Image"
  vpc_subnet_ids          = module.vpc.intra_subnets
  vpc_security_group_ids  = [module.vpc.default_security_group_id]
  attach_network_policy   = true

  allowed_triggers = {
  APIGatewayAny = {
    service    = "apigateway"
    source_arn = module.api_gateway.apigatewayv2_api_arn
  }
}

module "docker_images" {
  source = "./modules/images/aws"

  api_repo        = var.api_repo
  access_key      = var.aws_access_key
  secret_key      = var.aws_secret_key
  region          = var.aws_region
}
