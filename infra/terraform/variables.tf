variable "resource_group_name" {
  default = "finbank-data-rg"
}

variable "location" {
  default = "Central US"
}

variable "storage_account_name" {
  default = "finbankdatalake123"
}

variable "sql_server_name" {
  default = "finbank-sql-server-demo"
}

variable "sql_database_name" {
  default = "finbank-sql-db"
}

variable "sql_admin_login" {
  default = "azureadmin"
}

variable "sql_admin_password" {
  description = "SQL admin password"
  sensitive   = true
}