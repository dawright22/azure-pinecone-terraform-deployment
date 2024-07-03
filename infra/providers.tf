# Azure provider version
terraform {
  required_version = ">= 1.3.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0, < 4.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.3.2"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "random" {}

# # Configure the Vault provider to interact with the newly created cluster
# provider "vault" {
#   address = var.vault_addr
#   token = var.vault_token
#     # Ensure you have a method to authenticate to Vault, such as a token.
# }