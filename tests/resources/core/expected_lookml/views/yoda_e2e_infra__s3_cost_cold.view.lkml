view: yoda_e2e_infra__s3_cost_cold {
  sql_table_name: public_yoda_e2e_infra.s3_cost_cold ;;

  dimension_group: billing_period {
    type: time
    sql: ${TABLE}.billing_period ;;
    description: "Billing period date monthly"
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

  dimension_group: bill_start_date {
    type: time
    sql: ${TABLE}.bill_start_date ;;
    description: "Billing date for a specific S3 service (day granularity)"
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

  dimension: bucket {
    type: string
    sql: ${TABLE}.bucket ;;
    description: "Bucket Name"
  }

  dimension: product_product_family {
    type: string
    sql: ${TABLE}.product_product_family ;;
    description: "Data Transfer, API Request, Storage, Fee"
  }

  dimension: line_item_usage_type {
    type: string
    sql: ${TABLE}.line_item_usage_type ;;
    description: "Out/In-Bytes, Requests-Tier,TimedStorage, StorageAnalytics, DataTransfer, Inventory-ObjectsListed, Retrieval, EarlyDelete-ByteHrs"
  }

  dimension: cost {
    type: number
    sql: ${TABLE}.cost ;;
    description: "Cost per product family/usage type"
  }
}