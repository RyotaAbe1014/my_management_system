<script>
import { Doughnut } from 'vue-chartjs'

export default ({
  extends: Doughnut,
  data() {
    return {
      datas: {
        labels: ["完了", "未完了"],
        // 表示するデータ
        datasets: [
          {
            data: [10, 2],
            backgroundColor: ['#89c3eb', '#f87979']
          }
        ]
      },
      options: {
        responsive: true
      }
    }
  },
  mounted() {
    this.renderChart(this.datas, this.options)
  }
})
</script>