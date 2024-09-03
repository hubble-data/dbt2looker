view: yoda_e2e_infra_stg__costpo_kubecost_snapshot {
  sql_table_name: protected_yoda_e2e_infra.costpo_kubecost_snapshot ;;

  dimension: average_of_cpu_efficiency {
    type: number
    sql: ${TABLE}.average_of_cpu_efficiency ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: average_of_ram_efficiency {
    type: number
    sql: ${TABLE}.average_of_ram_efficiency ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: kubecost_data_container {
    type: string
    sql: ${TABLE}.kubecost_data_container ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: kubecost_data_group {
    type: string
    sql: ${TABLE}.kubecost_data_group ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: kubecost_data_product_line {
    type: string
    sql: ${TABLE}.kubecost_data_product_line ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: kubecost_data_team {
    type: string
    sql: ${TABLE}.kubecost_data_team ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: savings_opportunities {
    type: number
    sql: ${TABLE}.savings_opportunities ;;
    description: "TODO: Update Column {col_name} Information"
  }

  dimension: total_cost {
    type: number
    sql: ${TABLE}.total_cost ;;
    description: "TODO: Update Column {col_name} Information"
  }

  measure: count {
    type: count
    description: "Default count measure"
  }
}