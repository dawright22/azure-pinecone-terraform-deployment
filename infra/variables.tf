variable "region" {
  type    = string
  default = "eastus"
}

//vault address
variable "vault_addr" {
  type    = string
  default = "http://localhost:8200"
}

//vault token
variable "vault_token" {
  type    = string
  default = "s.1234567890"
}