view: yoda_e2e_bi___loyalty__fact_purchases {
  sql_table_name: public_yoda_e2e_bi.loyalty_fact_purchases ;;

  dimension_group: purchase_created_at {
    type: time
    sql: ${TABLE}.purchase_created_at ;;
    description: "TODO: Update Column {col_name} Information"
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

  dimension_group: purchase_updated_at {
    type: time
    sql: ${TABLE}.purchase_updated_at ;;
    description: "TODO: Update Column {col_name} Information"
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

  dimension_group: purchase_date {
    type: time
    sql: ${TABLE}.purchase_date ;;
    description: "TODO: Update Column {col_name} Information"
    datatype: datetime
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
    description: "TODO: Update Column {col_name} Information"
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

  dimension: purchase_id {
    type: number
    sql: ${TABLE}.purchase_id ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_before_swell_acquisition {
    type: number
    sql: ${TABLE}.is_before_swell_acquisition ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_applied_to_campaigns {
    type: number
    sql: ${TABLE}.is_applied_to_campaigns ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_fraud_review {
    type: number
    sql: ${TABLE}.is_fraud_review ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_swell_user {
    type: number
    sql: ${TABLE}.is_swell_user ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_move_merchant_to_new_tier {
    type: number
    sql: ${TABLE}.is_move_merchant_to_new_tier ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: purchase_value_cents_in_original_currency {
    type: number
    sql: ${TABLE}.purchase_value_cents_in_original_currency ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: purchase_currency {
    type: string
    sql: ${TABLE}.purchase_currency ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: discount_cents_in_original_currency {
    type: number
    sql: ${TABLE}.discount_cents_in_original_currency ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: billing_city {
    type: string
    sql: ${TABLE}.billing_city ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: shipping_country_code {
    type: string
    sql: ${TABLE}.shipping_country_code ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: shipping_city {
    type: string
    sql: ${TABLE}.shipping_city ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: customer_ip_address {
    type: string
    sql: ${TABLE}.customer_ip_address ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: browser_country_code {
    type: string
    sql: ${TABLE}.browser_country_code ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: store_address {
    type: string
    sql: ${TABLE}.store_address ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: store_city {
    type: string
    sql: ${TABLE}.store_city ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: store_state {
    type: string
    sql: ${TABLE}.store_state ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: referral_discount_code_id__swell_referral_discount_code {
    type: number
    sql: ${TABLE}.referral_discount_code_id__swell_referral_discount_code ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: merchant_id__dim_stores {
    type: number
    sql: ${TABLE}.merchant_id__dim_stores ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: customer_id__swell_customers {
    type: number
    sql: ${TABLE}.customer_id__swell_customers ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: referral_id__swell_referrals {
    type: number
    sql: ${TABLE}.referral_id__swell_referrals ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: user_agent_id__swell_user_agent {
    type: number
    sql: ${TABLE}.user_agent_id__swell_user_agent ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: redemption_code_id__swell_redemption_code {
    type: number
    sql: ${TABLE}.redemption_code_id__swell_redemption_code ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: order_id__fact_orders {
    type: string
    sql: ${TABLE}.order_id__fact_orders ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: app_key {
    type: string
    sql: ${TABLE}.app_key ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: store_id {
    type: number
    sql: ${TABLE}.store_id ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: store_name {
    type: string
    sql: ${TABLE}.store_name ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: organization_id {
    type: number
    sql: ${TABLE}.organization_id ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_test_store {
    type: number
    sql: ${TABLE}.is_test_store ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: is_active_store {
    type: number
    sql: ${TABLE}.is_active_store ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: platform_name {
    type: string
    sql: ${TABLE}.platform_name ;;
    description: "TODO: Update Column {col_name} Information"
  }
}