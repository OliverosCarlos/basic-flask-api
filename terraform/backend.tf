terraform {
 backend "gcs" {
   bucket  = "thekubekloud"
   prefix  = "terraform/state"
 }
 experiments = [module_variable_optional_attrs]
}