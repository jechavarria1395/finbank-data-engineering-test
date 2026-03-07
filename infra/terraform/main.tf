resource "azurerm_resource_group" "finbank_rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "datalake" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.finbank_rg.name
  location                 = azurerm_resource_group.finbank_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  is_hns_enabled = true
}

resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_name  = azurerm_storage_account.datalake.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_name  = azurerm_storage_account.datalake.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_name  = azurerm_storage_account.datalake.name
  container_access_type = "private"
}


resource "azurerm_mssql_server" "sql_server" {
  name                         = var.sql_server_name
  resource_group_name          = azurerm_resource_group.finbank_rg.name
  location                     = azurerm_resource_group.finbank_rg.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_login
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_mssql_database" "sql_database" {
  name      = var.sql_database_name
  server_id = azurerm_mssql_server.sql_server.id
  sku_name  = "Basic"
}

resource "azurerm_mssql_firewall_rule" "allow_my_ip" {
  name             = "AllowMyIP"
  server_id        = azurerm_mssql_server.sql_server.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}


resource "azurerm_log_analytics_workspace" "log_analytics" {
  name                = var.log_analytics_name
  location            = azurerm_resource_group.finbank_rg.location
  resource_group_name = azurerm_resource_group.finbank_rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}


resource "azurerm_data_factory" "data_factory" {
  name                = var.data_factory_name
  location            = azurerm_resource_group.finbank_rg.location
  resource_group_name = azurerm_resource_group.finbank_rg.name
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "key_vault" {
  name                        = var.key_vault_name
  location                    = azurerm_resource_group.finbank_rg.location
  resource_group_name         = azurerm_resource_group.finbank_rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = false
}

resource "azurerm_databricks_workspace" "databricks" {
  name                = var.databricks_workspace_name
  location            = azurerm_resource_group.finbank_rg.location
  resource_group_name = azurerm_resource_group.finbank_rg.name
  sku                 = "standard"
}