view: yoda_e2e_platform__dim_stores {
  sql_table_name: public_yoda_e2e_platform.dim_stores ;;

  dimension_group: store_created_at {
    type: time
    sql: ${TABLE}.store_created_at ;;
    description: "TODO: Update Table Description"
    datatype: timestamp
    timeframes: [
      raw,
      time,
      hour,
      date,
      week,
      month,
      quarter,
      year,
    ]
  }

  dimension_group: merchant_created_at {
    type: time
    sql: ${TABLE}.merchant_created_at ;;
    description: "TODO: Update Table Description"
    datatype: timestamp
    timeframes: [
      raw,
      time,
      hour,
      date,
      week,
      month,
      quarter,
      year,
    ]
  }

  dimension_group: dwh_updated_at {
    type: time
    sql: ${TABLE}.dwh_updated_at ;;
    description: "TODO: Update Table Description"
    datatype: timestamp
    timeframes: [
      raw,
      time,
      hour,
      date,
      week,
      month,
      quarter,
      year,
    ]
  }

  dimension: store_id {
    type: number
    sql: ${TABLE}.store_id ;;
    description: "TODO: Update Table Description"
    primary_key: yes
  }

  dimension: organization_id {
    type: number
    sql: ${TABLE}.organization_id ;;
    description: "TODO: Update Table Description"
  }

  dimension: app_key {
    type: string
    sql: ${TABLE}.app_key ;;
    description: "TODO: Update Table Description"
  }

  dimension: store_domain {
    type: string
    sql: ${TABLE}.store_domain ;;
    description: "TODO: Update Table Description"
  }

  dimension: is_test_store {
    type: number
    sql: ${TABLE}.is_test_store ;;
    description: "TODO: Update Table Description"
  }

  dimension: is_active_store {
    type: number
    sql: ${TABLE}.is_active_store ;;
    description: "TODO: Update Table Description"
  }

  dimension: store_name {
    type: string
    sql: ${TABLE}.store_name ;;
    description: "TODO: Update Table Description"
  }

  dimension: store_language {
    type: string
    sql: ${TABLE}.store_language ;;
    description: "TODO: Update Table Description"
  }

  dimension: platform_name {
    type: string
    sql: ${TABLE}.platform_name ;;
    description: "TODO: Update Table Description"
  }

  dimension: is_blacklisted {
    type: number
    sql: ${TABLE}.is_blacklisted ;;
    description: "TODO: Update Table Description"
  }

  dimension: merchant_id {
    type: number
    sql: ${TABLE}.merchant_id ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_company_name {
    type: string
    sql: ${TABLE}.loyalty_company_name ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_currency {
    type: string
    sql: ${TABLE}.loyalty_currency ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_platform {
    type: string
    sql: ${TABLE}.loyalty_platform ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_is_completed_profile {
    type: number
    sql: ${TABLE}.loyalty_is_completed_profile ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_is_redemptions_enabled {
    type: number
    sql: ${TABLE}.loyalty_is_redemptions_enabled ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_plan {
    type: string
    sql: ${TABLE}.loyalty_plan ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_contact_email {
    type: string
    sql: ${TABLE}.loyalty_contact_email ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_is_test_account {
    type: number
    sql: ${TABLE}.loyalty_is_test_account ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_opt_in_strategy {
    type: number
    sql: ${TABLE}.loyalty_opt_in_strategy ;;
    description: "TODO: Update Table Description"
  }

  dimension: referral_opt_in_strategy {
    type: number
    sql: ${TABLE}.referral_opt_in_strategy ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_group_id {
    type: string
    sql: ${TABLE}.loyalty_group_id ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_vip_type {
    type: string
    sql: ${TABLE}.loyalty_vip_type ;;
    description: "TODO: Update Table Description"
  }

  dimension: loyalty_is_vip_enabled {
    type: number
    sql: ${TABLE}.loyalty_is_vip_enabled ;;
    description: "TODO: Update Table Description"
  }
}