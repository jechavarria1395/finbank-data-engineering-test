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

variable "data_factory_name" {
  default = "finbank-adf-demo"
}

variable "databricks_workspace_name" {
  default = "finbank-databricks-demo"
}

variable "key_vault_name" {
  default = "finbank-kv-demo-123"
}

variable "log_analytics_name" {
  default = "finbank-log-demo"
}