connection: "yoda"
include: "views/*"

explore: yoda_e2e_loyalty__fact_store_profile_daily {
  description: "yoda_e2e_loyalty store profile measures"

  join: yoda_e2e_platform__dim_stores {
    type: inner
    relationship: many_to_one
    sql_on: ${yoda_e2e_loyalty__fact_store_profile_daily.app_key} = ${yoda_e2e_platform__dim_stores.app_key} ;;
  }

  sql_always_where: yoda_e2e_loyalty__fact_store_profile_daily.count_campaigns = {% parameter yoda_e2e_platform__dim_stores.past_num_days %} ;;
}