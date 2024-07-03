# # Enable the Transit secrets engine
# resource "vault_mount" "transit" {
#   path        = "transit"
#   type        = "transit"
#   description = "Transit secrets engine for encryption/decryption tasks"
# }

# # Create a named encryption key for the Transit secrets engine
# resource "vault_transit_secret_backend_key" "orders" {
#   backend     = vault_mount.transit.path
#   name        = "orders"
#   deletion_allowed = true # Set to true to allow deletion of the key, if necessary
# }